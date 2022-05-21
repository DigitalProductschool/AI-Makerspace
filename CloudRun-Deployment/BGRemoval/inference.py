import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms

from src.models.modnet import MODNet


class BGRemoval:
    def __init__(self):
        self.ref_size = 512

        # create MODNet and load the pre-trained ckpt
        self.model = MODNet(backbone_pretrained=False)
        self.model = nn.DataParallel(self.model)

        ckpt_path = "./pretrained/modnet_photographic_portrait_matting.ckpt"
        weights = torch.load(ckpt_path, map_location=torch.device('cpu'))

        self.model.load_state_dict(weights)
        self.model.eval()

        self.image, self.im, self.mask, self.im_h, self.im_w = None, None, None, None, None

    def load_image(self, image):
        self.image = image

        # define image to tensor transform
        im_transform = transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
        # convert image to PyTorch tensor
        self.im = im_transform(self.image)

        # add mini-batch dim
        self.im = self.im[None, :, :, :]

        # resize image for input
        im_b, im_c, self.im_h, self.im_w = self.im.shape
        if max(self.im_h, self.im_w) < self.ref_size or min(self.im_h, self.im_w) > self.ref_size:
            if self.im_w >= self.im_h:
                im_rh = self.ref_size
                im_rw = int(self.im_w / self.im_h * self.ref_size)
            elif self.im_w < self.im_h:
                im_rw = self.ref_size
                im_rh = int(self.im_h / self.im_w * self.ref_size)
        else:
            im_rh = self.im_h
            im_rw = self.im_w

        im_rw = im_rw - im_rw % 32
        im_rh = im_rh - im_rh % 32

        self.im = F.interpolate(self.im, size=(im_rh, im_rw), mode='area')

    def run_model(self):
        # inference
        _, _, self.mask = self.model(self.im, True)

        # resize and save matte
        self.mask = F.interpolate(self.mask, size=(self.im_h, self.im_w), mode='area')
        self.mask = self.mask[0][0].data.cpu().numpy()

    def remove_background(self, r, g, b, a):
        self.mask = np.repeat(self.mask[:, :, None], 4, axis=2)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2RGBA)
        out = self.image * self.mask + np.full(self.mask.shape, [b, g, r, a]) * (1 - self.mask)
        return out
