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
print(f"Element-wise multiplication (mul): {torch.mul(x,y)}, Matrix multiplication (matmul): {torch.matmul(x,y)}")

# Slicing operations like numpy
x = torch.rand(5, 3)
# print(x)
print(x[:, 0])  # Get all rows for 0th column
print(x[1, :])  # Get row number 1 but all columns
print(x[1, 1])  # Get element at position 1,1
# If have only 1 element and want to get the actual value use:
print(x[1, 1].item())


# Reshaping Tensor
x = torch.rand(4, 4)
y = x.view(16)  # Convert to 1D vector; number of elements must still be the same
# If we don't want to put the dimension value for 1 of the dimensions then
# we can just write "-1" and Pytorch will calculate it
y = x.view(8, -1)
print(y.size())
