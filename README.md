# Youtube Scene Text Search

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gyuilLim/youtube_scene_search/blob/main/text_search_main.ipynb)

This repository was created to find scenes auotomatically that you want in youtube video.

I provied automation tool to find specific scene with your text.

## Environment(conda)

Various deep learning models are used in this tool.

 Models : [CLIP](https://github.com/openai/CLIP), [BLIP-2](https://github.com/salesforce/LAVIS/tree/main/projects/blip2)

 So I recommend you to install the following command, for setting an environment.


## Usage

1. Clone repo from here https://github.com/gyuilLim/youtube_scene_search
2. Change the directory to where you have cloned repo.

```bash
cd youtube_scene_search
```
3. Create conda virtual environment.
```bash
conda create -n youtube_scene_search python=3.8
conda install --file requirements.txt
```

4. Install the command.

I give you CLI for making it easy to execute.

CLI requires 4 aurguments.

* youtube video(str) : video that you want to find sepecific scenes.
* text(str) : text that you want to search with in youtube video.
* model(str) : CLIP or BLIP.
* kfe(bool) : kfe means 'key frame extraction'. you can choose whether to use it or not.
* download(bool) : whether to download youtube video.

So, you can install CLI like :

```bash
$ python text_search_main.py \
--url 'https://youtu.be/wbM4HS1sbXM?si=g8A58del3e_5Ljpo' \
--text "a baby with her mother" \
--model "clip" \
--kfe False \
--download True
```

Return value is the youtube link where the scene is played.

```bash
https://youtu.be/wbM4HS1sbXM?t=1
```
## Result

![image](https://github.com/gyuilLim/youtube_scene_search/assets/50009192/b58ffbee-d5d8-495a-a003-8784a76978b3)

Scene that is mached with input text **"a baby with her mother"**


## Recommended specifications

||CLIP|BLIP-2|
|---|---|---|
|GPU memory|4.5GB|12GB|

You can run this tool in the Colab T4 (15GB) environment.
