3 / 3

### 卷积神经网络 Convolutional Neural Networks (CNNs)

- 专门用于处理网格形数据，如图像
- 局部连接、权重共享和空间相关性
- 自动提取特征

<!-- Lecture: 卷积神经网络（CNNs）是一种专门用于处理网格形数据（如图像）的神经网络。它们利用局部连接、权重共享和空间相关性，自动提取图像中的特征。-->

![Convolutional Neural Networks](https://chat.openai.com/chat?model=gpt-4)

#### Convolutional Neural Networks

### CNN 的主要组成部分 Key Components of CNNs

- 卷积层 Convolutional Layer
- 池化层 Pooling Layer
- 全连接层 Fully Connected Layer

<!-- Lecture: CNN 的主要组成部分包括卷积层、池化层和全连接层。每一层都有特定的功能和目标。-->

![Key Components of CNNs](https://chat.openai.com/chat?model=gpt-4)

#### Key Components of CNNs

### 卷积层 Convolutional Layer

- 使用卷积核进行局部连接
- 学习空间特征
- 减少参数数量

<!-- Lecture: 卷积层通过使用卷积核进行局部连接，学习图像中的空间特征。这有助于减少网络中的参数数量。-->

![Convolutional Layer](https://chat.openai.com/chat?model=gpt-4)

#### Convolutional Layer

### 卷积相关概念和数学表示 Convolution Concepts and Mathematical Notation

- 卷积运算 Convolution Operation
- 滑动窗口 Sliding Window
- 步长 Stride
- 填充 Padding

<!-- Lecture: 卷积运算是一种数学操作，用于将两个函数组合成一个新的函数。在 CNN 中，这些函数通常表示为输入图像和卷积核。滑动窗口方法用于在图像上应用卷积核。步长决定了滑动窗口在图像上移动的速度。填充是在图像边缘添加额外像素的过程，以便卷积核能够覆盖整个图像。-->

![Convolution Concepts and Mathematical Notation](https://chat.openai.com/chat?model=gpt-4)

#### Convolution Concepts and Mathematical Notation

### 卷积运算 Convolution Operation


$$
s(t) = (x * w)(t) = \sum_{a=-\infty}^{\infty} x(a) w(t-a)
$$
<!-- Lecture: 在连续情况下，卷积运算定义为两个函数 $x$ 和 $w$ 的乘积的积分。这里，$s(t)$ 是卷积的结果，$t$ 是空间（或时间）变量。-->

### 二维卷积运算 2D Convolution Operation

$$
S(i, j) = (I * K)(i, j) = \sum_{m} \sum_{n} I(m, n) K(i-m, j-n)
$$

<!-- Lecture: 对于二维情况（如图像），卷积运算定义为两个二维函数（图像 $I$ 和卷积核 $K$）的乘积的双重求和。这里，$S(i, j)$ 是卷积的结果，$(i, j)$ 是空间坐标。-->

![2D Convolution Operation](https://chat.openai.com/chat?model=gpt-4)

#### 2D Convolution Operation

### 步长 Stride

- 控制滑动窗口在图像上移动的速度
- 用于减少输出尺寸和计算量
- 较大的步长可能导致信息丢失

<!-- Lecture: 步长是一个整数，表示滑动窗口在图像上移动的速度。较大的步长可以减少输出尺寸和计算量，但可能导致信息丢失。-->

![Stride](https://chat.openai.com/chat?model=gpt-4)

#### Stride

### 填充 Padding

- 在图像边缘添加额外像素
- 使卷积核能够覆盖整个图像
- 控制输出尺寸

<!-- Lecture: 填充是在图像边缘添加额外像素的过程，以便卷积核能够覆盖整个图像。这可以帮助我们控制输出尺寸。-->

![Padding](https://chat.openai.com/chat?model=gpt-4)

#### Padding



### 池化层 Pooling Layer

- 降低空间尺寸
- 减少计算量
- 增加平移不变性

<!-- Lecture: 池化层用于降低图像的空间尺寸，从而减少计算量。它还可以增加网络的平移不变性，有助于提高模型的泛化能力。-->

![Pooling Layer](https://chat.openai.com/chat?model=gpt-4)

#### Pooling Layer

2 / 2

### 池化层 Pooling Layer

- 降低特征图尺寸
- 减少参数数量和计算量
- 提取空间信息，增加模型的平移不变性

<!-- Lecture: 池化层用于降低特征图尺寸，减少参数数量和计算量。它们还可以提取空间信息，增加模型的平移不变性。-->

![Pooling Layer](https://chat.openai.com/chat?model=gpt-4)

#### Pooling Layer

### 常见的池化方法 Common Pooling Methods

- 最大池化 Max Pooling
- 平均池化 Average Pooling

<!-- Lecture: 最大池化是一种常用的池化方法，它选择给定窗口内的最大值作为输出。平均池化则计算窗口内所有值的平均值作为输出。-->

![Common Pooling Methods](https://chat.openai.com/chat?model=gpt-4)

#### Common Pooling Methods

### 最大池化 Max Pooling

- 选择窗口内的最大值作为输出
- 更关注显著特征

<!-- Lecture: 最大池化选择给定窗口内的最大值作为输出。这种方法更关注显著特征。-->

![Max Pooling](https://chat.openai.com/chat?model=gpt-4)

#### Max Pooling

### 平均池化 Average Pooling

- 计算窗口内所有值的平均值作为输出
- 更关注整体特征

<!-- Lecture: 平均池化计算窗口内所有值的平均值作为输出。这种方法更关注整体特征。-->

![Average Pooling](https://chat.openai.com/chat?model=gpt-4)

#### Average Pooling

### 全连接层 Fully Connected Layer

- 将卷积和池化层的输出连接到输出层
- 进行分类或回归任务

<!-- Lecture: 全连接层将卷积和池化层的输出连接到输出层，用于进行分类或回归任务。-->

![Fully Connected Layer](https://chat.openai.com/chat?model=gpt-4)

#### Fully Connected Layer

### 全连接层 Fully Connected Layer

- 将特征向量连接到输出
- 学习特征间的关系
- 最后一层通常用于分类或回归任务

<!-- Lecture: 全连接层将特征向量连接到输出，用于学习特征间的关系。最后一层全连接层通常用于分类或回归任务。-->

![Fully Connected Layer](https://chat.openai.com/chat?model=gpt-4)

#### Fully Connected Layer

### 作用 Function

- 捕捉特征之间的复杂关系
- 整合特征，进行决策

<!-- Lecture: 全连接层的作用是捕捉特征之间的复杂关系，并将这些特征整合在一起，以便进行决策。-->

![Function of Fully Connected Layer](https://chat.openai.com/chat?model=gpt-4)

#### Function of Fully Connected Layer

### 最后一层 Last Layer

- 输出层 Output Layer
- 用于分类或回归任务
- 激活函数 Activation Function

<!-- Lecture: 最后一层全连接层通常称为输出层，用于分类或回归任务。在这一层中，可以使用不同的激活函数来适应任务需求。-->

![Last Layer of Fully Connected Layer](https://chat.openai.com/chat?model=gpt-4)

#### Last Layer of Fully Connected Layer

