from torch.utils.data import Dataset, DataLoader
import torch.nn as nn

class makeDataset(Dataset):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]
    
class makeModel(nn.Module):
    def __init__(self, input_shape, hidden_size, output_size):
        super(makeModel, self).__init__()
        self.linear1 = nn.Linear(input_shape, hidden_size[0])
        self.relu1 = nn.ReLU(hidden_size[0])
        self.linear2 = nn.Linear(hidden_size[0], hidden_size[1])
        self.relu2 = nn.ReLU(hidden_size[1])
        self.linear3 = nn.Linear(hidden_size[1], hidden_size[2])
        self.relu3 = nn.ReLU(hidden_size[2])
        self.linear4 = nn.Linear(hidden_size[2], output_size)
        self.signoid = nn.Sigmoid()
        
    def forward(self, inputs):
        out = self.relu1(self.linear1(inputs))
        out = self.relu2(self.linear2(out))
        out = self.relu3(self.linear3(out))
        out = self.linear4(out)
        out_signoid = self.signoid(out)
        return out_signoid