# Pytorch

* Widely-used Python based machine learning framework renowned for its flexibility and ease of use from research prototyping to production deployment.
* Write high-performance and optimized deep learning code, with **hardware acceleration** on NVIDIA GPUs (GPUs, TPUs, and multiple GPUs in parallel).
* Libraries for vision, NLP, audio applications.
* Access to a rich ecosystem of **pre-built deep learning models** through TorchHub or torchvision.models (transfer learning, fine-tuning etc. possible).
* Most deep architectures are constructed by iterative combination and recombination of a finite set of architectural primitives.
* **Deep Learning Primitives** in Pytorch - data loading, NN layer types, activations, loss functions, and optimizers.
* Comprehensive set of tools for the full stack of deep learning workflows, including data preprocessing, model design, training, and deployment in various environments (local applications, cloud platforms, or Docker containers etc).
* Enables **fast research prototyping** with models in Python code, Automatic differentiation (torch.autograd), and eager mode.
* Initially developed by Meta (Facebook AI Research), PyTorch has evolved into an open-source project with a thriving community contributing to its development and enhancement. Its dynamic computation graph and imperative programming paradigm make it particularly well-suited for dynamic, research-oriented deep learning tasks, where rapid experimentation and model iteration are paramount.
* Supports **production deployment** - TorchScript, TorchServe, quantization.
* **Motivation** - Python, Numpy
  * NumPy offers manifold faster low-level implementations for matematical operations with vectorization than Python's 64 bit calculations leading to interpretor overhead.
  * Pytorch takes motivation from NumPy to make GPU accelerated code (X.cuda()) with automatic differentiation for backpropagation (dX = X.grad).
* Building Blocks - Tensors, Operations, Modules

### What is GPU/TPU?
* GPU (Graphic Processing Unit) - Specialized hardware component designed for parallel processing of large blocks of data.
* Originally developed for rendering graphics in video games and multimedia applications, GPUs have evolved into powerful computational engines capable of accelerating a wide range of tasks, including deep learning.
* TPU (Tensor Processing Unit) - Custom-designed hardware accelerator developed by Google specifically for accelerating machine learning workloads, particularly those involving tensor operations.

### What is Tensor?
* Pytorch building blocks
* Mathematical object that generalizes scalars, vectors, and matrices to higher dimensions. (multi-dimensional arrays)
* Primary/Fundamental data structures in DL used to represent input data, model parameters, and output data etc. componenets of DL pipeline throughout the computational graph.
  
| | | | |
|-|-|-|-|
| Scalar | Vector | Matrix | Tensor |
| 0D | 1D | 2D | Multi-D |

### Common mistakes
* Tensors not right *datatype* (tensor.dtype)
* Tensors not right *shape* (tensor.shape)
* Tensors not on the right *device* (tensor.device)

### Matrix Multiplication Rules:
1. *Inner dimensions* must match (inner most number in dimension of 1st matrix (right most in shape) == outer most number in dimension of 2nd matrix (left most in shape))
2. Resulting matrix will have shape of *outer dimension* (left most in shape of 1st (all except last), right most in shape of 2nd)


## References
* Eager vs graph execution mode - https://pytorch.org/blog/optimizing-production-pytorch-performance-with-graph-transformations/
* Autograd - https://pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html
* https://deepgenerativemodels.github.io/syllabus.html
