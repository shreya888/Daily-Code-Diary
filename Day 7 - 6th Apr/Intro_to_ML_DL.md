# Introduction to ML/DL/NN

### ML Algorithm vs Traditional Programming:

* **Traditional Programming**: Given inputs and rules (function), what is the output?
* **ML**: Given the inputs and the desired outputs, what are the rules (functions)?

<img src="https://github.com/shreya888/Daily-Code-Diary/assets/25200389/adcaffed-5f40-4e43-9b08-677f0e88b666" width=50%>

### Why ML (DL)?

* "If you can build a *simple rule-based* system that does not require ML, do that." - Google's ML Handbook
* ML is advantageous for:
  * Problems with a long list of rules (e.g., self-driving car rules)
  * Continually changing environments (DL can adapt/learn)
  * Discovering new insights within large collections of data
  * ML over a complex heuristic (unmaintainable)
* When NOT to use ML/DL (typically):
  * Need for explainability (typically uninterpretable by humans)
  * When traditional approaches are better suited
  * When errors are unacceptable (since DL outputs are probabilistic and not always predictable)
  * Limited availability of data

*(Note: There are ways to make ML/DL reproducible (predictable), explainable, etc. This is a generic list.)*

### ML vs DL

| ML               | DL                              |
|------------------|---------------------------------|
| Structured data with rows and columns | Unstructured data |
| Common Algorithms: | |
| Random Forest    | Neural Networks                 |
| Gradient Boosted Algorithms (XGBoost) | Fully Connected Neural Networks (FCNN) |
| Naive Bayes      | Convolutional Neural Networks (CNN) |
| Nearest Neighbour | Recurrent Neural Networks (RNN) |
| Support Vector Machine (SVM) etc. | Transformer etc. |

*(Note: Unstructured data like images and audio can be converted into a structured format using tensors.)*

### Anatomy of neural networks

🠋 Inputs - Text, Images, Audio, etc., which cannot be understood by computers 

🠋 Numerical Encoding - Data must be represented in numerical form for computer processing

🠋 Neural Network - Learns representations (patterns/features/weights)

🠋 Representational Outputs - Features/matrix/weight tensor/learned representation (usually need to be converted for humans to understand)

🠋 Outputs - Human understandable/interpretable terms

<img src="https://github.com/shreya888/Daily-Code-Diary/assets/25200389/f79e4a4e-0258-46d2-b3d5-d586c25cbc71" width=60%>

**Overall Architecture:**
* Inner Layer: Data input
* Hidden Layer(s): Learns patterns in data
* Output Layer: Outputs learned representation or prediction probabilities

*Patterns = Embeddings = Weights = Feature Representation = Feature Vector*

*Each layer is a combination of linear and non-linear functions.*


### Different Learning Paradigms
* **Supervised Learning**:
  - **Definition**: Learning from labeled data, where the model learns to map input data to known output labels.
  - **Key Concepts**:
    - **Training Data**: Consists of input-output pairs. Train -> Validate -> Test (mutually exclusive datapoints)
    - **Loss Function**: Measures the discrepancy between predicted and actual outputs.
    - **Generalization**: The ability of the model to perform well on unseen data.
    - **Overfitting vs. Underfitting**: Balancing model complexity to avoid learning noise or being too simplistic.
    - **Evaluation Metrics**: Measures to assess model performance such as accuracy, precision, recall, and F1-score.
    - **Examples**: Classification, Regression.

* **Unsupervised Learning**:
  - **Definition**: Discovering patterns and structures in data without explicit labels.
  - **Key Concepts**:
    - **Dimensionality Reduction**: Reducing the number of features while preserving essential information.
    - **Clustering Algorithms**: Techniques such as K-means, hierarchical clustering, and DBSCAN for grouping similar data points.
    - **Dimensionality Reduction**: Reducing the number of features while preserving essential information. e.g. Principal Component Analysis (PCA), t-distributed Stochastic Neighbor Embedding (t-SNE) etc.
    - **Density Estimation**: Estimating the underlying probability distribution of the data.
    - **Examples**: Clustering, Dimensionality Reduction, Anomaly Detection.

* **Self-supervised Learning**:
  - **Definition**: Generating labels from the data itself, typically by solving auxiliary tasks that are designed to provide supervision signals without human-labeled data.
  - **Key Concepts**:
    - **Auxiliary Tasks**: Training a model to solve related tasks that indirectly benefit the primary task. Example:
      - **Contrastive Learning**: Learning representations by contrasting positive and negative examples.
      - **Autoencoding**: Training models to reconstruct the input from corrupted or incomplete versions.
      - **Temporal Ordering**: Predicting the temporal order of sequences without explicit supervision.
    - **Examples**: Predicting missing words in a sentence (Masked Language Model), Image Inpainting.

* **Semi-supervised Learning**:
  - **Definition**: Combining labeled and unlabeled data for training, leveraging the abundance of unlabeled data.
  - **Key Concepts**:
    - **Label Propagation**: Propagating labels from labeled to unlabeled data points based on their similarity.
    - **Consistency Regularization**: Ensuring model predictions remain consistent under small perturbations of the input.
    - **Manifold Assumption**: Assuming that data points close to each other in the input space should have similar labels.
    - **Examples**: Pseudo-labeling, Co-training, Tri-training.

* **Reinforcement Learning**:
  - **Definition**: Learning through interaction with an environment to achieve a goal by receiving rewards or penalties.
  - **Key Concepts**:
    - **Agent-Environment Interaction**: The agent takes actions in an environment and receives feedback in the form of rewards and observations.
    - **Exploration-Exploitation Tradeoff**: Balancing between trying out new actions (exploration) and exploiting known actions (exploitation).
    - **Markov Decision Process (MDP)**: A mathematical framework to model sequential decision-making under uncertainty.
    - **Policy Learning**: Learning a strategy (policy) to select actions in different states of the environment.
    - **Examples**: Game Playing (e.g., AlphaGo), Robotics, Autonomous Driving.

* **Transfer Learning**:
  - **Definition**: Utilizing knowledge gained from one task to improve learning in another task, often by transferring learned features or parameters.
  - **Key Concepts**:
    - **Pre-trained Models**: Models trained on large-scale datasets and fine-tuned on task-specific data.
    - **Domain Adaptation**: Adapting the model to a new domain with different data distributions.
    - **Fine-tuning**: Fine-tuning pre-trained models on task-specific data to adapt them to new tasks.
    - **Knowledge Distillation**: Transferring knowledge from a large, complex model to a smaller, simpler model; teacher to student.
    - **Feature Extraction vs. Fine-tuning**: Transfer learning can involve either using pre-trained models as feature extractors for bigger models or just fine-tuning the entire model or later few layers.
    - **Examples**: Image Classification (using pre-trained models like VGG, ResNet), Natural Language Processing (using pre-trained language models like BERT, GPT).


### Other Common Terminology in ML/DL
* **Instance**: An individual data point or observation in a dataset, typically represented as a single row, which you want to make a prediction for.
* **Label**: The output of prediction task or target variable that either the model is trying to predict or the right output supplied in training data.
* **Feature**: An input variable or property/attribute that is used in prediction tasks. Features can be numeric, categorical, or textual, and they provide information about the instances in a dataset.
* **Feature Column**: A column in a dataset that represents a specific feature. Each feature column contains values corresponding to the instances in the dataset.
* **Example**: A combination of an instance (with features) and it's label in a dataset.
* **Model**: A mathematical/statistical representation or algorithm of prediction task (learns patterns from data to make predictions or decisions). Models can be trained using various machine learning and deep learning techniques.
* **Metric**: A measure used to evaluate the performance of a model. Common metrics include accuracy, precision, recall, F1-score, mean squared error (MSE), and mean absolute error (MAE). A number u care about but cannot directly optimize.
* **Objective**: The goal or objective function or metric that the model aims to optimize during training. It defines the criteria for assessing the model's performance and guides the learning process.
* **Pipeline**: A sequence of data processing components or steps that are chained together to automate the machine learning workflow. Pipelines typically include data preprocessing, feature extraction, model training, and evaluation stages.




