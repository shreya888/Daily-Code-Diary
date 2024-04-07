import torch

# Introduction to Tensor

# Creating Tensor
scalar = torch.tensor(8)  # torch.tensor - Most common class in Pytorch
vector = torch.tensor([7, 1])
MATRIX = torch.tensor([[1, 2], [6, 8]])
# Number of dimensions in tensor variable; Number of sq brackets [] => ndim value
print(f"Dimensions of scalar: {scalar.ndim}, vector: {vector.ndim}, and matrix: {MATRIX.ndim}")
print(f"Shape of matrix: {MATRIX.shape}")

# Randomized creation of tensor
x = torch.empty(2, 3)  # Accesses random memory location (cannot be controlled)
x = torch.rand(2, 3)  # Can be controlled by seed
x = torch.zeros(2, 3)  # Initialize all values to 0s
x = torch.ones(2, 3)  # Initialize elements to 1s

# Get tensor back - use only iff it is scalar or single element reference
print(f"Get scalar tensor back: {scalar.item()}")

# Check type of tensor using dtype
print(f"\nTensor: {x}, and dtype: {x.dtype}")  # By default, it is float32 type

# But can define the dtype when initializing
x = torch.ones(2, 3, dtype=torch.int)
print(f"Tensor of int dtype: {x}")

# Get size of tensor
print(f"Tensor size: {x.size()}")
# .shape is an alias for .size(), and was added to more closely match numpy

# Create Tensor
TENSOR = torch.tensor([[[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]]])
print(f"Tensor dimension: {TENSOR.ndim} and shape: {TENSOR.shape}")
print(TENSOR[0])  # Meaning we have one dimension of 3X3
