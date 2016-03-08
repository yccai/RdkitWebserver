from django.shortcuts import render
import json
from django.http import HttpResponse
# Create your views here.

import rdkit
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D

import uuid

def index(request):

	response_data = {}
	response_data["module"] = rdkit.__repr__()

	return HttpResponse(json.dumps(response_data), content_type="application/json")


def validate(request, smiles):

	mol = Chem.MolFromSmiles(str(smiles))

	response_data = {}
	response_data["module"] = rdkit.__repr__()
	response_data["smiles"] = smiles
	response_data["is_valid"] = (mol != None)
	if mol: response_data["mol"] = mol.__repr__()

	return HttpResponse(json.dumps(response_data), content_type="application/json")

def png(request, smiles):
	mol = Chem.MolFromSmiles(str(smiles))
	image = Draw.MolToImage(mol)
	response = HttpResponse(mimetype="image/png")
	image.save(response, "PNG")
	return response

def moltosvg(mol,molSize=(450,150),kekulize=True):
    mc = Chem.Mol(mol.ToBinary())
    if kekulize:
        try:
            Chem.Kekulize(mc)
        except:
            mc = Chem.Mol(mol.ToBinary())
    if not mc.GetNumConformers():
        rdDepictor.Compute2DCoords(mc)
    drawer = rdMolDraw2D.MolDraw2DSVG(molSize[0],molSize[1])
    drawer.DrawMolecule(mc)
    drawer.FinishDrawing()
    svg = drawer.GetDrawingText()
    # It seems that the svg renderer used doesn't quite hit the spec.
    # Here are some fixes to make it work in the notebook, although I think
    # the underlying issue needs to be resolved at the generation step
    return svg #.replace('svg:','')

def svg(request, smiles):
        mol = Chem.MolFromSmiles(str(smiles))
	svg = moltosvg(mol)
        return HttpResponse(svg, mimetype="image/svg+xml")

