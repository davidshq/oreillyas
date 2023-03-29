#!/bin/bash

rm -rf tmp
mkdir tmp
cd tmp
dolt init
dolt sql < dolt-schema.sql
dolt table import -u books oreilly_mod.csv
