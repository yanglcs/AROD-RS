import torch.backends.cudnn as cudnn
from data import *
from data import VOC_CLASSES as voc_labelmap
from data import COCO_CLASSES as coco_labelmap
from data import hrsc_CLASSES as hrsc_labelmap


from models import build_ssd, build_robust_ssd

import sys
import os
import time
import argparse
import numpy as np
import pickle
from utils.utils import get_logger, Empty, Timer
import cv2
from utils.cfgParser import cfgParser

from attack import *
from robust import *


def save_images(images, img_list, idx, output_dir):
    """Saves images to the output directory.
        Args:
          images: tensor with minibatch of images
          img_list: list of filenames without path
            If number of file names in this list less than number of images in
            the minibatch then only first len(filenames) images will be saved.
          output_dir: directory where to save images
    """
    for i, sample_idx in enumerate(idx.numpy()):
        # Images for inception classifier are normalized to be in [-1, 1] interval,
        # so rescale them back to [0, 1].
        filename = img_list[sample_idx]
        cur_images = (images[i, :, :, :] * 255).astype(np.uint8)
        with open(os.path.join(output_dir, filename), 'wb') as f:
            cv2.imsave(f, cur_images.transpose(1, 2, 0), format='png')
