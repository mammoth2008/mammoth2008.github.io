3. 关系数据库标准语言 SQL
3.4 数据查询

数据查询
    SELECT [ALL | DISTINCT] <目标列表达式>, <目标列表达式>, ...
    FROM <表名或视图名> [AS <别名>]
    [WHERE <条件表达式>]
    [GROUP BY <列名1> [HAVING <条件表达式>]]
    [ORDER BY <列名2> [ASC|DESC]];

查询过程
- 根据 WHERE 子句中的条件表达式
- 从 FROM 子句指定的表中选出满足条件的元组
- 根据 SELECT 子句中的目标列表达式
- 选取元组中的属性
- 形成结果表

查询子句
- GROUP BY子句按照指定的列进行分组
- 可在每个组上应用聚集函数
- 若有 HAVING 条件则只输出满足条件的组
- 若有 ORDER BY 子句则对结果表排序

查询指定列
SELECT Sno, Sname FROM Student;

查询全部列
SELECT * FROM Student;

查询经过计算的值
SELECT Sname, 2014 - Sage FROM Student;

指定列别名
SELECT Sname AS NAME, 2014 - Sage AS BIRTHDAY FROM Student;

消除取值重复的行
SELECT DISTINCT Sno FROM SC;

査询满足条件的元组
- 使用 WHERE 子句
- 比较: <, >, <=, >=, =, !=
- 范围: BETWEEN AND, NOT BETWEEN AND
- 集合: IN, NOT IN

比较
SELECT Sname FROM Student WHERE Sdept = 'CS';

范围
SELECT Sname, Sdept, Sage FROM Student WHERE Sage BETWEEN 20 AND 23;

集合
SELECT Sname, Ssex FROM Student WHERE Sdept IN ('CS', 'MA', 'IS');

字符匹配
- 使用 LIKE 进行字符串匹配
- 可以使用通配符
- "%" 代表任意长度的字符串
- "_" 代表任意单个字符.

字符匹配
SELECT * FROM Student WHERE Sno LIKE '201215121';
SELECT Sname, Sno, Ssex FROM Student WHERE Sname LIKE '刘%';
SELECT Sname FROM Student WHERE Sname LIKE '欧阳_';
SELECT Sname, Sno FROM Student WHERE Sname LIKE '_阳%';
SELECT Sname, Sno, Ssex FROM Student WHERE Sname NOT LIKE '刘%';

涉及空值的查询
使用 IS NULL 谓词查询空值
SELECT Sno, Cno FROM SC WHERE Grade IS NULL;
使用 IS NOT NULL 谓词查询非空值
SELECT Sno, Cno FROM SC WHERE Grade IS NOT NULL;

多重条件查询
- 使用逻辑运算符 AND 和 OR 连接多个查询条件.
-  AND 的优先级高于 OR
- 可以使用括号改变优先级
SELECT Sname FROM Student WHERE Sdept = 'CS' AND Sage < 20;
SELECT Sname, Ssex FROM Student WHERE Sdept = 'CS' OR Sdept = 'MA' OR Sdept = 'IS';

ORDER BY子句
- 对查询结果按照属性列排序
- 可以对一个或多个属性列排序
- 默认按升序排列
SELECT Sno, Grade FROM SC WHERE Cno = '3' ORDER BY Grade DESC;
SELECT * FROM Student ORDER BY Sdept, Sage DESC;

聚集函数

#### COUNT函数
#### SUM函数
#### AVG函数
#### MAX函数
#### MIN函数
#### COUNT函数

- 用于统计元组个数或某一列中值的个数.
- 示例: 
  - 查询学生总人数: `SELECT COUNT(*) FROM Student;`
  - 查询选修了课程的学生人数: `SELECT COUNT(DISTINCT Sno) FROM SC;`

#### SUM函数

- 用于计算某一列值的总和（此列必须是数值型）.
- 示例: 
  - 计算选修1号课程的学生平均成绩: `SELECT AVG(Grade) FROM SC WHERE Cno = '1';`


#### AVG函数
- 用于计算某一列值的平均值（此列必须是数值型）.
- 示例: 
  - 计算选修1号课程的学生平均成绩: `SELECT AVG(Grade) FROM SC WHERE Cno = '1';`


#### MAX函数
- 用于求一列值中的最大值.
- 示例: 
  - 查询选修1号课程的学生最高分数: `SELECT MAX(Grade) FROM SC WHERE Cno = '1';`


#### MIN函数
- 用于求一列值中的最小值.
- 示例: 
  - 查询选修1号课程的学生最低分数: `SELECT MIN(Grade) FROM SC WHERE Cno = '1';`

#### 使用聚集函数的注意事项

- 当聚集函数遇到空值时, 除`COUNT(*)`外, 会跳过空值而只处理非空值.
- 注意, `WHERE`子句中不能使用聚集函数作为条件表达式, 聚集函数只能用于`SELECT`子句和`GROUP BY`中的`HAVING`子句.

### GROUP BY子句

- 使用`GROUP BY`子句将查询结果按某一列或多列的值分组, 值相等的为一组.
- 目的是为了细化聚集函数的作用对象.
- 示例: 
  - 求各个课程号及相应的选课人数: `SELECT Cno, COUNT(Sno) FROM SC GROUP BY Cno;`
  - 查询选修了三门以上课程的学生学号: `SELECT Sno FROM SC GROUP BY Sno HAVING COUNT(*) > 3;`

- `WHERE`子句与`HAVING`短语的区别在于作用对象不同.
- `WHERE`子句作用于基本表或视图, 从中选择满足条件的元组.
- `HAVING`短语作用于组, 从中选择满足条件的组.

#### 查询平均成绩大于等于90分的学生学号和平均成绩

- 此例中, `WHERE`子句中不能使用聚集函数作为条件表达式.
- 正确的查询语句应为: 
  ```
  SELECT Sno, AVG(Grade)
  FROM SC
  GROUP BY Sno
  HAVING AVG(Grade) >= 90;
  ```

### 连接查询

- 连接查询指同时涉及两个以上

的表的查询操作.
- 包括等值连接查询, 自然连接查询, 非等值连接查询, 自身连接查询, 外连接查询和复合条件连接查询等.

#### 等值与非等值连接查询

- 连接查询中, 用于连接两个表的条件称为连接条件或连接谓词.
- 连接条件的一般格式为: `<表名1>.<列名1> <比较运算符> <表名2>.<列名2>`
- 比较运算符主要有`=, >, <, >=, <=, !=（或<>）`等.
- 连接条件中的列名称为连接字段.
- 当连接运算符为`=时`, 称为等值连接；使用其他运算符则称为非等值连接.

#### 自身连接

- 连接操作不仅可以在两个表之间进行, 也可以是一个表与自身进行连接, 称为表的自身连接.

#### 查询每门课的间接先修课

- 为了得到每门课的间接先修课（即先修课的先修课）, 需要将Course表与自身进行连接.
- 需要为Course表取两个别名, 一个是FIRST, 另一个是SECOND.
- SQL语句示例: 
  ```
  SELECT FIRST.Cno, SECOND.Cpno
  FROM Course FIRST, Course SECOND
  WHERE FIRST.Cpno = SECOND.Cno;
  ```

3.4.3嵌套查询
在SQL语言中,一个SELECT-FROM-WHERE语句称为一个查询块。将一个查询块嵌 套在另一个查询块的WHERE子句或HAVING短语的条件中的查询称为嵌套查询(nested query)o 例如：
SELECT Sname
FROM Student
WHERE Sno IN
(SELECT Sno
FROM SC
WHERE Cno=* 2 *);
本例中，下层查询块SELECT Sno FROM SC WHERE Cno='2'是嵌套在上层查询块 SELECT Sname FROM Student WHERE Sno IN的WHERE条件中的。上层的査询块称为外 层查询或父查询，下层查询块称为内层查询或子查询。
SQL语言允许多层嵌套査询，即一个子査询中还可以嵌套其他于査询。需要特别指出 的是，子査询的SELECT语句中不能使用ORDER BY子句，ORDER BY子句只能对最终 査询结果排序。
嵌套査询使用户可以用多个简单查询构成复杂的査询，从而增强SQL的查询能力。以 层层嵌套的方式来构造程序正是SQL中“结构化”的含义所在。
1.带有IN谓词的子查询
在嵌套查询中，子查询的结果往往是-个集合，所以谓词IN是嵌套査询中最经常使 用的谓词。 
［例3.55］査询与"刘晨”在同一个系学习的学生。 先分步来完成此查询，然后再构造嵌套查询。
①	确定“刘晨”所在系名
SELECT Sdept
FROM Student
WHERE Sname=，刘晨，； 结果为CS。
②	查找所有在CS系学习的学生。
SELECT Sno,Sname,Sdept
FROM Student
WHERE Sdept=* CS 结果为 .
Sno	Sname	Sdept
201215121	李勇	CS
201215122	刘晨	CS
将第一步查询嵌入到第二步查询的条件中，构造嵌套查询如下：
SELECT Sno,Sname,Sdept	/*例 3.55 的解法一*/
FROM Student
WHERE Sdept IN
(SELECT Sdept
FROM Student
WHERE Sname—刘晨，)；
本例中，子查询的查询条件不依赖于父查询，称为不相关子查询。•种求解方法是由里 向外处理，即先执行子査询，子查询的结果用于建立其父查询的查找条件。得到如下的语句：
SELECT Sno,Sname,Sdept FROM Student
WHERE Sdept IN (CS'); 然后执行该语句。
本例中的査询也可以用自身连接来完成：
SELECT S1 .Sno,S 1 .Sname.S 1 .Sdept	/*例 3.55 的解法:*/
FROM Student S1,Student S2
WHERE Sl.Sdept=S2.Sdept AND S2.Snamc='刘晨'； 
可见，实现同一个查询请求可以有多种方法，当然不同的方法其执行效率可能会有差 别，甚至会差别很大。这就是数据库编程人员应该掌握的数据库性能调优技术，有兴趣的 读者可以参考本章相关文献资料和具体产品的性能调优方法。
［例3.56］查询选修了课程名为“信息系统”的学生学号和姓名。
本查询涉及学号、姓名和课程名三个属性。学号和姓名存放在Student表中，课程名 存放在Course表中，但Student与Course两个表之间没有直接联系，必须通过SC表建立 它们二者之间的联系。所以本查询实际上涉及三个关系。
SELECT Sno^Sname	③ 最后在Student关系中
FROM Student	取出Sno和Sname
WHERE Sno IN	
(SELECT Sno	②然后在SC关系中找出
FROM SC	选修了 3号课程的学生
WHERE Cno IN	学号
(SELECT Cno	①首先在Course关系中
FROM Course	找出“信息系统”的课
WHERE Cname=，信息系统'	程号，结果为3号

)；
本查询同样可以用连接査询实现：
SELECT Student.Sno,Sname
FROM Student,SC,Course
WHERE Student.Sno=SC.Sno AND
SC.Cno=Course.Cno AND
Course.Cname='信息系统'；
有些嵌套查询可以用连接运算替代，有些是不能替代的。从例3.55和例3.56可以看 到，查询涉及多个关系时，用嵌套查询逐步求解层次清楚，易于构造，具有结构化程序设 计的优点。但是相比于连接运算，目前商用关系数据库管理系统对嵌套查询的优化做得还 不够完善，所以在实际应用中，能够用连接运算表达的查询尽可能釆用连接运算。
例3.55和例3.56中子査询的查询条件不依赖于父查询，这类子查询称为不相关子查 询。不相关子查询是较简单的一类子査询。如果子查询的查询条件依赖于父查询，这类子 查询称为相关子查询(correlated subquery),整个查询语句称为相关嵌套查询(correlated nested query) 语句。
例3.57就是一个相关子查询的例子。 

2.带有比较运算符的子查询
带有比较运算符的子查询是指父查询与子查询之间用比较运算符进行连接。当用户能 确切知道内层查询返回的是单个值时，可以用〉、V、=、＞=、v=、！=或＜＞等比较运算符。
例如在例3.55中，由于一个学生只可能在一个系学习，也就是说内查询的结果是一个 值，因此可以用=代替IN：
SELECT Sno,Sname,Sdept	/*例 3.55 的解法三♦/
FROM Student
WHERE Sdept =
(SELECT Sdept
FROM Student
WHERE Sname=，刘晨，)；
［例3.57］找出每个学生超过他自己选修课程平均成绩的课程号。
SELECT Sno,Cno
FROM SC x
WHERE Grade ＞=(SELECT AVG(Grade)	/*某学生的平均成绩*/
FROM SC y
WHERE y.Sno=x.Sno);
x是表SC的别名，又称为元组变量，可以用来表示SC的一个元组。内层查询是求一 个学生所有选修课程平均成绩的，至于是哪个学生的平均成绩要看参数x.Sno的值，而该 值是与父查询相关的，因此这类查询称为相关子查询。
这个语句的一种可能的执行过程采用以下三个步骤。
①	从外层查询中取出SC的一个元组X,将元组x的Sno值(201215121)传送给内层查询。
SELECT AVG(Grade)
FROM SC y
WHERE y.Sno='201215121‘；
②	执行内层查询，得到值88 (近似值)，用该值代替内层查询，得到外层查询：
SELECT Sno, Cno
FROM SC x
WHERE Grade ＞=88;
③	执行这个查询，得到
(201215121,1)
(201215121,3)
然后外层查询取出下一个元组重复做上述①至③步骤的处理，直到外层的SC元组全 部处理完毕。结果为.
(201215121.1)
(201215121,3)
(201215122.2)
求解相关子查询不能像求解不相关子査询那样次将子查询求解出来，然后求解父査 询。内层查询由于与外层查询有关，因此必须反复求值。
3.带有ANY (SOME)或ALL谓词的子查询
子查询返回单值时可以用比较运算符，但返回多值时要用ANY (有的系统用SOME) 或ALL谓词修饰符。而使用ANY或ALL谓词时则必须同时使用比较运算符。其语义如 下所示：
>ANY	大于子查询结果中的某个值
>ALL	大于子查询结果中的所有值
<ANY	小于子査询结果中的某个值
<ALL	小于子查询结果中的所有值
>=ANY	大于等于子查询结果中的某个值
>=ALL	大于等于子査询结果中的所有值
<=ANY	小于等于子査询结果中的某个值
<=ALL	小于等于子查询结果中的所有值
=ANY	等于子查询结果中的某个值
=ALL	等于子查询结果中的所有值(通常没有实际意义)
!=（或v>） ANY	不等于子査询结果中的某个值
!=（或v>） ALL	不等于子査询结果中的任何一个值
［例3.58］查询非计算机科学系中比计算机科学系任意一个学生年龄小的学生姓名和 年龄。
SELECT Sname,Sage
FROM Student
WHERE Sage<ANY （SELECT Sage
FROM Student
WHERE Sdept=' CS *）
AND Sdept o' CS	/*注意这是父查询块中的条件•/
结果如下：
Sname	Sage
王敏	18
张立	19 

关系数据库管理系统执行此查询时，首先处理子查询，找出CS系中所有学生的年龄， 构成一个集合(20,19)；然后处理父查询，找所有不是CS系且年龄小于20或19的学生。
本查询也可以用聚集函数来实现，首先用子查询找出CS系中最大年龄(20),然后在 父查询中查所有非CS系且年龄小于20岁的学生。SQL语句如下：
SELECT Sname,Sage
FROM Student
WHERE Sage <
(SELECT MAX(Sage)
FROM Student
WHERE Sdept=* CS *)
AND Sdept o1 CS *;
［例3.59］查询非计算机科学系中比计算机科学系所有学生年龄都小的学生姓名及年龄。
SELECT Sname,Sage
FROM Student
WHERE Sage < ALL
(SELECT Sage
FROM Student
WHERE Sdept=* CS *)
AND Sdept o * CS
关系数据库管理系统执行此查询时，首先处理子査询，找出CS系中所有学生的年龄， 构成一个集合(20,19)。然后处理父查询，找所有不是CS系且年龄既小于20,也小于19 的学生。查询结果为
Sname	Sage
王敏	18
本查询同样也可以用聚集函数实现。SQL语句如下：
SELECT Sname,Sage
FROM Student
WHERE Sage <
(SELECT MIN(Sage)
FROM Student
WHERE Sdept='CS‘)
AND Sdept o*CS*;
事实上，用聚集函数实现子査询通常比直接用ANY或ALL査询效率要高。ANY、ALL 
与聚集函数的对应关系如表3.7所示。
表3.7 ANY （或SOME）、ALL谓词与聚集函数、IN谓词的等价转换关系
	=	o或!=	<	<=	>	>=
ANY	IN	―	<MAX	<=MAX	>MIN	>=MIN
ALL	—	NOT IN	<MIN	<=M!N	>MAX	>=MAX

表3.7中，=ANY等价于IN谓词，＜ANY等价于＜MAX, oALL等价于NOT IN谓 词，＜ALL等价于＜MIN,等等。
4.带有EXISTS谓词的子查询
EXISTS代表存在量词带有EXISTS谓词的子査询不返回任何数据，只产生逻辑真 值“true”或逻辑假值-falser
可以利用EXISTS来判断xWS、SjR、S=R、SflR非空等是否成立。
［例3.60］査询所有选修了 1号课程的学生姓名。
本査询涉及Student和SC表。可以在Student中依次取每个元组的Sno值，用此值去 检查SC表。若SC中存在这样的元组，其Sno值等于此Student.Sno值，并且其Cno=U, 则取此Student.Sname送入结果表。将此想法写成SQL语句是
SELECT Sname
FROM Student
WHERE EXISTS
（SELECT *
FROM SC
WHERE Sno=Student.Sno AND Cno=T）;
使用存在量词EXISTS后，若内层査询结果非空，则外层的WHERE子句返回真值， 否则返回假值。
由EXISTS引出的子查询，其目标列表达式通常都用*,因为带EXISTS的子查询只 返回真值或假值，给出列名无实际意义。
本例中子查询的査询条件依赖于外层父查询的某个属性值（Student的Sno值），因此 也是相关子查询。这个相关子查询的处理过程是：首先取外层査询中Student表的第一个 元组，根据它与内层査询相关的属性值（Sno值）处理内层查询，若WHERE子句返回值 为真，则取外层查询中该元组的Sname放入结果表；然后再取Student表的下一个元组； 重复这一•过程，直至外层Student表全部检查完为止。
本例中的查询也可以用连接运算来实现，读者可以参照有关的例子自己给出相应的 SQL语句。
与EXISTS谓词相对应的是NOT EXISTS谓词。使用存在量词NOT EXISTS后，若内 

层查询结果为空，则外层的WHERE子句返回真值，否则返回假值。
［例3.61］査询没有选修1号课程的学生姓名。
SELECT Sname
FROM Student
WHERE NOT EXISTS
(SELECT *
FROM SC
WHERE Sno=Student.Sno AND Cno=T);
一些带EXISTS或NOT EXISTS谓词的子查询不能被其他形式的子査询等价替换，但 所有带IN谓词、比较运算符、ANY和ALL谓词的子查询都能用带EXISTS谓词的子查询 等价替换。例如带有IN谓词的例3.55可以用如下带EXISTS谓词的子查询替换：
SELECT Sno,Sname,Sdept	/*例 3.55 的解法四♦/
FROM Student SI
WHERE EXISTS
(SELECT ♦
FROM Student S2
WHERE S2.Sdept=Sl.Sdept AND
S2.Sname=，刘晨)；
由于带EXISTS量词的相关子査询只关心内层查询是否有返回值，并不需要査具体值, 因此其效率并不一定低于不相关子查询，有时是高效的方法。
［例3.62］查询选修了全部课程的学生姓名。
SQL中没有全称量词(forall),但是可以把带有全称量词的谓词转换为等价的带有存 在量词的谓词：
(Vx)P=n (3x(-| P))
由于没有全称量词，可将题目的意思转换成等价的用存在量词的形式：查询这样的学 生，没有一门课程是他不选修的。其SQL语句如下：
SELECT Sname
FROM Student
WHERE NOT EXISTS
(SELECT *
FROM Course
WHERE NOT EXISTS
(SELECT ♦
FROM SC 
WHERE Sno=Student.Sno
AND Cno=Course.Cno));
从而用EXIST/NOT EXIST来实现带全称量词的查询。
［例3.63］查询至少选修了学生201215122选修的全部课程的学生号码。
本查询可以用逻辑蕴涵来表达:查询学号为x的学生，对所有的课程y,只要201215122 学生选修了课程y,则x也选修了 y。形式化表示如下：
用p表示谓词“学生201215122选修了课程y”
用q表示谓词“学生x选修了课程y”
则上述査询为
(Vy) pf q
SQL语言中没有蕴涵(implication)逻辑运算，但是可以利用谓词演算将一个逻辑蕴 涵的谓词等价转换为
pf q— pVq
该查询可以转换为如下等价形式：
(Vy)p—q=-| (3y(n (p—q )))=-］ (3y(i (n pVq)))三 r By(pA-)q)
它所表达的语义为：不存在这样的课程y.学生201215122选修了 y,而学生x没有 选。用SQL语言表示如下：
SELECT DISTINCT Sno
FROM SC SCX
WHERE NOT EXISTS
(SELECT *
FROM SC SCY
WHERE SCY.Sno=' 201215122 1 AND
NOT EXISTS
(SELECT»
FROM SC SCZ
WHERE SCZ.Sno=SCX.Sno AND
SCZ.Cno=SCY.Cno));
3.4.4集合查询
SELECT语句的査询结果是元组的集合，所以多个SELECT语句的结果可进行集合 操作。集合操作主要包括并操作UNION,交操作INTERSECT和差操作EXCEPTo
注意，参加集合操作的各查询结果的列数必须相同；对应项的数据类型也必须相同。
［例3.64］查询计算机科学系的学生及年龄不大于19岁的学生。 
第3 -关系敎招库标冷话，SQL
SELECT *
FROM Student
WHERE Sdept=,CS,
UNION
SELECT *
FROM Student
WHERE Sage<=19;
本査询实际上是求计算机科学系的所有学生与年龄不大于19岁的学生的并集。使用 UNION将多个查询结果合并起来时，系统会自动去掉重复元组。如果要保留重复元组则用 UNION ALL操作符。
［例3.65］查询选修了课程1或者选修了课程2的学生。
本例即査询选修课程1的学生集合与选修课程2的学生集合的并集。
SELECT Sno
FROM SC
WHERE Cno=' 1 '
UNION
SELECT Sno
FROM SC
WHERE Cno=, 2
［例3.66］査询计算机科学系的学生与年龄不大于19岁的学生的交集。
SELECT *
FROM Student
WHERE Sdept=*CS'
INTERSECT
SELECT ♦
FROM Student
WHERE Sage<=19;
这实际上就是查询计算机科学系中年龄不大于19岁的学生。
SELECT ♦
FROM Student
WHERE Sdept=,CS, AND
Sage<=19;
［例3.67］查询既选修了课程1又选修了课程2的学生。就是査询选修课程1的学生 集合与选修课程2的学生集合的交集。 
SELECT Sno
FROM SC
WHERE Cno=' 1 *
INTERSECT
SELECTSno
FROM SC
WHERE Cno='2
本例也可以表示为
SELECT Sno
FROM SC
WHERE Cno=' 1 * AND Sno IN
(SELECT Sno
FROM SC
WHERE Cno=' 2*);
［例3.68］查询计算机科学系的学生与年龄不大于19岁的学生的差集。
SELECT *
FROM Student
WHERE Sdept=,CS,
EXCEPT
SELECT *
FROM Student
WHERE Sage <=19;
也就是查询计算机科学系中年龄大于19岁的学生。
SELECT ♦
FROM Student
WHERE Sdept=,CS, AND Sage>19：
3.4.5基于派生表的查询
子查询不仅可以出现在WHERE子句中，还可以出现在FROM子句中，这时子查询生 成的临时派生表(derived table)成为主查询的査询对象。例如，例3.57找出每个学生超过 他自己选修课程平均成绩的课程号，也可以用如下的查询完成：
SELECT Sno, Cno
FROM SC, (SELECT Sno, Avg(Grade) FROM SC GROUP BY Sno)
AS Avg_sc(avg_sno,avg_grade) 
WHERE SC.Sno = Avg sc.avg sno and SC.Grade ＞= Avg sc.avg grade
这里FROM子句中的子查询将生成一个派生表Avg_sc=该表由avg sno和avg grade 两个属性组成，记录了每个学生的学号及平均成绩。主查询将SC表与Avg_sc按学号相等 进行连接，选出修课成绩大于其平均成绩的课程号。
如果子査询中没有聚集函数，派生表可以不指定属性列，子查询SELECT子句后面的列 名为其默认属性。例如例3.60査询所有选修了 1号课程的学生姓名，可以用如卜•査询完成：
SELECT Sname
FROM Student, (SELECT Sno FROM SC WHERE Cno=' 1 *) AS SCI
WHERE Sludent.Sno=SCl.Sno;
需要说明的是，通过FROM子句生成派生表时，AS关键字可以省略，但必须为派生 关系指定一个别名。而对于基本表，别名是可选择项。
3.4.6 SELECT语句的一般格式
SELECT语句是SQL的核心语句，从前面的例子可以看到其语句成分丰富多样，下面 总结一下它们的一般格式。
SELECT语句的一般格式；
SELECT ［ALLIDISTINCT］〈目标列表达式〉［别名］［,〈目标列表达式〉［别名］〕…
FROM＜表名或视图名〉［别名］［，〈表名或视图名〉［别名］］…| (〈SELECT语句〉)［AS］〈别名〉
［WHERE ＜条件表达式〉］
［GROUP BY〈列名 1＞ ［HAVING ＜条件表达式＞］］
［ORDER BY〈列名 2＞ ［ASC|DESC］］;
1.	目标列表达式的可选格式
(1) *
(2)	v表名〉.*
(3)	COUNT( ［DISTINCT|ALL］ *)
(4)	［〈表名〉.］〈属性列名表达式〉［,［〈表名〉.］〈属性列名表达式＞］…
其中，V属性列名表达式〉可以是由属性列、作用于属性列的聚集函数和常量的任意算术运 算(+, -，♦, /)组成的运算公式。
2.	聚集函数的一般格式
COUNT
SUM
y AVG ＞ ( ［DISTINCT|ALL］〈列名〉)
MAX
MIN
3. WHERE子句的条件表达式的可选格式
(1)
'〈属性列名〉
〈属性列名＞0	〈常量〉
[ANY|ALL] (SELECT 语句)
(2)
	R属性列名〉、		'〈属性列名〉'
〈属性列名〉[NOT] BETWEEN ＜	V常量〉	» ANDY	〈常量〉
	{SELECT 语句）_		（SELECT 语句）-
（3）
'（v值 1＞ [,〈值 2＞] ••■）
〈属性列名〉[NOT] IN «
（SELECT 语句）
（4）	＜属性列名＞ [NOT] LIKE＜匹配串〉
（5）	〈属性列名＞ IS [NOT] NULL
（6）	[NOT] EXISTS （SELECT 语句）
（7）
	AND			AND	
〈条件表达式〉-		•〈条件表达式〉	V		卜〈条件表达式〉…
	OR			QR	丿
