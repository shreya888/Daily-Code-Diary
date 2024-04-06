'''
Common methods of defining a tensor
'''
import torch

x = torch.empty(2, 3)  # Accesses random memory location (cannot be controlled)
x = torch.rand(2, 3)  # Can be controlled by seed
x = torch.zeros(2, 3)  # Initialize all values to 0s
x = torch.ones(2, 3)  # Initialize elements to 1s

# Check type of tensor using dtype
print(x, x.dtype)  # By default, it is float32 type

# But can define the dtype when initializing
x = torch.ones(2,3, dtype=torch.int)
print(x)

# Get size of tensor
print(x.size())

# Define your own tensor values
x = torch.tensor([[2.5, 0.3], [4.9, 7.5]])
print(x)
