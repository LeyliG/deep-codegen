import torch.nn as nn
import torch.nn.functional as F
# Add the parent directory to the Python path
import sys
import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pytorch_apis import linear, gspmmv

class GCNLayer(nn.Module):
    def __init__(self, in_feats, out_feats, graph, device):
        super(GCNLayer, self).__init__()
        self.weight = nn.Parameter(th.randn(in_feats, out_feats))
        self.graph = graph
        self.device = device

    def forward(self, inputs):
        # Perform feature transformation using a linear layer
        h = linear(inputs, self.weight, inputs.shape[0], self.weight.shape[1], self.device)
        
        # Graph propagation using SpMMv
        h = gspmmv(self.graph, h, h.shape[0], h.shape[1], False, False, self.device)
        return h

class TwoLayerGCN(nn.Module):
    def __init__(self, in_feats, hidden_feats, out_feats, graph, device):
        super(TwoLayerGCN, self).__init__()
        self.layer1 = GCNLayer(in_feats, hidden_feats, graph, device)
        self.layer2 = GCNLayer(hidden_feats, out_feats, graph, device)

    def forward(self, inputs):
        # First layer with ReLU activation
        h = self.layer1(inputs)
        h = F.relu(h)
        
        # Second layer (output layer)
        h = self.layer2(h)
        return h