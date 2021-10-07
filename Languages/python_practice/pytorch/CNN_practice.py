from glob import glob
import numpy as np
from PIL import Image
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import torchvision
from torchvision import transforms
import matplotlib.pyplot as plt

class CustomDataset(Dataset):
    def __init__(self, main_dir):
        self.main_dir = main_dir
        self.all_imgs = glob(main_dir)
        self.all_labels = torch.randint(low=0, high=5, size=(len(self.all_imgs),))
    
    def __len__(self):
        return len(self.all_imgs)
    
    def __getitem__(self, idx):
        img_path = self.all_imgs[idx]
        img = np.array(Image.open(img_path))* 255 # np array, H x W x C
        img = torch.from_numpy(img).permute(2, 0, 1).float() # torch tensor, C x H x W
        return img, self.all_labels[idx]


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.model = nn.Sequential(
            # 3 x 480 x 640
            nn.Conv2d(3, 64, 3, stride=1, padding=1), nn.LeakyReLU(0.2),
            nn.Conv2d(64, 128, 3, stride=1, padding=1), nn.LeakyReLU(0.2),
            nn.MaxPool2d(2, 2),
            # 128 x 240 x 320
            nn.Conv2d(128, 256, 3, stride=1, padding=1), nn.LeakyReLU(0.2),
            nn.Conv2d(256, 512, 3, stride=1, padding=1), nn.LeakyReLU(0.2),
            nn.MaxPool2d(2, 2),
            # 512 x 120 x 160
            nn.Conv2d(512, 512, 3, stride=1, padding=1), nn.LeakyReLU(0.2),
            nn.Conv2d(512, 512, 3, stride=1, padding=1), nn.LeakyReLU(0.2),
            nn.MaxPool2d(2, 2),
            # 512 x 60 x 80
            nn.AdaptiveAvgPool2d(1)
            )
            # 512 x 1 x 1
        
        self.classifier = nn.Linear(512, 5)
    
    def forward(self, x):
        out = self.model(x)
        out = out.view(-1, 512)
        out = self.classifier(out)
        #out = torch.squeeze(out)
        return out


num_samples = 10
in_channels = 3
H = 480
W = 640

#data = torch.randn(num_samples, num_channels, H, W)

#data = CustomDataset(r"D:\DevPath\optical_flow_results\RAFT\FlowFrames__1MKB3Avehs.mp4\*")
transform = transforms.Compose([transforms.ToTensor(), lambda x:x * 255])
data = torchvision.datasets.ImageFolder(root=r"D:\DevPath\optical_flow_results\RAFT\FlowFrames", transform=transform)
dataloader = DataLoader(data, batch_size=1)

#print("len(data): ", len(data))
#print(data[15][0].shape, data[15][1])
#plt.imshow(data[15].permute(1, 2, 0))
#plt.show()

if 1:
    net = Net()
    
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(net.model.parameters(), lr=1e-5)
    num_epochs = 1
    
    for epoch in range(num_epochs):
        for batch_idx, samples in enumerate(dataloader):
            x, y = samples
            
            optimizer.zero_grad()
            
            # Forward
            prediction = net.forward(x)
            
            # Backward
            loss = criterion(prediction, y)
            loss.backward()
            
            # Optimize
            optimizer.step()
            
            # Print statistics
            print("Epoch {}, Batch {}".format(epoch + 1, batch_idx + 1))
    print("Finished training")


if 0:
    fig, axs = plt.subplots(2, 3)
    axs[0, 0].imshow(data[0, 0, :, :] * 255)
    axs[0, 1].imshow(data[0, 1, :, :] * 255)
    axs[0, 2].imshow(data[0, 2, :, :] * 255)
    axs[1, 0].imshow(result[0, 0, :, :] * 255)
    axs[1, 1].imshow(result[0, 1, :, :] * 255)
    axs[1, 2].imshow(result[0, 2, :, :] * 255)
    plt.show()
