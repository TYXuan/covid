#!/bin/bash

docker login
docker pull tyxuan/covid:tagname
#cat ~/access_token.txt | docker login --username tyxuan --password-stdin
docker run -d --name 86a85c70adef21307e924bcabbfddf256fc81f24ff7e8dabe8d9ea70e99f3ba3 -it f9c14fe76d50
docker exec 86a85c70adef21307e924bcabbfddf256fc81f24ff7e8dabe8d9ea70e99f3ba3 pwd /usr/share
docker cp 86a85c70adef21307e924bcabbfddf256fc81f24ff7e8dabe8d9ea70e99f3ba3:/usr/share/COVID-19_Radiography_Dataset data/
python src/dataprocessing.py
python src/modeling.py