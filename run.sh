#!/bin/bash

docker login
docker pull tyxuan/covid:tagname
#cat ~/access_token.txt | docker login --username tyxuan --password-stdin
docker container run -d tyxuan/covid:tagname
#docker container run -d --name serene_ptolemy -it tyxuan/covid:tagname
docker exec serene_ptolemy pwd /usr/share
docker cp serene_ptolemy:/usr/share/COVID-19_Radiography_Dataset data/
python src/dataprocessing.py
python src/modeling.py