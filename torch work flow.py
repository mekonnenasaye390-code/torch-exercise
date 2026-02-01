import torch
from matplotlib import pyplot as plt
from torch import nn
weight=0.7
bias=0.3
start=0
end=1
step=0.02
x=torch.arange(start,end,step)
y=weight*x + bias
print(x,y,len(x))
train_split=int(0.8 * len(x))
x_train=x[:train_split]
y_train=y[:train_split]
x_test=x[train_split:]
y_test=y[train_split:]
print(x_train,y_train,x_test,y_test,len(x_train),len(x_test))
## visiualize of the graph
def plot_prediction(train_data=x_train,train_label=y_train,test_data=x_test,test_label=y_test):
 plt.figure(figsize=(10,10))
plt.scatter(x_train,y_train,color='blue',label='train',s=8)
plt.scatter(x_train,y_train,color='red',label='train',s=2)
plt.legend(prop={'size':10})
plt.show()
