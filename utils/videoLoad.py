import matplotlib.pyplot as plt
import cv2, pafy
from pytube import YouTube
import re

def extract_video_id(youtube_link):
    index = youtube_link.find('?')

    if index != -1 :
        youtube_link = youtube_link[:index]

    return youtube_link

def video_load_from_url(url, download = False) :
    
    if download == True :
        streams = YouTube(url).streams.filter(adaptive=True, subtype="mp4", resolution="360p", only_video=True)
        streams[0].download(filename="video.mp4")
        url = extract_video_id(url)
        cap = cv2.VideoCapture('./video.mp4')


    elif download == False :
        url = extract_video_id(url)
        video = pafy.new(url)
        best = video.getbest(preftype = 'mp4')
        cap = cv2.VideoCapture(best.url)
    
    return cap, url