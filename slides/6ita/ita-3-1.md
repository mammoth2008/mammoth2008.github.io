3. 深度学习的数学基础
3.1 高等数学基础

### 函数的定义
- 量和量之间的关系如: $ A = \pi r^2 $
- $ y = f(x) $ 其中 $ x $ 是自变量, $ y $ 是因变量
- 函数在 $ x\_0 $ 处取得的函数值 $ y\_0 = \left. y \right|\_{x = x\_0} = f(x\_0) $
- 符号只是一种表示, 也可以: $ y = g(x) $, $ y = \varphi(y) $, $ y = \psi(x) $

### 几种函数
- 分段函数
- 反函数
- 显函数与隐函数

### 分段函数
$$
f(x) = \begin{cases}
\sqrt{x}, & x \geq 0 \\\
-x, & x < 0
\end{cases}
$$

### 反函数
- 若 $ y = f(x) $, 则反函数表示为 $ x = f^{-1}(y) $
$$
h = \frac{1}{2} g t^2 \rightarrow h = h(t)
$$
$$
t = \sqrt{\frac{2h}{g}} \rightarrow t = t(h)
$$

### 显函数与隐函数
- 显函数形式如 $ y = f(x) $
$$
y = x^2 + 1
$$
- 隐函数形式如 $ F(x, y) = 0 $
$$
3x + y - 4 = 0
$$

### 函数的几种特性
- 奇偶性
- 周期性
- 单调性

### 奇偶性
- 偶函数: y 轴对称
$$
f(-x) = f(x)
$$
$$
f(x)= x^2
$$
$$f(-x) = (-x)^2 = x^2 = f(x)
$$
- 奇函数: 原点对称
$$
f(-x) = - f(x)
$$
$$
f(x)= x^3
$$
$$
f(-x) = (-x)^3 = -x^3 = - f(x)
$$

### 周期性
$$
f(x+T) = f(x)
$$

### 单调性
- 单调递增函数
$$
f(x) = \log(x+1)
$$
- 单调递减函数
$$
f(x) = -\log(x+1)
$$

### 数列
- 按照一定次序排列的一列数 $ u\_1, u\_2, \cdots, u\_n, \cdots $ 其中 $ u_n $ 叫做通项
- 对于数列 $ \\{ u\_n \\} $ :
- 如果当 $ n $ 无限增大时, 其通项无限接近于一个常数 $ A $
- 则称该数列以 $ A $ 为极限, 或数列收敛于 $ A $
- $ \lim\limits\_{n \to \infty} u\_n = A, $ 或 $ u\_n \to A \ (n \to \infty) $
- 否则称数列为发散
- $ \lim\limits\_{n \to \infty} \frac{1}{3^n} = 0, \quad \lim\limits\_{n \to \infty} \frac{n}{n+1} = 1, \quad \lim\limits\_{n \to \infty} 2^n $ 不存在

### 符号表示
- $ x \to \infty $ 表示 "当 $ |x| $ 无限增大时"
- $ x \to +\infty $ 表示 "当 $ x $ 无限增大时"
- $ x \to -\infty $ 表示 "当 $ x $ 无限减小时"
- $ x \to x\_0 $ 表示 "当 $ x $ 从 $ x\_0 $ 左右两侧无限接近 $ x\_0 $ 时"
- $ x \to x\_0^+ $ 表示 "当 $ x $ 从 $ x\_0 $ 右侧无限接近 $ x\_0 $ 时"
- $ x \to x\_0^- $ 表示 "当 $ x $ 从 $ x\_0 $ 左侧无限接近 $ x\_0 $ 时"

### 极限
$$ \lim\limits\_{x \to +\infty} e^{-x} = 0 $$
$$ \lim\limits\_{x \to \infty} \frac{1}{x} = 0 $$
$$ \lim\limits\_{x \to -\infty} \arctan{x} = -\frac{\pi}{2} $$

### 极限
- 函数在 $ x\_0 $ 的领域内有定义, $ \lim\limits\_{x \to x\_0} f(x) = A, $ 或 $ f(x) \to A \ (x \to x\_0) $
$$
\lim\limits\_{x \to 1} \frac{x^2 - 1}{x - 1} = \lim\limits\_{x \to 1} \frac{(x-1)(x+1)}{x-1} = 2
$$
- 左右极限: 函数在左半领域/右半领域内有定义
- $ \lim\limits\_{x \to x\_0^+} f(x) = A $, 或 $ f(x) \to A \ (x \to x\_0^+) $
- $ \lim\limits\_{x \to x\_0^-} f(x) = A $, 或 $ f(x) \to A \ (x \to x\_0^-) $

### 极限
- $ \lim\limits\_{x \to x\_0} f(x) = A $ 的充要条件是
$$ \lim\limits\_{x \to x\_0^-} f(x) = \lim\limits_{x \to x\_0^+} f(x) = A $$

### 极限
$$ f(x) = \begin{cases}
x - 1, & x < 0 \\\
0, & x = 0 \\\
x + 1, & x > 0
\end{cases} $$
 当 $ x \to 0 $ 时 $ f(x) $ 的极限
$$ \lim\limits\_{x \to 0^+} f(x) = \lim\limits\_{x \to 0^+} (x + 1) = 1 $$
$$ \lim\limits\_{x \to 0^-} f(x) = \lim\limits\_{x \to 0^-} (x - 1) = -1 $$
$ \therefore \lim\limits\_{x \to 0} f(x) $ 不存在
