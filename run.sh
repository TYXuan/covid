#!/bin/bash

winpty docker login -u tyxuan
cat ~/.docker/config.json
docker run -d --name e9c79ca11ef4e7e4b8bc8ae078f0c89d56e75c45007b1bef3eff1418ff045376 -it f9c14fe76d50
docker exec e9c79ca11ef4e7e4b8bc8ae078f0c89d56e75c45007b1bef3eff1418ff045376 pwd /usr/share
docker cp e9c79ca11ef4e7e4b8bc8ae078f0c89d56e75c45007b1bef3eff1418ff045376:/usr/share/COVID-19_Radiography_Dataset data/
python src/dataprocessing.py
python src/modeling.py