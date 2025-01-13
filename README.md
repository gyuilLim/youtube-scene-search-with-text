# Scene search with text

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gyuilLim/youtube_scene_search/blob/main/text_search_main.ipynb)

This repository was created to find scenes that you waant auotomatically in youtube video.

I provide automation tool to find specific scenes with your text.

## Environment(conda)

Deep learning models are used in this tool.

 Models : [CLIP](https://github.com/openai/CLIP), [BLIP-2](https://github.com/salesforce/LAVIS/tree/main/projects/blip2)

 So I recommend you to install the following command, for setting an environment.(Also You can run in Colab)


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

CLI requires 5 aurguments.

* youtube video(str) : video that you want to find sepecific scenes.
* text(str) : text that you want to search with in youtube video.
* model(str) : CLIP or BLIP.
* kfe(bool) : kfe means 'key frame extraction'. you can choose whether to use it or not.
* download(bool) : whether to download youtube video.

So, you can install as CLI like this :

```bash
$ python text_search_main.py \
--url 'https://www.youtube.com/watch?v=82C19hXaloc' \
--text "A man standing while holding a book" \
--model "clip" \
--kfe False \
--download True
```

Return value is the youtube link where the scene is played.

```bash
https://www.youtube.com/watch?v=82C19hXaloc&t=4
```
## Result

![image](https://github.com/gyuilLim/youtube_scene_text_search/assets/50009192/c040b52d-4c5a-4684-98d6-6e646c91a76a)

Scene that is matched with input text **"A man standing while holding a book"**


## Recommended specifications

||CLIP|BLIP-2|
|---|---|---|
|GPU memory|4.5GB|12GB|

You can run this tool in the Colab T4 (15GB) environment.
