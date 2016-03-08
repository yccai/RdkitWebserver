#!/usr/bin/env bash

rm *.svg

for line in $(cat molecules.csv); do
  echo $line
  name=${line%,*}
  smiles=${line#*,}
  wget http://ec2-52-31-145-209.eu-west-1.compute.amazonaws.com:8080/smiles/"${smiles}"/svg -O $name.svg
done
