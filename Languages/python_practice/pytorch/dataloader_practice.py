# https://wikidocs.net/55580

import torch
import torch.nn as nn
import torch.nn.functional as F

from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.model = nn.Sequential(
            # 1 x 16 x 16
            nn.Conv2d(1, 64, 3, stride=1, padding=1), nn.LeakyReLU(0.2),
            nn.Conv2d(64, 128, 3, stride=1, padding=1), nn.LeakyReLU(0.2),
            nn.MaxPool2d(2, 2),
            # 128 x 8 x 8
            nn.Conv2d(128, 256, 3, stride=1, padding=1), nn.LeakyReLU(0.2),
            nn.Conv2d(256, 512, 3, stride=1, padding=1), nn.LeakyReLU(0.2),
            nn.MaxPool2d(2, 2),
            # 512 x 4 x 4
            nn.Conv2d(512, 512, 3, stride=1, padding=1), nn.LeakyReLU(0.2),
            nn.Conv2d(512, 512, 3, stride=1, padding=1), nn.LeakyReLU(0.2),
            nn.MaxPool2d(2, 2),
            # 512 x 2 x 2
            nn.AvgPool2d(2)
            )
            # 512 x 1 x 1
        
        self.classifier = nn.Linear(512, 5)
    
    def forward(self, x):
        print(x.size())
        out = self.model(x)
        print(out.size())
        out = out.view(-1, 512)
        print(out.size())
        out = self.classifier(out)
        print(out.size())
        return out

def main():

    torch.manual_seed(23)

    x_train = torch.randint(low=0, high=100, size=(100, 1, 16, 16)).type(torch.FloatTensor)
    y_train = torch.randint(low=0, high=5, size=(100, 1)).type(torch.FloatTensor)

    dataset = TensorDataset(x_train, y_train)

    dataloader = DataLoader(dataset, batch_size=10, shuffle=True)
    
    net = Net()

    optimizer = torch.optim.SGD(net.model.parameters(), lr=1e-5)

    num_epochs = 5

    for epoch in range(1, num_epochs + 1):
        for batch_idx, samples in enumerate(dataloader):
            #print(batch_idx)
            #print(samples)
            x_train, y_train = samples
            
            # Forward
            prediction = net.forward(x_train)
            cost = F.mse_loss(prediction, y_train)
            
            # Backward
            optimizer.zero_grad()
            cost.backward()
            optimizer.step()
            
            print("Epoch {:4d}/{}, Batch {:2d}/{}, Cost {:.6f}".format(
                   epoch, num_epochs, batch_idx + 1, len(dataloader), cost.item()))

if __name__ == "__main__":
    main()