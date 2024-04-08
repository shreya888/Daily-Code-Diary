import torch

# Manipulating tensors (tensor operations)
x = torch.rand(2, 2)
y = torch.rand(2, 2)

# Element wise addition, subtraction, multiplication and division
z = x + y
z = torch.add(x, y)  # Same thing
z = x - y
z = torch.sub(x, y)
z = x * y
z = torch.mul(x, y)
z = x / y
z = torch.div(x, y)

# Inplace addition
y.add_(x)  # Modifies y
# In general, in Pytorch every function that has a trailing underscore will modify the variable that it is applied on

# Matrix Multiplication (Dot Product)
z = torch.matmul(x,y)
z = x @ y  # same operation
z = torch.mm(x, y)  # same operation
print(f"Element-wise multiplication (mul): {torch.mul(x,y)}, Matrix multiplication (matmul): {torch.matmul(x,y)}\n")

# Slicing operations like numpy
x = torch.rand(5, 3)
# print(x)
print(x[:, 0])  # Get all rows for 0th column
print(x[1, :])  # Get row number 1 but all columns
print(x[1, 1])  # Get element at position 1,1
# If, have only 1 element and want to get the actual value use:
print(x[1, 1].item())
print()

# Reshaping Tensor
x = torch.rand(4, 4)
y = x.view(16)  # Convert to 1D vector; number of elements must still be the same
# If we don't want to put the dimension value for 1 of the dimensions then
# we can just write "-1" and Pytorch will calculate it
y = x.view(8, -1)
print(y.size())
print()

# Transpose - switches axes or dimensions of a given tensor; matrix manipulation
# Transpose shape of one of the matrix to fix our shape issue in matmul error
tensor_A = torch.rand(2,3)
tensor_B = torch.rand(2,3)
print(f"Original shape - tensor_B: {tensor_B.shape}, Transposed shape: {tensor_B.T.shape}, tensor_A stays the same: {tensor_A.shape}")
print(f"Multiplying: {tensor_A.shape}, {tensor_B.T.shape} <- Inner dimensions must match")
print(f"Output shape: {torch.mm(tensor_A, tensor_B.T).shape} <- Outer dimensions rule\n")

# Tensor Aggregation - min, max, mean, sum (because going from large amount of numbers to a small amount of numbers)
x = torch.arange(0, 100, 10)
# Find min
z = torch.min(x)
z = x.min()  # same
# Find max
z = torch.max(x)
z = x.max()
# Find mean - Note: torch.mean() function requires a tensor of float32 datatype to work
# Because the tensor we created is int64 (Long) which cannot be used in mean (floating or complex only)
z = torch.mean(x.type(torch.float32))
z = x.type(torch.float32).mean()
# Find sum
z = torch.sum(x)
z = x.sum()

# Finding Positional min & max of tensors

