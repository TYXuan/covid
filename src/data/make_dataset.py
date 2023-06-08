import os
import numpy as np
import pandas as pd
import cv2

def read_img_file(path, levels, label_dict):
    """Extracts contents of file into pandas DataFrame 

    Args:
        path (string): Location of the folder where all files are stored.
        levels (list): Location of the pictures of specific labels.
        label_dict (dictionary): Name of labels to map with levels.

    Returns:
        pandas DataFrame: Returns pandas DataFrame with contents of file.
    """
    data_dir = os.path.join(path)
    
    data = []
    for id, level in enumerate(levels):
        for file in os.listdir(os.path.join(data_dir, level)):
            data.append(['{}/{}'.format(level, file), level])

    df = pd.DataFrame(data, columns=['image_file', 'label'])
    df['label'] = df['label'].map(label_dict)
    df['path'] = path + '/' + df['image_file']

    return df

def img_data_array(DataFrame, image_size):
    """[summary]

    Args:
        DataFrame ([type]): [description]
        image_size (tuple):  Image resolution in pixels e.g. (128x128)

    Returns:
        data (list): Returns list of image data
    """      
    data = []
    
    # Storing images and their labels into a list for further Train Test split
    for i in range(len(DataFrame)):
        image = cv2.imread(DataFrame['path'][i])
        # resize image to a fixed NxN pixels, ignoring aspects ratio
        image = cv2.resize(image, image_size)
        data.append(image)

    data = np.array(data, dtype='float') / 255

    return data

def img_label_list(DataFrame):
    """[summary]

    Args:
        DataFrame ([type]): [description]

    Returns:
        labels (list): Returns list of image labels
    """      
    labels = []
    
    # Storing images and their labels into a list for further Train Test split
    for i in range(len(DataFrame)):
        label = DataFrame['label'][i]
        labels.append(label)

    return labels