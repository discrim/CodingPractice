import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class Model(nn.Module):
    def __init__(self, batch_size, sequence_length, input_size, hidden_size, num_layers, num_classes, device):
        super(Model,self).__init__()
        self.batch_size = batch_size
        self.sequence_length = sequence_length
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.num_classes = num_classes
        self.device = device
        self.rnn=nn.RNN(input_size = input_size,hidden_size=hidden_size,batch_first=True)
        
    def forward(self,x,hidden):
        #input x 를 (batch_size,sequence_length,input_size)로 reshape함
        #just for make sure이라고 하심.
        x=x.view(self.batch_size, self.sequence_length, self.input_size)
        
        #Propagate input through RNN
        #Input:(batch,seq_len,input_size)
        print("x.shape: ", x.shape)
        print("hidden.shape: ", hidden.shape)
        out,hidden = self.rnn(x,hidden)
        print("out.shape: ", out.shape)
        print("hidden.shape: ", hidden.shape)
        
        #for make sure, output이 N * 5 shape을 따르게 하기 위해서
        out = out.view(-1, self.num_classes)
        return hidden,out
    
    def init_hidden(self):
        #initialize hidden and cell states
        return torch.zeros(self.num_layers, self.batch_size, self.hidden_size).to(self.device)


def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    num_classes = 5
    input_size = 5 # one-hot size
    hidden_size = 5 #output from the cell. 바로 결과 예측을 위해서 5로 설정
    batch_size = 1 # sentence의 개수 (단어개수)
    sequence_length = 6 # 이번에는 한번에 하나씩 해본다
    num_layers = 1 # one layer rnn이다. (아직 안 다룬 개념)


    # Data
    idx2char = ['h','i','e','l','o']
    x_data = [0,1,0,2,3,3] #hihell
    one_hot_lookup = [[1,0,0,0,0], #h
                      [0,1,0,0,0], #i
                      [0,0,1,0,0], #e
                      [0,0,0,1,0], #l
                      [0,0,0,0,1]] #o
    x_one_hot = [one_hot_lookup[x] for x in x_data]
    y_data = [1,0,2,3,3,4] #ihello


    inputs = torch.Tensor(x_one_hot)
    labels = torch.LongTensor(y_data)
    
    
    model = Model(batch_size, sequence_length, input_size, hidden_size, num_layers, num_classes, device).to(device)
    criterion = nn.CrossEntropyLoss() #1
    optimizer = optim.Adam(model.parameters(),lr = 0.1)
    
    for epoch in range(5):
        optimizer.zero_grad()
        loss = 0
        hidden = model.init_hidden() #2

        #print("predicted string : ",end="")
        
        """
        for input,label in zip(inputs,labels): #3
            input = input.to(device)
            label = label.to(device)
            label = label.view(1)
            
            print("Input: {}, Label: {}".format(input, label))
            
            #hidden = model.init_hidden() #2
            hidden,output = model(input,hidden)
            #print(hidden)
            #print(output)
            
            val,idx = output.max(1)
            #print(idx2char[idx.data[0]],end="")
            loss += criterion(output,label)
            
            #optimizer.zero_grad()
            #loss = criterion(output, label)            
            #loss.backward()
            #optimizer.step()
        """
        
        inputs = inputs.to(device)
        labels = labels.to(device)
        
        hidden, outputs = model(inputs, hidden)
        loss = criterion(outputs, labels)
        
        _, idx = outputs.max(1)
        result_str = ''.join([idx2char[c] for c in idx.squeeze()])

        print(", epoch: %d, loss: %1.3f" % (epoch+1,loss))
        print("Predicted string: {}\n\n".format(result_str))
        loss.backward()
        optimizer.step()
        
        #print(model.rnn.weight_ih_l0.grad)
        #print(model.rnn.weight_hh_l0.grad)


if __name__ == "__main__":
    main()