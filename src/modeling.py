import pandas as pd
import numpy as np
from data.make_dataset import img_data_array
from tensorflow.keras.models import load_model

print('Importing dataset from ./data...')
df = pd.read_csv('./data/covid.csv', index_col=[0])

# Balance dataset
print('Balancing dataset...')

normal = df[df['label'] == 'normal']
pneumonia = df[df['label'] == 'pneumonia']
covid = df[df['label'] == 'covid']

normal = normal.sample(n=len(pneumonia), random_state=123)
covid = covid.sample(n=len(pneumonia), random_state=123)

balanced_data = pd.concat([normal, covid, pneumonia]).reset_index(drop = True)

# Converting images into array then scale all pixels to a range of [0,1]
print('Storing images to array in a range of [0,1]...')

image_size = (128,128)
X = img_data_array(balanced_data, image_size=image_size)

# Load CNN model
print('Loading model...')
cnn_model = load_model('./src/models/cnn_model.hdf5')

batch_size = 50
y_pred = cnn_model.predict(x=X, batch_size=batch_size)

y_pred_df = pd.DataFrame(data=y_pred.argmax(axis=1), columns=["predicted_labels"])

label_dict = {1:'normal', 0:'covid', 2:'pneumonia'}
y_pred_df = y_pred_df['predicted_labels'].map(label_dict)

results = balanced_data[['image_file']].join(y_pred_df)
results.to_csv(r'./data/cnn_results.csv')
print('Results saved into csv format!')


