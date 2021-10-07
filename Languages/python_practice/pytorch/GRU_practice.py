import torch
import torch.nn as nn
import torch.optim as optim

if 0:
    input_size = 10
    hidden_size = 20
    num_layers = 2
    batch = 3
    seq_len = 5

    rnn = nn.GRU(input_size=10, hidden_size=20, num_layers=2)
    feat = torch.randn(5, 3, 10) # seq_len x batch x input_size
    h0 = torch.randn(2, 3, 20) # num_layers * num_directions(1) x batch x hidden_size
    out, hn = rnn(feat, h0)
    # out (last layer of GRU): seq_len x batch x num_directions(1) * hidden_size
    # hn: num_layers * num_directions(1) x batch x hidden_size

class GRU(nn.Module):
    def __init__(self, batch_size, seq_len, input_size, hidden_size, num_layers, num_classes, device):
        super(GRU, self).__init__()
        
        self.batch_size = batch_size
        self.seq_len = seq_len
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.num_classes = num_classes
        self.device = device
        
        self.model = nn.GRU(input_size=input_size, hidden_size=hidden_size,
                            num_layers=num_layers)
    
    def forward(self, input, hid):
        input = input.view(self.batch_size, self.seq_len, self.input_size)
        out = self.model(input, hid)
        out = out.view(-1, self.num_classes)
        return out, hid
    
    def init_hidden(self):
        return torch.zeros(self.num_layers, self.batch_size, self.hidden_size).to(self.device)

def main():
    """ From 'hihell', predict 'ihello'.
    Mapping:
        'e' = [1, 0, 0, 0, 0]
        'h' = [0, 1, 0, 0, 0]
        'i' = [0, 0, 1, 0, 0]
        'l' = [0, 0, 0, 1, 0]
        'o' = [0, 0, 0, 0, 1]
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    batch_size = 1
    seq_len = 1
    input_size = 5
    hidden_size = 5
    num_layers = 1
    num_classes = 5
    
    idx2char = ['e', 'h', 'i', 'l', 'o']
    x_data = [1, 2, 1, 0, 3, 3]
    one_hot_lookup = [[1, 0, 0, 0, 0],
                      [0, 1, 0, 0, 0],
                      [0, 0, 1, 0, 0],
                      [0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 1]]
    x_one_hot = [one_hot_lookup[x] for x in x_data]
    y_data = [2, 1, 0, 3, 3, 4]
    
    inputs = torch.tensor(x_one_hot)
    labels = torch.tensor(y_data)
    
    model = GRU(batch_size, seq_len, input_size, hidden_size, num_layers, num_classes, device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.1)
    
    for epoch in range(100):
        optimizer.zero_grad()
        hid = model.init_hidden()
        loss = 0
        
        print("Prediction: ", end="")
        
        for input, label in zip(inputs, labels):
            inputs = inputs.to(device)
            labels = labels.to(device).view(-1, 1)
            out, hid = model.forward(input, hid)
            val, idx = out.max(1)
            print(idx2char[idx.data[0]], end="")
            loss += criterion(out, label)
        
        print(", epoch {}, loss: {:1.3f}".format(epoch + 1, loss.data[0]))
        loss.backward()
        optimizer.step()
    

if __name__ == "__main__":
    main()