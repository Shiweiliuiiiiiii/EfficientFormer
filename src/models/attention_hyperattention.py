from torch import nn

from models.hyperattention.hyper_attn import HyperAttention

class HyperAttention(nn.Module):
    """
    The HyperAttention block as given in https://arxiv.org/abs/2310.05869
    """
    def __init__(self, config, query, key, value):
        super().__init__()

        self.num_hash = config['']
        self.input_dim = config['']


        

        self.device = config['device'] if 'device' in config else 'cuda' # Fix device use
        