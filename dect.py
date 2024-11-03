import torch
import torch.nn as nn

# 定义卷积神经网络（CNN）模型
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.conv3 = nn.Conv2d(64, 64, 3, 1)
        self.fc1 = nn.Linear(64 * 3 * 3, 64)
        self.fc2 = nn.Linear(64, 10)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.max_pool2d(x, 2, 2)
        x = torch.relu(self.conv2(x))
        x = torch.max_pool2d(x, 2, 2)
        x = torch.relu(self.conv3(x))
        x = x.view(-1, 64 * 3 * 3)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return torch.log_softmax(x, dim=1)

# 创建模型实例并移动到设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = Net().to(device)

# 加载训练好的模型状态字典
model.load_state_dict(torch.load('mnist_cnn.pth', map_location=device, weights_only=True))
model.eval()

# 根据输入张量进行推理预测
def make_prediction(input_tensor):
    with torch.no_grad():
        input_tensor = input_tensor.to(device)
        output = model(input_tensor)
        probabilities = torch.exp(output)
        predicted_class = torch.argmax(probabilities, dim=1)
    return predicted_class.item()

