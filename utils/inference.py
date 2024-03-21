import clip
from tqdm import tqdm
from utils.textSimilarity import text_similarity

def inference(model_name, text, model, dataloader, device) :
    if model_name == "clip" :
        logits = []
        text = clip.tokenize(['a baby with her mother']).to(device)
        for data in tqdm(dataloader) :
            data = data.to(device)
            image_features = model.encode_image(data)
            text_features = model.encode_text(text)
            
            logits_per_image, logits_per_text = model(data, text)
            logits.append(logits_per_image)

            flat = [item.item() for logit in logits for item in logit]
            max_index = flat.index(max(flat))


    elif model_name == "blip" :
        msg_list = []
        for data in tqdm(dataloader) :
            data = data.to(device)
            msg = model.generate({"image": data})
            msg_list.append(msg)
        
        flat_msg_list = [msg for sublist in msg_list for msg in sublist]
        max_index = text_similarity(flat_msg_list, 'a baby with her mother')


    return max_index
