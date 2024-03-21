from text_search.videoLoad import video_load_from_url
from text_search.frameMethod import key_frame_detection
from text_search.dataset import custom_dataset
from text_search.model import load_model
from text_search.inference import inference

from torch.utils.data import DataLoader
from tqdm import tqdm
import torch
import matplotlib.pyplot as plt
import argparse

# input argument
parser = argparse.ArgumentParser(
    description='Input Text and what model you wanna use.')
train_set = parser.add_mutually_exclusive_group()
parser.add_argument('--url', default='',
                    type=str, help='Youtube video address')
parser.add_argument('--text', default='',
                    type=str, help='Input your text.')
parser.add_argument('--model', default="clip", choices=['clip', 'blip'],
                    type=str, help='clip or blip')
parser.add_argument('--kfe', default=False, choices=[True, False],
                    type=bool, help='True or False')
parser.add_argument('--download', default=True, choices=[True, False],
                    type=bool, help='True of False')
args = parser.parse_args()



device = "cuda" if torch.cuda.is_available() else "cpu"

# video load
print('video load ... ')
cap, url = video_load_from_url(args.url, args.download)
print('video load complete ')

# KFD
print('key frame extraction ... ')
frame_list, time_line = key_frame_detection(cap, args.kfe)
print('key frame extraction complete ')


# dataloader
dataset = custom_dataset(frame_list, args.model)
dataloader = DataLoader(dataset, batch_size=32)

# load model
print('model load ...')
model = load_model(args.model, device)
print('model load complete')

# inference
print('inference loading ... ')
model.eval()
max_index = inference(args.model, args.text, model, dataloader, device)
print('infrence complete ')

print(url + '?t=' + str(int(time_line[max_index])))
plt.imshow(frame_list[max_index])

