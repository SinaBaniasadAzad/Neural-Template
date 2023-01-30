import torch
import torch.nn as nn

## config debugger
debug_base_folder = r'../debug'

#### setting for DGCNN
emb_dims = 1024
k = 20
dropout = 0.5
output_channels = 256

## setting for image encoder
img_ef_dim = 64

#### setting for MLP
decoder_input_embbeding_size = 128
decoder_input_size = 3
decoder_layers = [1024, 1024, 1024, 512, 256, 128]
decoder_activation = nn.LeakyReLU(negative_slope=0.02)
decoder_last_activation = lambda x: torch.clamp(x, 0, 1)

### setting for flow Decoder
flow_layers_dim = [256, 256, 256]
flow_input_dim = 3
flow_layer_type = 'concatsquash'
flow_activation = torch.nn.Softplus()
flow_trainable_T = True
flow_T = 1.0
flow_use_linear = True
atol = 1e-5
rtol = 1e-5
initial_mean = 0.5
ODE_networkt_type = 'ODE_ResNet'
flow_resnet_use_tanh = False
flow_resnet_use_softplus = False
flow_field_use_embedding_dim = True
flow_use_bsp_field = True
flow_use_split_dim = True
flow_use_mutilple_layers = True
flows_layers_cnt = 1
bsp_encoder_layers = [256, 512, 1024]
bsp_p_dim = 4096
bsp_c_dim = 32
bsp_phase = 1
bsp_thershold = 0.01



#### Training
data_worker = 6
coordinate_max_len = 500000
encoder_type = '3DCNN'
decoder_type = 'Flow'
network_type = 'AutoEncoder'
lr = 5e-5
beta1 = 0.5
clamp_dist = 0.1
network_resume_path = None
optimizer_resume_path = None
data_type = 'IMNET'
data_folder = 'home'
data_path = r'./data/all_vox256_img/all_vox256_img_train.hdf5'
sample_voxel_size = 16
num_sample_per_model = 16392
load_ram = False
batch_size = 32
loss_fn = nn.MSELoss() # nn.MSELoss
training_epochs = 300
saving_intervals = 5
exp_idx = 200
starting_epoch = 0
starting_phase = 2
special_symbol = ''
testing_indices = [6, 18, 22, 25, 34, 43, 53, 57, 59, 77, 107, 113, 116, 127, 145, 208]
half_batch_size_when_phase_2 = False
use_testing = True
testing_interval = 1
auto_encoder_config_path = None
auto_encoder_resume_path = None
