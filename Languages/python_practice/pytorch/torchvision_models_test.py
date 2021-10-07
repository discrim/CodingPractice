"""
The purpose of this file is:
- to test loading torchvision.models.vgg19() from torchvision
- to test loading pretrained weights of them

Try using various versions of pytorch.
Working:
    pytorch 1.8.1 + torchvision 0.2.1
    pytorch 1.6.0 + torchvision 0.7.0
    pytorch 1.4.0 + torchvision 0.2.2
Not working:
    pytorch 1.2.0 + torchvision 0.7.0
"""

import torch
import torchvision.models as models

def main():
    model = models.vgg19(pretrained=True).eval()


if __name__ == "__main__":
    main()