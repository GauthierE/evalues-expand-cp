'''LeNet in PyTorch (adapted for 62 classes).'''
import torch.nn as nn
import torch.nn.functional as F
    
class LeNet62(nn.Module):
    def __init__(self):
        super(LeNet62, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)  # MNIST has 1 channel (grayscale)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1   = nn.Linear(16 * 4 * 4, 120)  # adjusted for MNIST input size
        self.fc2   = nn.Linear(120, 84)
        self.fc3   = nn.Linear(84, 62)

    def forward(self, x):
        out = F.relu(self.conv1(x))
        out = F.max_pool2d(out, 2)
        out = F.relu(self.conv2(out))
        out = F.max_pool2d(out, 2)
        out = out.view(out.size(0), -1)  # flatten
        out = F.relu(self.fc1(out))
        out = F.relu(self.fc2(out))
        out = self.fc3(out)
        return out