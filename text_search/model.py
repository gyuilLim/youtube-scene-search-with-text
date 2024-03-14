
from lavis.models import load_model_and_preprocess
import clip

def load_blip(device) :
    model, _, _ = load_model_and_preprocess(
        name="blip2", model_type="pretrain", is_eval=True, device=device
    )

    return model

def load_clip(device) :
    model, _ = clip.load("ViT-B/32", device=device)

    return model

def load_model(name, device) :
    if name == "clip" :
        return load_clip(device)
    
    elif name == "blip" :
        return load_blip(device)