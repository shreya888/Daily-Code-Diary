# Pytorch

* Widely-used deep learning framework renowned for its flexibility and ease of use in research settings. (very similar to Numpy)
* Write high-performance/fast/optimized deep learning code in Python, allowing seamless execution on various hardware accelerators (GPUs, TPUs, and multiple GPUs in parallel).
* Access to a rich ecosystem of pre-built deep learning models through TorchHub or torchvision.models, facilitating rapid prototyping and experimentation (transfer learning, fine-tuning etc. possible).
* Comprehensive set of tools for the full stack of deep learning workflows, including data preprocessing, model design, training, and deployment in various environments (local applications, cloud platforms, or Docker containers etc).
* Initially developed by Meta (Facebook AI Research), PyTorch has evolved into an open-source project with a thriving community contributing to its development and enhancement. Its dynamic computation graph and imperative programming paradigm make it particularly well-suited for dynamic, research-oriented deep learning tasks, where rapid experimentation and model iteration are paramount.

### What is GPU/TPU?
* GPU (Graphic Processing Unit) - Specialized hardware component designed for parallel processing of large blocks of data.
* Originally developed for rendering graphics in video games and multimedia applications, GPUs have evolved into powerful computational engines capable of accelerating a wide range of tasks, including deep learning.
* TPU (Tensor Processing Unit) - Custom-designed hardware accelerator developed by Google specifically for accelerating machine learning workloads, particularly those involving tensor operations.

### What is Tensor?
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
