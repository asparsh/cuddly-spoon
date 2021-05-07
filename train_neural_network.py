import torch
import torch.nn as nn

def training_routine(net,train_loader,n_iters,gpu):
    
    optimizer = torch.optim.SGD(net.parameters(),lr=0.0001,momentum=0.8)
    criterion = nn.BCELoss()
    loss_list = []
    index_list = []
    
    for j in range(n_iters):  
        running_loss = 0
        full_accuracy = 0
        
        for index, (data, labels) in enumerate(train_loader):
            
            net.train()
            optimizer.zero_grad()
            
            if gpu:
                data,labels = data.float().cuda(),labels.long().cuda()
                net = net.cuda()
            else:
                data,labels = data.float(),labels.float()
        
            train_output = net(data)
            train_loss = criterion(train_output,labels.unsqueeze(1))
            running_loss = running_loss + train_loss.cpu().detach().numpy()
            train_loss.backward()
            optimizer.step()
            
            net.eval()
            train_prediction = train_output.cpu().detach().argmax(dim=1)
            train_accuracy = (train_prediction.numpy()==labels.cpu().numpy()).mean() 
            full_accuracy += train_accuracy
        
        loss_list.append(float(running_loss)/index+1)
        index_list.append(index+1)
        print("---------------------------------------------------------------------")
        print("Epoch: ", j+1)
        print("---------------------------------------------------------------------")
        print("Running Loss: ", float(running_loss)/index+1)
        
    net = net.cpu()
    return net, loss_list, index_list