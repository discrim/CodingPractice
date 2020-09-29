import torch
import torchvision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt

A = [[1, 1], [1, 1]]
B = torch.rand((3, 4))

##plt.imshow(B)
##plt.show()


outh, outw = 2, 2
transform = transforms.Compose([
    transforms.RandomCrop((outh, outw))
    ])

out = transform(B)
plt.imshow(out)
plt.show()
