from data import make_dataset
import pandas as pd

# Download data and save in local folder
import wget
print('Downloading data...')

url = "https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database/download"
wget.download(url, './data/')
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