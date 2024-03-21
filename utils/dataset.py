from torchvision import transforms
from torchvision.transforms.functional import InterpolationMode
import torch
from PIL import Image


class custom_dataset(torch.utils.data.Dataset): 
    def __init__(self, frame_list, model):
        self.frame_list = frame_list
        self.model = model
        self.pil_image_list = [self.frame_to_PIL(frame) for frame in frame_list]
        
        self.image_size = 224

        self.mean = (0.48145466, 0.4578275, 0.40821073)
        self.std = (0.26862954, 0.26130258, 0.27577711)
      
        self.transform = transforms.Compose(
                [
                    transforms.Resize(
                        (self.image_size, self.image_size), interpolation=InterpolationMode.BICUBIC
                    ),
                    transforms.ToTensor(),
                    transforms.Normalize(self.mean, self.std),
                ]
            )

    def __len__(self):
        return len(self.pil_image_list)

    def __getitem__(self, idx):
        return self.transform(self.pil_image_list[idx])

    def frame_to_PIL(self, frame):
        pil_image = Image.fromarray(frame)
        return pil_image