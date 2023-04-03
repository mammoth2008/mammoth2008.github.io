2 机器学习与深度学习
2.1 机器学习的概念与原理

### 什么是机器学习？

- 教计算机从数据中学习
- 做出决定或预测
- 每个任务都没有明确的编程
- 随着经验的积累自动改进
- 应用于各种任务和领域

<!-- Lecture: 机器学习是人工智能的一个子领域, 重点是教计算机从数据中学习模式. 机器学习算法不是为每项任务编写具体的指令, 而是让计算机随着更多的数据和经验自动提高其性能. 这使它们能够在没有明确编程的情况下做出决定或预测. -->

<!-- Lecture: 机器学习是一种从数据中学习模式和知识的方法. 通过不断积累经验, 机器学习算法能够自动改进其性能. 机器学习已经广泛应用于各种任务和领域. -->

![Machine Learning](img/c02/machine-learning.png)
#### Machine Learning

![Machine Learning](img/c02/machine-learning.webp)
#### Machine Learning

### 机器学习原理

- 输入数据: 例子, 特征和标签
- 学习算法: 处理数据
- 模型: 学习过程的结果
- 对新数据进行预测或决策

### 机器学习为什么重要

- 实现复杂任务的自动化
- 提高效率和准确性
- 适应新的数据和情况
- 分析和发现大型数据集的模式

![Machine Learning](img/c02/machine-learning-applications.png)
#### Machine Learning

### 重要人物

- Arthur Samuel: Machine Learning
- Geoffrey Hinton: Deep Learning
- Yann LeCun: CNN
- Yoshua Bengio: RNN and LSTM
- 吴恩达: Coursera and Google Brain
- Ian Goodfellow: GAN
- Jürgen Schmidhuber: Reinforcement Learning
- 李飞飞: ImageNet

![Arthur Samuel](img/c02/author-samuel.webp)
#### Arthur Samuel

![Andrew Ng](img/c02/andrew-ng.webp)
#### Andrew Ng

![Ian Goodfellow](img/c02/Ian-Goodfellow.jpg)
#### Ian Goodfellow

![Jürgen Schmidhuber](img/c02/jurgen-schmidhuber.webp)
#### Jürgen Schmidhuber

![Fei-fei Li](img/c02/fei-fei-li.jpg)
#### Fei-fei Li

### 重点事件

- 1957: 感知机 Perceptron
- 1986: 神经网络的反向传播算法 Backpropagation
- 1997: 支持向量机 SVMs
- 2006: 深度学习 Deep learning
- 2012: AlexNet
- 2014: 生成对抗网络 GAN
- 2017: Transformer
- 2018: Diffusion Models
- 2022: ChatGPT

![Backpropagation](img/c02/backpropatation.webp)
#### Backpropagation

![SVM](img/c02/svm.png)
#### SVM

![GAN](img/c02/gan.jpg)
#### GAN

![Transformer Model](img/c02/Transformer-model.jpg)
#### Transformer Model

![Diffusion Models](img/c02/diffusion-model.png)
#### Diffusion Model

![ChatGPT](img/c02/chatgpt.jpg)
#### ChatGPT

### 关键论文

- Rosenblatt, F. (1958). The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain.
- Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by back-propagating errors.
- Cortes, C., & Vapnik, V. (1995). Support-vector networks.
- Hinton, G. E., Osindero, S., & Teh, Y. W. (2006). A fast learning algorithm for deep belief nets.
- Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet classification with deep convolutional neural networks.
- Goodfellow, I., Pouget-Abadie, ... & Bengio, Y. (2014). Generative adversarial networks.

### 机器学习分类

- 监督学习 Supervised Learning
- 无监督学习 Unsupervised Learning
- 强化学习 Reinforcement Learning

![Supervised Learning](img/c02/supervised-learning.jpg)
#### Supervised Learning

![Unsupervised Learning](img/c02/unsupervised-learning.png)
#### Unsupervised Learning

![Reinforcement Learning](img/c02/reinforcement-learning.png)
#### Reinforcement Learning

### 监督学习

- 从标记的数据中学习
- 分类和回归
- Linear Regression, SVM, Decision Tree

<!-- Lecture: 监督学习是机器学习的一种类型, 在这种学习中, 模型是使用标记的数据来训练的, 这些数据包含输入特征和相应的输出标签. 其目的是学习从输入到输出的映射, 这可用于未来的预测. -->

![Linear Regression](img/c02/linear_regression.png)
#### Linear Regression

![Decision Tree](img/c02/decision-tree.png)
#### Decision Tree

### 无监督学习

- 从未标记的数据中学习
- 聚类和降维
- K-means, PCA

<!-- Lecture: 无监督学习是一种处理无标签数据的机器学习. 其目的是发现数据中的潜在模式或结构, 例如将类似的数据点归类（聚类）或降低数据的维度, 以便进行可视化和分析. -->

![K-means](img/c02/k-means.png)
#### K-means

![PCA](img/c02/pca.png)
#### PCA

### 强化学习

- 从与环境的互动中学习
- 智能体, 环境, 行动和奖励
- Q-learning, Deep Q-Networks, Policy Gradients

<!-- Lecture: 强化学习是一种机器学习, 代理通过与环境的互动来学习做决定. 代理人以奖励或惩罚的形式接收反馈, 并试图通过学习最优策略, 在一段时间内使累积奖励最大化. -->
