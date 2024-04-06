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
    - **Examples**: Classification, Regression.

* **Unsupervised Learning**:
  - **Definition**: Discovering patterns and structures in data without explicit labels.
  - **Key Concepts**:
    - **Clustering**: Grouping similar data points together.
    - **Dimensionality Reduction**: Reducing the number of features while preserving essential information.
    - **Examples**: Clustering, Dimensionality Reduction, Anomaly Detection.

* **Self-supervised Learning**:
  - **Definition**: Generating labels from the data itself, often by predicting missing parts of the input.
  - **Key Concepts**:
    - **Auxiliary Tasks**: Training a model to solve related tasks that indirectly benefit the primary task.
    - **Examples**: Predicting missing words in a sentence (Masked Language Model), Image Inpainting.

* **Semi-supervised Learning**:
  - **Definition**: Combining labeled and unlabeled data for training, leveraging the abundance of unlabeled data.
  - **Key Concepts**:
    - **Utilization of Unlabeled Data**: Incorporating unlabeled data to improve model performance.
    - **Examples**: Pseudo-labeling, Co-training, Tri-training.

* **Reinforcement Learning**:
  - **Definition**: Learning through interaction with an environment to achieve a goal by receiving rewards or penalties.
  - **Key Concepts**:
    - **Agent-Environment Interaction**: The agent takes actions in an environment and receives feedback in the form of rewards and observations.
    - **Exploration vs. Exploitation**: Balancing between trying out new actions and exploiting known actions.
    - **Examples**: Game Playing (e.g., AlphaGo), Robotics, Autonomous Driving.

* **Transfer Learning**:
  - **Definition**: Utilizing knowledge gained from one task to improve learning in another task, often by transferring learned features or parameters.
  - **Key Concepts**:
    - **Pre-trained Models**: Models trained on large-scale datasets and fine-tuned on task-specific data.
    - **Feature Extraction vs. Fine-tuning**: Transfer learning can involve either using pre-trained models as feature extractors or fine-tuning the entire model.
    - **Examples**: Image Classification (using pre-trained models like VGG, ResNet), Natural Language Processing (using pre-trained language models like BERT, GPT).






