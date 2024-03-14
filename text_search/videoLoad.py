import matplotlib.pyplot as plt
import cv2, pafy
import re

def extract_video_id(youtube_link):
    index = youtube_link.find('?')

    if index != -1 :
        youtube_link = youtube_link[:index]

    return youtube_link

def video_load_from_url(url) :
    url = extract_video_id(url)
    video = pafy.new(url)

    best = video.getbest(preftype = 'mp4')

    cap = cv2.VideoCapture(best.url)
    
    return cap, url