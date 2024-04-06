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

### Different learning paradigms

* **Supervised Learning** - Learning from labeled data (input-output pairs)
* **Unsupervised Learning** - Discovering patterns in data without explicit labels
* **Self-supervised Learning** - Generating labels from the data itself (e.g., predicting missing parts of the input)
* **Semi-supervised Learning** - Combining labeled and unlabeled data for training
* **Reinforcement Learning** - Learning through interaction with an environment to achieve a goal by receiving rewards or penalties
* **Transfer Learning** - Utilizing knowledge from one task to improve learning in another task



