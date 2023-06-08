from data import make_dataset
import pandas as pd

# Import dataset
levels = ['Normal/images', 'COVID/images', 'Viral Pneumonia/images']
path = "./data/COVID-19_Radiography_Dataset"
label_dict = {'Normal/images':'normal', 'COVID/images':'covid', 'Viral Pneumonia/images':'pneumonia'}

df = make_dataset.read_img_file(path=path, levels=levels, label_dict=label_dict)
print('Dataset is imported!')

# Save dataset
df.to_csv(r'./data/covid.csv')
print('Dataset saved into csv format!')