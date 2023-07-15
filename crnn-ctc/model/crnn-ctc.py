import math
import torch
from torch import nn
import torch.nn.functional as F
from collections import OrderedDict

class ConvNN(nn.Module):
    def __init__(self, config):
        super().__init__()
        
        self.conv = nn.Conv2d(config['in_channel'], config['out_channel'], kernel_size=config['kernel_size'], stride = config['stride'], padding=config['padding'])
        self.batch_norm = nn.BatchNorm2d(config['out_channel'])
        self.activation = config['activation'](inplace=True)
        self.dropout = nn.Dropout(p=config['dropout'])
        
    def forward(self, data):
        x = self.conv(data)
        x = self.batch_norm(x)
        x = self.activation(x)
        x = self.dropout(x)
        
        return x
        
class BatchRNN(nn.Module):
    def __init__(self, config):
        super().__init__()
        
        self.input_size = config['input_size']
        self.hidden_size = config['hidden_size']
        self.batch_norm = nn.BatchNorm2d(config['input_size'])
        self.rnn = config['rnn_type'](input_size=config['input_size'], hidden_size=config['hidden_size'], bidirectional=config['bidirectional'], bias=False)
        self.dropout = nn.Dropout(p=config['dropout'])
        
    def forward(self, data):
        x = data.transpose(-1, -2)
        x = self.batch_norm(x)
        x = x.transpose(-1, -2)
        x, _ = self.rnn(x)
        x = self.dropout(x)
        
        return x
    
class RCNN(nn.Module):
    def __init__(self, config):
        super().__init__()
        
        self.config = config
        
        self.cnn_param = config['cnn_param']
        self.rnn_param = config['rnn_param']
        
        # cnn layer
        cnns = []
        cnn_layers = config['cnn_param']['layers']
        rnn_input_size = config['rnn_param']["rnn_input_size"]
        
        for n in range(len(cnn_layers)):
            cnn_config = {
                'in_channel': config['cnn_param']['channel'][n][0],
                'out_channel': config['cnn_param']['channel'][n][1],
                'kernel_size': config['cnn_param']['kernel_size'],
                'stride': config['cnn_param']['stride'],
                'padding': config['cnn_param']['padding']
            }
            
            cnn = ConvNN(config=cnn_config)
            cnns.append('%d' % n, cnn) 
        
            try:
                rnn_input_size = int(math.floor((rnn_input_size+2*cnn_config['padding'][1]-cnn_config['kernel_size'][1])/cnn_config['stride'][1])+1)
            except:
                rnn_input_size = rnn_input_size
            
        self.conv = nn.Sequential(OrderedDict(cnns))
        rnn_input_size *= cnn_config['out_channel']
        
        rnns = []
        rnn_config = {
            'hidden_size': config['rnn_param']['hidden_size'],
            'rnn_type': config['rnn_param']['rnn_type'],
            'layers': config['rnn_param']['layers'],
            'bidirectional': config['rnn_param']['bidirectional']
        }
        
        
            
            
        
