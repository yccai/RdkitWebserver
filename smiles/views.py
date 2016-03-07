from django.shortcuts import render
import json
from django.http import HttpResponse
# Create your views here.

import rdkit
from rdkit import Chem
from rdkit.Chem import Draw
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
