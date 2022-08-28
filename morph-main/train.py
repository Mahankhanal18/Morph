from morph import Morph
import torch

model = Morph(
    models_root='./pretrained',
    dtype=torch.float32,
    is_mega=True,
    is_reusable=True
)
