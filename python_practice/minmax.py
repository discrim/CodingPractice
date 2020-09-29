import torch

preds = torch.rand(3, 2)
x, y = preds[:,0], preds[:,1]
print(preds)
print(preds[0, 0])
print(preds[0][0])
print(len(preds))
print(x)
print(y)

Xmin = min(preds[:,0])
print(Xmin)

