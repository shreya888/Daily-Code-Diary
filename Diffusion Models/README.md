These are my notes from when I was studying the [How diffussion models work](https://learn.deeplearning.ai/courses/diffusion-models/lesson/1/introduction) course at [deeplearning.ai](deeplearning.ai).

# What Are Diffusion Models in Essence?

Diffusion models have become popular due to their ability to generate high-quality, diverse, and realistic data (e.g., images, audio, text), making them a powerful tool in generative modeling.

### Goal:
The primary goal of diffusion models is to generate novel images that are not part of the training set. These models aim for the neural network (NN) to learn fine details (like hair or accessories), general outlines (such as the distinction between the head and body), and everything in between.

### Understanding the Noising Process:
To help the model focus on different levels of detail, a process called "noising" is used, where progressively increasing amounts of noise are added to the images. This concept is inspired by diffusion in Physics. Analogy—imagine dropping ink into clear water. Initially, the ink forms a concentrated drop, but as it disperses, the ink becomes increasingly disperses and eventually becomes indistinguishable from water as it mixes in homogeneously.

### How the Forward Process (Diffusion) Works:
This is a process where data (like an image) is progressively corrupted by adding noise over several steps. By the end of this process, the data is almost indistinguishable from random noise. Pitorial representation below:

<img src="https://github.com/user-attachments/assets/64c603cd-83e3-4041-8d1e-fe8fca38d3f7" width=50%>


1. **No Noise**: The image is in its original, pristine form.
2. **Little Noise**: Small amounts of noise suggest possible details that might need to be filled in by the model.
3. **Moderate Noise**: More noise blurs finer details, but the general details and overall structure of the object remains discernible.
4. **Heavy Noise** (Completely Noisy): With significant noise, the broadest outline  is also difficult to distinguish, which is the starting point for our neural net to suggest what the object might look like denoised.

### Reverse Process (Denoising):
The model is trained to reverse the noising process by gradually removing the noise, step by step, to recover the original data. Starting from pure noise, the model learns to denoise it to reconstruct the data.

### Training the Neural Network:
During training, the model is given pairs of slightly noisy data and the original data. It learns to predict the less noisy version of the data at each step of the reverse process. When noise is added to the point that the model "has no idea" what the image originally was, this high level of noise follows a normal (Gaussian) distribution. This is a key aspect of the training, as it allows the model to generalize beyond the training data.

### Generating New Images:
Once trained, the model can start with random noise and iteratively apply the learned reverse process to generate new, high-quality data samples. By sampling noise from a normal (Gaussian) distribution and feeding it through the trained NN, entirely new images can be generated from different samples. The model effectively "denoises" the random noise, transforming it into coherent images that were not part of the training set.


-----------------------------------------------------------------------------------------

# Sampling

Sampling in diffusion models is the process of generating new data, such as images, by reversing the noise addition process that the model was trained on. This involves starting with random noise and iteratively refining it to produce a coherent, realistic output.

### Key Concepts of Sampling:
1. **Noise Sample as input:**
The process begins with a noise sample drawn from a Gaussian distribution. This noise serves as the initial input to the model. This is passed onto our trained neural network.

2. **Iterative Refinement:**
The neural network (NN) tries to predict the noise for a t-1 timestep at each step t. By subtracting this predicted noise from the original noise sample at timestep t, the model gradually refines the image. Since this prediction for denoising is not perfect, the process is repeated multiple times. This reverse diffusion process is stochastic, meaning it involves some randomness, which contributes to the diversity of generated samples.

3. **Prediction and Correction:**
At each step, the NN predicts the noise that needs to be subtracted from the current sample. This predicted noise is then subtracted from the original noisy input, moving the sample closer to the desired output. However, since the prediction is only an approximation, not all noise is removed in one step. So we need to go through multiple iterations of this refinement process for high-quality results.

#### To summarize:
Noise sample -> trained NN -> predicts noise (not sample image) -> subtract this predicted noise from the earlier noise sample to get something more like the image we want to predict.

### Understanding Algorithmically:
Process -> Noise prediction, Subtraction from sample, and Re-noising
Repeated across multiple iterations, progressively refining the sample until it closely resembles the original data distribution.

#### Pseudocode:
<img src="https://github.com/user-attachments/assets/17ce163f-5687-465a-9162-727d0ca741b3" width=50%>


* #### Initial Setup:
  `Sample = Random Sample`
  The process starts with a random noise sample.

* #### Loop Through Time Steps:
  1) **Loop in Reverse Time**:
`For t = T to 1`
Sampling typically involves a predefined number of time steps (T). Each step (t) corresponds to a level of noise that is gradually reduced. The more steps in the process, the finer the details the model can capture, but it also requires more computational power and time. The denoising process iterates backward in time, starting from fully diffused noise (high noise) all the way back up moving towards a less noisy, more structured sample (aka when we first dropped the ink into the water).

  2) **Adding Controlled Noise:**
`extra_noise = random sample if t > 1 else extra_noise = 0`
If we're not at the final step, some additional noise is added back into the process. This step ensures that the sample remains within the expected noise distribution aka normal like the expected input.

  3) **Predicting Noise:**
`predicted_noise = trained_nn(x_t-1, t)`
The current noisy sample is passed through the trained neural network to predict the noise that should be subtracted.

  4) **Updating the Sample:**
   `s1, s2, s3 = ddpm_sampling(t)`
   `sample = s1 * (sample - s2 * predicted_noise) + s3 * extra_noise`
Using the DDPM (Denoising Diffusion Probabilistic Model) sampling algorithm, the predicted noise is scaled by s2 and subtracted from the current sample. The result is scaled by s1, and a small amount of scaled (s3) extra noise is added back in. This helps to maintain the stability of the model and prevents it from collapsing to the mean of the dataset.

#### Stabilizing the Model by Adding Noise Back In:
After denoising, the sample might not retain the expected noise distribution, which the neural network was trained on. By adding a small amount of noise back in, scaled according to the timestep the denoising is at (s3), the sample is kept within a distribution that the NN can handle in subsequent steps. Empirically, this addition of noise helps stabilize the NN, preventing it from collapsing into values close to an average of dataset rather than generating diverse and detailed samples.

#### Noise Schedule:
The process relies on a noise schedule, a sequence that dictates how much noise to remove at each step. The schedule is critical because it affects the quality and diversity of the generated samples. An optimal schedule balances between too much noise (leading to poor-quality outputs) and too little (resulting in low diversity).

### Challenges:
* **Computationally Intensive**: Sampling can be computationally expensive because it requires many iterations, each involving the model running complex computations.
* **Trade-off Between Speed and Quality**: Faster sampling methods exist but often at the cost of the quality or diversity of the generated images.

-----------------------------------------------------------------------------------------

# Neural Network behind Diffusion (Generally UNet)
Diffusion models commonly use the U-Net architecture, a neural network well-suited for image generation tasks due to its ability to capture both fine details and overall structures in images, thanks to its unique architecture. The U-Net architecture is crucial in both the noising and denoising processes in diffusion models.

### Key Features of U-Net in Diffusion Models:
#### 1. Encoder-Decoder Structure:
The U-Net has an encoder-decoder structure. In diffusion models, the output size should be the same as input such that full resolution of image is processed. This is ensured by U-Net, where the size of output is always the same as the input size.
  * **Encoder (Downsampling Path)**: Compresses the input image by progressively reducing its resolution and extracting high-level features through convolutional layers and pooling operations.
  * **Decoder (Upsampling Path)**: Mirrors the encoder but reverses the process, gradually restoring the image to its original size using upsampling layers. This helps recover fine details from the original image.

#### 2. Skip Connections:

Used to link layers from the encoder directly to the decoder at corresponding levels. These connections transfer detailed information from the downsampling path to the upsampling path, helping preserve fine-grained features that might otherwise be lost during compression.

#### 3. Handling Additional Information via Embeddings:

The U-Net in diffusion models can incorporate additional information in the form of embeddings that modify the generation process:
  * **Temporal Embedding (temb)**: Provides information about the time step (or noise level) in the diffusion process, allowing the model to adjust its predictions based on how much noise is present at each iteration.
  * **Context Embedding (cemb)**: Can be used to control the image generation process, for example by conditioning on text descriptions or other factors, allowing for guided generation (e.g., text-to-image models).

These embeddings are incorporated into the network's forward pass, often added or multiplied into the upsampling layers to modulate the output.

##### Example in Forward Pass:

`up2 = up1(cemb1 * up1 + temb1, down2)`

In this example, the context embedding (cemb1) is multiplied with the output of the previous layer (up1), while the temporal embedding (temb1) is added to refine the network’s prediction based on the noise level at that time step. This combined input is then processed by the next layer (down2).

#### 4. Multiscale Learning:

The U-Net architecture’s ability to handle multiple scales of image information, from global structures to finer details, is especially beneficial in diffusion models. This allows the model to effectively denoise images by progressively refining both the coarse and detailed features as the reverse diffusion process proceeds.

#### 5. Noise Prediction:

During sampling, the U-Net predicts the noise present in the image at each step. The predicted noise is subtracted from the input image, refining the noisy image to a cleaner version through several iterations.

#### 6. Maintaining Image Consistency:

Since the output size is always the same as the input size, the U-Net ensures that the generated images remain consistent in resolution. This makes it suitable for tasks like super-resolution, text-to-image generation, and other image-based tasks in diffusion models.

### To Conclude, Why use UNet for Difussion?
* **Efficient Denoising**: The combination of downsampling, upsampling, and skip connections enables the U-Net to efficiently denoise images while preserving fine details.
* **Incorporating Temporal and Contextual Information**: The ability to integrate temporal and contextual embeddings allows for guided/controlled generation, making the U-Net flexible in applications like text-to-image generation or super-resolution.
* **Scalability and Stability**: The U-Net is scalable and can process images at different resolutions, while the use of embeddings helps stabilize the neural network during the iterative noise removal process.

In summary, U-Net’s capacity to handle both global and fine features, along with its flexibility in processing embeddings, makes it an ideal choice for diffusion models. This architecture ensures high-quality image generation through its robust denoising process, which is crucial in generative modeling tasks.



















