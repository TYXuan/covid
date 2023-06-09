#!/bin/bash

docker login
docker pull tyxuan/covid:tagname
#cat ~/access_token.txt | docker login --username tyxuan --password-stdin
docker run -d --name 86a85c70adef -it f9c14fe76d50
docker exec 86a85c70adef pwd /usr/share
docker cp 86a85c70adef:/usr/share/COVID-19_Radiography_Dataset data/
python src/dataprocessing.py
python src/modeling.py