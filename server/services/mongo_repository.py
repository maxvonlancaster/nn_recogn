from pymongo import MongoClient

from bson.binary import Binary
import io
from PIL import Image

from bson.json_util import dumps
from bson.json_util import loads

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
    client.close()
    return 1

def get_images():
    image_list = []

    client = MongoClient(con_str)
    db = client['image_app']
    collection = db['images']
    for document in collection.find({}, {"image": 1}):
        image_list.append(document.get("image"))

    return image_list