### ML Algorithm vs Traditional Programming:
* **Traditional** - Given inputs and rules (function), what is the output?
* **ML** - Given the inputs and the desired outputs, what are the rules (functions)?
<img src="https://github.com/shreya888/Daily-Code-Diary/assets/25200389/adcaffed-5f40-4e43-9b08-677f0e88b666" width=50%>

### Why ML (DL)?
* "If u can build a *simple rule-based* system that does not require ML, do that." - Google's ML Handbook
* ML is advantageous for:
  * Problems with long list of rules (e.g. self-driving car rules)
  * Continuially changing environments (DL can adapt/learn)
  * Discovering new insights within large collections of data
* When NOT to use ML/DL (typically):
  * Need explainability (typically uninterpretable by humans)
  * When traditional approach is better suited
  * When errors are unacceptable (since DL outputs are probabilistic and so not predictable)
  * Limited availability of data

*There are ways to make ML/DL reproduable (predictable), explainable etc. This is a generic list

### ML vs DL

| ML  |  DL |
|---|---|
| Structured data (rows and columns) | Unstructured data |
|Common Algos:|
| Random Forest | Neural Nets |
| Gradient Boosted Algos (XGBoost) | Fully Connected Neural Nets (FCNN) |
| Naive Bayes | Convolutional NN (CNN) |
| Nearest Neighbour | Recurrent NN (RNN) |
| Support Vector Machine (SVM) etc. | Transformer etc. |

*(Note: Unstructured data like images and audio can be converted into a structured format using tensors.)*

### Anatomy of neural networks
🠋 Inputs - Text, Images, Audio etc. which cannot be understood by computers 

🠋 Numerical Encoding - for computer to understand data, it needs to be numbers

🠋 NeuralNetwork - Learns representations (patterns/features/weights)

🠋 Representational Ouputs - Features/matrix/weight tensor/learned reprentation (usually need to be converted for humans to undertand)

🠋 Outputs - Human understandable/interpretable terms

<img src="https://github.com/shreya888/Daily-Code-Diary/assets/25200389/f79e4a4e-0258-46d2-b3d5-d586c25cbc71" width=60%>

* Inner Layer - Data goes in here
* Hidden Layer(s) - Learns patterns in data
* Output Layer - Ouputs learned representation or prediction probabilities

