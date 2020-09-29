import torch

def myfunc(device):
    print(device)

if __name__ == '__main__':
    device = torch.device('cpu')
    print(type(device), device)

    device = str(device)
    print(type(device), device)

    device = 'cpu'
    print(type(device), device)

    myfunc('cpu')
