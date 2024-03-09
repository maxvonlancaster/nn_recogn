from pymongo import MongoClient

from bson.binary import Binary
import io
from PIL import Image

import os
from dotenv import load_dotenv

con_str = os.getenv('CONN_STR')

def save_image(image, file_name):
    client = MongoClient(con_str)
    db = client['image_app']
    collection = db['images']
    binary_data = Binary(image)

    image_doc = {'image': binary_data, 'file_name': file_name}
    result = collection.insert_one(image_doc)
    return 1