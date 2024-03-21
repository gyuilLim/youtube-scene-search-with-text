import os
import cv2
import csv
import numpy as np
import time
import peakutils
import matplotlib.pyplot as plt
from PIL import Image
from tqdm import tqdm
# from scenedetect import detect, ContentDetector


def scale(img, xScale, yScale):
    res = cv2.resize(img, None, fx=xScale, fy=yScale, interpolation=cv2.INTER_AREA)
    return res


def convert_frame_to_grayscale(frame):
    grayframe = None
    gray = None
    if frame is not None:
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = scale(gray, 1, 1)
        grayframe = scale(gray, 1, 1)
        gray = cv2.GaussianBlur(gray, (9, 9), 0.0)
    return grayframe, gray


def key_frame_detection(cap, kfe=False, Thres=0.3, plotMetrics=False, verbose=False):

    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    spf = 1 / fps

    if kfe == False :
        frame_list = []
        time_spans = []
        for i in tqdm(range(0, length)) :
            ret, frame = cap.read()

            if i % 12 == 0 :
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_list.append(frame)
                time_spans.append(spf * i)

        return frame_list, time_spans
  
    if (cap.isOpened()== False):
        print("Error opening video file")

    lstfrm = []
    lstdiffMag = []
    timeSpans = []
    images = []
    full_color = []
    lastFrame = None
    
    # Read until video is completed
    for i in tqdm(range(length)):
        ret, frame = cap.read()
        grayframe, blur_gray = convert_frame_to_grayscale(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        frame_number = cap.get(cv2.CAP_PROP_POS_FRAMES) - 1
        lstfrm.append(frame_number)
        images.append(grayframe)
        full_color.append(frame)
        if frame_number == 0:
            lastFrame = blur_gray

        diff = cv2.subtract(blur_gray, lastFrame)
        diffMag = cv2.countNonZero(diff)
        lstdiffMag.append(diffMag)
        time_Span = i * spf
        timeSpans.append(time_Span)
        lastFrame = blur_gray

    cap.release()
    y = np.array(lstdiffMag)
    base = peakutils.baseline(y, 2)
    indices = peakutils.indexes(y-base, Thres, min_dist=1)

    return_keyframe = []
    return_frame_times = []

    for x in indices:
        return_keyframe.append(full_color[x])
        return_frame_times.append(timeSpans[x])  # 프레임 시간 추가

    return return_keyframe, return_frame_times


# main method 2 - SCD

# def scene_change_detector(video_path):
#     scene_list = detect(video_path, ContentDetector())
#     return scene_list