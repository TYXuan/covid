from data import make_dataset
import pandas as pd

# Download data and save in local folder
print('Downloading data...')

import os
os.environ['KAGGLE_USERNAME'] = "yxuann"
os.environ['KAGGLE_KEY'] = "ac36787803b525335ecb015f9afb789f"

from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()
api.dataset_download_files('tawsifurrahman/covid19-radiography-database', path="./data/")

from zipfile import ZipFile
with ZipFile("./data/covid19-radiography-database.zip", "r") as zObject:
    zObject.extractall(path="./data/")
print('Data downloaded!')

# Import dataset
levels = ['Normal/images', 'COVID/images', 'Viral Pneumonia/images']
path = "./data/COVID-19_Radiography_Dataset"
label_dict = {'Normal/images':'normal', 'COVID/images':'covid', 'Viral Pneumonia/images':'pneumonia'}

df = make_dataset.read_img_file(path=path, levels=levels, label_dict=label_dict)
print('Dataset is imported!')

# Save dataset
df.to_csv(r'./data/covid.csv')
print('Dataset saved into csv format!')