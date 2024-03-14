from videoLoad import video_load_from_url
from frameMethod import key_frame_detection
from dataset import custom_dataset
from textSimilarity import text_similarity
from model import load_model

import numpy as np
from torch.utils.data import DataLoader
from lavis.models import load_model_and_preprocess
from tqdm import tqdm
import torch
import clip
import matplotlib.pyplot as plt
import argparse

import json
import requests

# input value
parser = argparse.ArgumentParser(
    description='Input Text and what model you wanna use.')
train_set = parser.add_mutually_exclusive_group()
parser.add_argument('--text', default='',
                    type=str, help='Input your text.')
parser.add_argument('--model', default="clip", choices=['clip', 'blip'],
                    type=str, help='clip or blip')
parser.add_argument('--kfe', default=False, choices=[True, False],
                    type=bool, help='True or False')
args = parser.parse_args()



device = "cuda" if torch.cuda.is_available() else "cpu"

# video load
print('video load ... ')
cap, url = video_load_from_url('https://youtu.be/wbM4HS1sbXM?si=g8A58del3e_5Ljpo')
# cap = video_load_from_url('https://www.youtube.com/watch?v=fiGSDywrX1Y')
print('video load complete ')

# KFD
print('key frame detection ... ')
frame_list, time_line = key_frame_detection(cap, args.kfe)
print('key frame detection complete ')


# dataloader
dataset = custom_dataset(frame_list, args.model)
dataloader = DataLoader(dataset, batch_size=32)

# load model
print('model load ...')
model = load_model(args.model, device)
if args.model == "blip" :
    model.float()
print('model load complete')

# inference

model.eval()
if args.model == "blip" :
    print('infrence loading ... ')
    msg_list = []
    for data in tqdm(dataloader) :
        data = data.to(device)
        msg = model.generate({"image": data})
        msg_list.append(msg)
        
    
    flat_msg_list = [msg for sublist in msg_list for msg in sublist]

    max_index = text_similarity(flat_msg_list, args.text)

    print(max_index)

    print('infrence complete ')

elif args.model == "clip" :
    print('infrence loading ... ')
    logits = []
    text = clip.tokenize([args.text]).to(device)
    for data in tqdm(dataloader) :
        data = data.to(device)
        image_features = model.encode_image(data)
        text_features = model.encode_text(text)
        
        logits_per_image, logits_per_text = model(data, text)
        logits.append(logits_per_image)

        flat = [item.item() for logit in logits for item in logit]
        max_index = flat.index(max(flat))
        
    print('infrence complete ')

print(url + '?t=' + str(int(time_line[max_index])))
plt.imshow(frame_list[max_index])

