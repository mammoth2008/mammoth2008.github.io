1. 人工智能技术概述
1.2 人工智能的发展历史

![AI Timeline](img/c01/ai-history.jpg)
#### Timeline

### 计算简史

- 古代
- 近代与近现代
- 现代和当代

### 古代

- 古希腊, Antikythera Mechanism, 安提基特拉机械
- 古中国, 列子·汤问, 偃师造人
- 古中国, 水动机械
- 古土耳其, Al-Jazari

![Antikythera Mechanism](img/c01/Antikythera.webp)
#### Antikythera Mechanism

![Antikythera Mechanism](img/c01/Antikythera-Mechanism.png)
#### Antikythera Mechanism

![Antikythera Mechanism](img/c01/Antikythera-Mechanism1.jpeg)
#### Antikythera Mechanism

![列子·汤问 偃师造人](img/c01/yanshi.png)
#### 列子·汤问 偃师造人

![Water Clock](img/c01/clocktower.jpg)
#### 中国古代的水力机械

![Water Clock](img/c01/clocktower1.webp)
#### 中国古代的水力机械

![Al-Jazari](img/c01/al-jazari.webp)
#### Ismail Al-Jazari (1136 - 1206)

### 近代与近现代

- 法国, Blaise Pascal 机械计算机
- 法国, Pierre Jaquet-Droz 自动人偶
- 法国, Joseph Marie Jacquard 提花织布机
- 英国, Charles Babbage & Ada Lovelace 分析机和差分机

![Pascal Calculator](img/c01/pascal-calculator.jpg)
#### Blasise Pascal Calculator

![Jaquet-Croz](img/c01/jaquet-droz.jpg)
#### Pierre Jaquet-Droz Automata

![Jaquet-Croz](img/c01/jaquet-droz1.jpeg)
#### Pierre Jaquet-Droz Automata

![Joseph Maie Jacquard](img/c01/jacquard-loom.jpg)
#### Jacquard Loom

![Joseph Maie Jacquard](img/c01/jacquard-loom1.jpg)
#### Jacquard Loom

![Babbage Difference Engine](img/c01/difference-engine.jpeg)
#### Babbage Difference Engine

![Babbage Analytical Engine](img/c01/analytical-engine.jpg)
#### Babbage Analytical Engine

![Ada Lovelace](img/c01/ada-lovelace.jpg)
#### Ada Lovelace

### 现代和当代

- 英国, Turing Machine, Turing Test
- 美国, ENIAC, UNIVAC I
- 美国, IBM PC
- 英国, World Wide Web
- 美国, Deep Blue
- 英国, AlphaGo
- 美国, ChatGPT

![Alan Turing](img/c01/turing-book.jpg)
#### Alan Turing

![Turing Machine](img/c01/turing-machine.jpg)
#### Turing Machine

![Turing Test](img/c01/turing-test-game.jpg)
#### Turing Test

![ENIAC](img/c01/eniac.png)
#### Electronic Numerical Integrator And Computer

![UNIVAC 1](img/c01/univac1.jpeg)
#### UNIVersal Automatic Computer 1

![IBM PC](img/c01/ibm-pc.webp)
#### IBM Personal Computer

![Tim Berners-Lee](img/c01/Tim_Berners-Lee.jpg)
#### Tim Berners-Lee

![The First WWW Server](img/c01/First_Web_Server.jpg)
#### The First World Wide Web Server

![Deep Blue](img/c01/deep-blue.jpg)
#### Deep Blue from IBM

![AlphaGo](img/c01/alphago.webp)
#### AlphaGo from DeepMind

![Sam Altman](img/c01/sam-altman.webp)
#### Sam Altman from OpenAI

### AI 英雄榜

- Marvin Minsky, JohnMcCarthy, 基于表示和推理 (1969, 1971)$
#### Allen Newell, Herbert Simon, 问题求解, 符号模型 (1975)$
#### Edward Feigenbaum, Raj Reddy, 专家系统 (1994)$
#### Geoffrey Hinton, Yann LeCun, Yoshua Bengio 深度学习 (2018)

![A.M Turing Award](img/c01/Turing_Bowl.jpg)
#### ACM A.M Turing Award (Turing Bowl)

![DL3](img/c01/dl3.jpeg)
#### Geoffrey Hinton, Yann LeCun and Yoshua Bengio

### AI 的诞生与发展

- AI 的诞生 (1943-1956)$
#### 第一波浪潮 (1952-1969)$
#### 第一次寒冬 (1966-1973)$
#### 专家系统 (1969-1986)$
#### 神经网络回归 (1986-)$
#### 概率推理和机器学习 (1987-)$
#### 大数据 (2001- )$
#### 深度学习狂潮 (2011- )$
#### 大语言模型 (2020-)

### AI 的诞生 (1943-1956)
#### Warren McCulloch, Walter Pitts, 人工神经元
- Donald Hebb, Hebbian Learning
- Marvin Minsky, Dean Edmonds, SNARC, 40 个神经元构成的网络
- Arthur Samuel, 跳棋程序
- Alan Turing, 图灵机和图灵测试
- Dartmouth Summer Research Project on Artificial Intelligence
- Logic Theorist

![Warren McCulloch and Walter Pitts](img/c01/McCulloch-Pitts.png)
#### Warren McCulloch and Walter Pitts

![Neuron](img/c01/neuron.gif)
#### Neuron

![M-P model](img/c01/m-p-model.png)
#### McCulloch-Pitts Model

![Donald Hebb](img/c01/hebb.jpg)
#### Donald Hebb

<!-- Lecture: Hebb 学习规则是 Donald Hebb 在 1949 年提出的一种学习规则, 用来描述神经元的行为是如何影响神经元之间的连接的: 如果相链接的两个神经元同时被激活, 我们可以认为这两个神经元之间的关系应该比较近, 因此将这两个神经元之间连接的权值增加; 而一个被激活一个被抑制, 显然两者间的权值应该减小. Hebb 还有一句非常著名的话, "neurons that fire together, wire together." 它是一个无监督学习规则, 使网络能够提取训练集的统计特性, 从而把输入信息按照相似程度划分为若干类.-->

![SNARC](img/c01/snarc.png)
#### SNARC by Marvin Minsky and Dean Edmonds

<!-- Lecture: Marvin Minsky 根据自己的数学模型, 创造了世界上第一台具有学习功能的机器, 即由真空管组成的人工神经网络 SNARC, 意为 "随机神经网络模拟加固计算器".  -->

![Arthur Samuel](img/c01/samuel.webp)
#### Arthur Samuel and Checkers

<!-- Lecture: 1956 年, Arthur Samuel 发明了一种能够通过自我学习攻克国际跳棋 (Checkers) 游戏的算法, 现在该算法被称为强化学习 (Reinforcement Learning). -->

### 

![Alan Turing](img/c01/Alan-Turing.webp)$
#### Alan Turing

![Dartmouth Summer Research Project on Artificial Intelligence](img/c01/dartmouth-workshop.webp)
#### Dartmouth Summer Research Project on Artificial Intelligence

![Logic Theorist](img/c01/newell-simon.jpeg)
#### Newell and Simon and Logic Theorist

<!-- Lecture: 逻辑理论家引出了几个对人工智能研究至关重要的概念: Reasoning as search, Heuristic search, and list processing. 推理即搜索, 启发式方法, 以及列表处理.-->

### 第一波浪潮 (1952-1969)
#### "Look, Ma, no hands!"
- Newell and Simon, General Problem Solver
- John McCarthy, Lisp
- Marvin Minsky, Blocks World
- Frank Rosenblatt, Perceptron (感知机)

### 第一次寒冬 (1966-1973)
#### 使用范围有限
- 能解决的问题简单
- 未能帮助工业发展
- Lighthill Report, 1973

![James Lighthill](img/c01/james-lighthill.webp)
#### James Lighthill, Author of Lighthill Report

<!-- Lecture: Imagine that you are teaching a very smart robot how to do a task, like cleaning your room. You can tell it exactly what to do step by step, and it will follow your instructions perfectly. But if you ask the robot to do something that it has never seen before, like picking up a new toy that you just bought, it might not know what to do.

### In the 1950s and 60s, researchers realized that creating intelligent machines was a lot harder than they thought. During the first AI winter of 1966-1973, many researchers and companies working on AI projects faced a lot of frustration and disappointment because they weren't able to make as much progress as they had hoped. This led to a decrease in funding and support for AI research, and many projects were put on hold or cancelled.


### The Lighthill Report, published in 1973, was a critical assessment of the state of artificial intelligence (AI) research at the time. The report was commissioned by the British government and was led by Sir James Lighthill, a mathematician and professor of theoretical physics.

### The report was highly critical of the progress being made in AI research at the time, and argued that the field had failed to live up to the expectations that had been set for it. The report claimed that AI researchers had overpromised and underdelivered, and that the progress being made in the field was largely incremental and lacked the breakthroughs that had been promised.


### One of the main criticisms in the report was that AI research was too focused on general problem-solving, and not enough on specific applications. The report argued that AI researchers were too focused on creating a general problem-solving machine, rather than developing AI applications that could solve specific problems.

### The report also criticized the use of heuristic methods in AI research, arguing that these methods were not well-suited to solving complex problems. Heuristics are problem-solving techniques that use trial and error and rules of thumb, rather than systematic analysis, to find solutions.


### The Lighthill Report was significant in that it led to a significant reduction in funding for AI research in the UK, and in other countries as well. This period, known as the "AI Winter," saw a decline in interest and funding for artificial intelligence research until the mid-1980s. However, the report did not halt AI research altogether, and the field continued to make slow progress despite the reduced funding. -->

### 专家系统 (1969-1986)
#### Dendral, The First Knowledge-intensive System
- Expert Systems
- MYCIN, About 450 Rules
- DEC, R1, 1982
- Market: A Few Million (1980) - billions (1988)

<!-- Lecture: DENDRAL 系统是一种帮助化学家判断某待定物质的分子结构的专家系统. 1965 年在美国斯坦福大学开始研制, 1968年研发成功, 它是 Feigenbaum 与化学家 J.Lederberg 合作的结果. 20 世纪 60 年代中期, Lederberg 提出了一种可以根据输入的质谱仪数据列出所有可能的分子结构的算法, 并在此后的 3 年里, 与 Feigenbaum 等人一起探讨了用规则表示知识系统的建立方法, 建成了 DENDRAL 系统, 期望利用这一系统在更短的时间里完成类似与人工列些所有可能分子结构的工作. DENDRAL 是世界上第一例成功的专家系统. -->

<!-- Lecture: MYCIN 与 DENDRAL 有两个主要区别. 首先, 不像 DENDRAL 规则, 不存在可以推导出 MYCIN 规则的一般理论模型, MYCIN 规则不得不从大量的专家访谈中获得. 其次, 规则必须反映与医学知识相关的不确定性. MYCIN 引入了一种称为确定性因子 (Certainty Factor) 的不确定性计算. -->

### 神经网络回归 (1986-)
#### 反向传播算法, Back-propagation
- 联结主义重新抬头, Connectionist
- 流畅而不精确
- 从样本中学习

![Back-propagation](img/c01/back-propagation.png)
#### Back-propagation

### 概率推理和机器学习 (1987-)
- 研发的基准: 数据集和竞赛
- Hidden Markov Model, HMM
- Bayesian Network
- Reinforcement Learning & Markov Decision Processe

<!-- Lecture: HMM 有两个相关的方面. 首先, 它们基于严格的数学理论. 这使得语音研究人员能够在其他领域数十年数学成果的基础上进行开发. 其次, 它们是在大量真实语音数据的语料库上训练而产生的. 这确保了健壮性, 并且在严格的盲测中, HMM的分数稳步提高. 因此, 语音技术和手写体字符识别的相关领域向广泛的工业和消费级应用过渡.  -->

![ViaVoice from IBM](img/c01/ViaVoice.jpg)
#### ViaVoice from IBM

### 大数据 (2001- )
- 大力出奇迹
- 自然语言理解
- 计算机视觉
- IBM, Watson
- 数据集成为 AI 的重要基础

<!-- Lecture: 如果有足够大的数据集, 合适的学习算法在识别句意的任务上可以达到超过96%的准确率. 此外, Banko and Brill (2001) 认为, 将数据集的规模增加两到三个数量级所获得的性能提升, 会超过调整算法带来的性能提升. -->

<!-- Lecture: 类似的现象似乎也发生在计算机视觉任务中, 例如填补照片中的破洞. Hays and Efros, (2007) 开发了一种巧妙的方法, 从类似的图像中混合像素. 他们发现, 该技术在仅包含数千幅图像的数据库中效果不佳, 但在拥有数百万幅图像的数据库中, 该技术超过了质量阈值. 不久之后, ImageNet 数据库 (Deng et al., 2009) 中可用的数千万幅图像引发了计算机视觉领域的一场革命.  -->

![IBM Watson](img/c01/ibm-watson.webp)
#### IBM Watson Defeats Humans in "Jeopardy!"

![Dataset of GPT-3](img/c01/dataset.png)
#### Dataset of GPT-3

### 深度学习狂潮 (2011- )
- 人多力量大
- 多层神经网络
- 卷积神经网络, Convolution Neural Network
- 循环神经网络, Recurrent Neural Network
- 算法和算力成为 AI 的重要基础

<!-- Lecture: 一个标准的计算机 CPU 每秒可以进行 10^9 或 10^10 次运算. 运行在特定硬件 (例如GPU, TPU 或 FPGA) 上的深度学习算法, 每秒可能进行 10^14 - 10^17 次运算, 主要是高度并行化的矩阵和向量运算. -->

![Deep Learning](img/c01/deep.png)
#### Deep Learning

![GPU Server](img/c01/compute-power.png)
#### GPU Server

### 大语言模型 (2020-)
- Transformer Model
- RLHF, Reinforcement Learning from Human Feedback
- Parameter War: 0.3B, 1.5B, 175B, 540B, 1200B

<!-- Lecture: 参数是可以根据模型自身的算法, 通过数据迭代自动学习出的变量. -->

![Parameter War](img/c01/parameter-war.jpg)
#### Parameter War

![Parameter War](img/c01/war3.png)
#### Parameter War

### 今天

- Stanford AI100 and AI Index
- "前所未有之大变局"
- Artificial Narrow Intelligence, ANI
- Artificial General Intelligence, AGI
- Artificial Superintelligence, ASI
- 我们该如何看待 AI?

![AI Revolution](img/c01/ai-revolution.jpg)
#### AI Revolution
