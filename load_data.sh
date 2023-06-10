#!/bin/sh
mkdir -p data/raw 
rm data/raw/*.csv; rm data/raw/*.geojson; rm data/raw/*.zip;

echo "Downloading data.. be patient, please!";
cd data/raw;

wget https://cdn.buenosaires.gob.ar/datosabiertos/datasets/sbase/subte-estaciones/estaciones-de-subte.geojson

wget https://cdn.buenosaires.gob.ar/datosabiertos/datasets/sbase/subte-estaciones/lineas-de-subte.csv

wget https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-educacion/barrios/barrios.csv
wget https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-educacion/barrios/barrios.geojson

wget https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/ciclovias/ciclovias_WGS84.csv
wget https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/ciclovias/ciclovias_WGS84.geojson
wget https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/ciclovias/ciclovias_WGS84.geojson

wget https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/bicicletas-publicas/recorridos-realizados-2023.zip
unzip recorridos-realizados-2023.zip

wget https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/bicicletas-publicas/recorridos-realizados-2022.zip
unzip recorridos-realizados-2022.zip

wget https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/bicicletas-publicas/recorridos-realizados-2021.zip
unzip recorridos-realizados-2021.zip

wget https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/bicicletas-publicas/recorridos-realizados-2020.zip
unzip recorridos-realizados-2020.zip

wget https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/bicicletas-publicas/usuarios_ecobici_2019.csv
wget https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/bicicletas-publicas/usuarios-ecobici-2018.csv
wget https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/bicicletas-publicas/usuarios-ecobici-2017.csv
wget https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/bicicletas-publicas/usuarios-ecobici-2016.csv
wget https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/bicicletas-publicas/usuarios-ecobici-2015.csv
rm *.zip