
7.3 概念结构设计

将需求分析得到的用户需求抽象为信息结构（即概念模型）的过程就是概念结构设计。它是整个数据库设计的关键。本节讲解概念模型的特点，以及用E-R模型来表示概念模型的方法。

7.3.1 概念模型

在需求分析阶段所得到的应用需求应

该以应用为中心，将这些需求的主要部分用数据库的数据结构来表达，这些数据结构应该使用户看到一个对他们而言是现实的模型，而不仅仅是由设计人员建立的数据库内部结构。

概念模型是抽象的数据结构，是在需求分析阶段通过对现实世界中的实体、实体之间的关系以及实体属性进行抽象建立的。它描述了用户对数据和其关系的认识。在概念模型中，主要包括三个概念：实体、联系和属性。实体和联系是描述现实世界的基本概念，属性是对实体和联系的描述。

1. 实体

实体是现实世界中一个具体的对象，它在数据库中对应一个实体集。一个实体集可以包含一个或多个实体。每个实体都有唯一的标识符，这个标识符可以是实体本身的属性，也可以是通过其他属性来唯一标识。

2. 联系

联系描述实体之间的关系。联系也可以有属性。联系分为一对一联系、一对多联系和多对多联系三种类型。

3. 属性

属性是实体或联系的特征。属性分为简单属性和复合属性两种类型。简单属性是不能再分的属性，复合属性是由若干简单属性组成的属性。

概念模型的优点是能够直观地表示现实世界的问题，并与用户进行交流和验证。它提供了一个桥梁，使用户和设计人员之间能够就需求达成一致，并作为数据库设计的依据。

7.3.2 E-R模型

E-R模型（Entity-Relationship Model）是一种常用的表示概念模型的方法，它使用图形符号来描述实体、联系和属性之间的关系。E-R模型的图形符号主要包括实体图、联系图和属性图。

1. 实体图

实体图用矩形框表示实体集，框中写上实体集的名字。实体集之间的联系用菱形连线表示，连线上写上联系的类型和联系的名字。

2. 联系图

联系图用菱形表示联系，菱形上写上联系的类型和联系的名字。实体集用矩形表示，框中写上实体集的名字。联系与实体集之间的连接用直线表示。

3. 属性图

属性图用椭圆形表示属性，椭圆形上写上属性的名字和类型。属性与实体集或联系之间的连接用直线表示。

E-R模型通过图形符号和标记来描述现实世界的概念模型，可以直观地表达实体、联系和属性

之间的关系。它是数据库设计中常用的方法，能够帮助设计人员和用户之间更好地理解和沟通需求。

总之，概念结构设计是将用户需求抽象为信息结构的过程，概念模型是概念结构设计的核心，而E-R模型是常用的表示概念模型的方法。概念结构设计的目标是建立一个对用户而言是现实的模型，以满足用户的需求，并为后续的逻辑设计和物理设计提供基础。

7.3.3 扩展的E-R模型

E-R方法是抽象和描述现实世界的有力工具。用E-R图表示的概念模型独立于具体的数据库管理系统所支持的数据模型，是各种数据模型的共同基础，因而比数据模型更一般、更抽象、更接近现实世界。E-R模型得到了广泛的应用，人们在基本E-R模型的基础上进行了某些方面的扩展，使其表达能力更强。

1. ISA联系

用E-R方法构建一个项目的模型时，经常会遇到某些实体型是某个实体型的子类型。例如，研究生和本科生是学生的子类型，学生是父类型。这种父类-子类联系称为ISA联系，表示“is a”的语义。ISA联系用三角形来表示。

ISA联系的一个重要性质是子类继承了父类的所有属性，当然子类也可以有自己的属性。例如，本科生和研究生是学生实体的子类型，他们具有学生实体的全部属性，研究生子实体型还有自己的属性"导师姓名"和"研究方向"。

ISA联系描述了对一个实体型中实体的一种分类方法，下面对分类方法做进一步说明。

2. 基数约束

基数约束是对实体之间一对一、一对多和多对多联系的细化。约束用一个数对min..max表示，如0..1、1..3、1..* (代表无穷大)。min=1的约束叫做强制参与约束，即被施加基数约束的实体型中的每个实体都要参与联系；min=0的约束叫做非强制参与约束，被施加基数约束的实体型中的实体可以出现在联系中，也可以不出现在联系中。

3. Part-of联系

Part-of联系即部分联系，它表明某个实体型是另外一个实体型的一部分。Part-of联系可以分为两种情况：非独占的Part-of联系和独占的Part-of联系。

非独占的Part-of联系表示整体实体如果被破坏，部分实体仍然可以独立存在。例如，汽车和轮子之间的联系就是非独占的Part-of联系。这种联系可以通过基数约束来表达。

独占的Part-of联系表示整体实体如果被破坏，部分实体不能存在。在E-R图中，独占联系可以使用弱实体类型和识别联系来表示。弱实体型是依赖于其他实体

型存在的实体型，而强实体型是独立存在的。弱实体型在E-R图中用双矩形表示，识别联系用双菱形表示。

需要注意的是，由于E-R图的图形元素并没有标准化，不同的教材和不同的构建E-R图的工具软件可能会有一些差异。

综上所述，扩展的E-R模型通过ISA联系、基数约束和Part-of联系等方式，使概念模型更加丰富和准确地描述现实世界的关系。

7.3.4 UML

表示E-R图的方法有若干种，使用统一建模语言UML是其中之一。UML是对象管理组织(Object Management Group, OMG)的一个标准，它提供了模型化和可视化支持的规范语言，适用于软件开发的各个阶段，包括需求规格描述、系统完成后的测试和维护等。UML不仅可以用于数据建模、业务建模和对象建模，还可以用于组件建模等。其中，类图是用UML表示概念模型（即E-R图）的一种方式。

在UML中，类（class）大致对应于E-R图中的实体。类具有面向对象的特征，不仅描述对象的属性，还包含对象的方法。然而，在E-R图中，既没有对象方法的概念，也没有对方法的直接支持。因此，在使用UML表示E-R图时，通常省略了对象方法的说明。

在UML中，实体型（实体）用类来表示，类图中的矩形框表示类，实体名放在上部，下面列出属性名。如果某个属性是实体的码属性，可以在属性后面加上"PK"（表示主键）来表示。

联系在UML中用类图之间的"关联"来表示。早期的UML只能表示二元关联，使用无向边将两个类连接起来，并在连线上方写上关联的名称。现在的UML已经扩展了非二元关联的表示方法，使用菱形框表示关联，框内写上联系名，并使用无向边分别连接关联的类。

基数约束在UML中的表示方式与E-R图中的基数约束类似。使用一个数对（min..max）表示类中的任意一个对象在关联中出现的最少次数和最多次数。例如，0..1、1..3、1..*等。UML中的基数约束标注方法与前面介绍的基数约束标注方法一样。

UML还支持超类-子类的概念，子类可以继承超类的属性，并且可以拥有自己的属性。这与E-R图中的父类-子类联系（或ISA联系）是一致的，因此很容易用UML表示E-R图中的父类-子类联系。

需要注意的是，如果整个计算机应用系统的设计和开发过程都采用了UML规范，开发人员自然可以使用UML对数据进行建模。然而，如果计算机应用系统的设计和开发并未使用UML，则建议在数据库设计中使用E-R模型来表示概念模型。

7.3.5 概念结构设计

在设计E-R图的过程中，概念结构设计是确定实体

与属性之间关系以及解决冲突等关键技术的第一步。概念结构设计的目标是对需求分析阶段收集到的数据进行分类、组织，确定实体、实体属性和实体之间的联系类型，从而形成E-R图。

在确定实体与属性之间的关系时，需要遵循一些原则。事实上，在现实世界中，具体的应用环境通常对实体和属性已经进行了自然的划分。在数据字典中，数据结构、数据流和数据存储都是由若干属性有意义地聚合而成的，这已经体现了实体与属性的划分。因此，可以先从这些内容出发来定义E-R图，然后进行必要的调整。在调整过程中，可以遵循以下原则：

1. 实体与属性的划分原则
   实体与属性之间并没有形式上可以截然划分的界限，因此在划分时需要考虑以下准则：
   - 作为属性的事物不能再具有需要描述的特性，即属性必须是不可分的数据项，不能包含其他属性。
   - 属性不能与其他实体具有联系，即E-R图中所表示的联系是实体之间的联系。
   满足上述准则的事物一般可以作为属性对待。例如，职工是一个实体，职工号、姓名、年龄可以作为职工的属性。如果职称没有与工资、岗位津贴、福利挂钩，即没有需要进一步描述的特性，那么根据准则可以将职称作为职工实体的属性。然而，如果不同的职称有不同的工资、岗位津贴和附加福利，那么将职称作为一个实体更合适。
   在医院中，一个病人只能住在一个病房，病房号可以作为病人实体的一个属性。但是，如果病房还需要与医生实体产生联系，即一个医生负责几个病房的病人的医疗工作，那么根据准则，病房应作为一个实体。
   同样地，如果一种货物只存放在一个仓库中，那么可以将存放货物的仓库号作为描述货物存放地点的属性。但是，如果一种货物可以存放在多个仓库中，或者仓库本身具有面积属性，或者仓库与职工存在管理上的联系，那么将仓库作为一个实体更合适。

2. E-R图的集成
   在开发大型信息系统时，常常采

用自顶向下的策略进行需求分析，然后自底向上地设计概念结构。这意味着首先设计各个子系统的E-R图，然后将它们集成起来形成整体的E-R图。E-R图的集成通常分为两步：
   - 合并：解决各个分E-R图之间的冲突，将它们合并成一个初步的E-R图。
   - 修改和重构：消除不必要的冗余，生成基本的E-R图。
   在合并E-R图的过程中，需要解决各个分E-R图之间的冲突，以形成一个统一的概念模型，能够被全系统中的所有用户理解和接受。这是合并E-R图的关键工作。合并完成后，对E-R图进行修改和重构，消除不必要的冗余，生成基本的E-R图。

以上是关于UML和概念结构设计的基本介绍。

各子系统的E-R图之间的冲突主要分为三类：属性冲突、命名冲突和结构冲突。

1. 属性冲突:
   属性冲突包含两类冲突：
   - 属性域冲突：属性值的类型、取值范围或取值集合不同。例如，零件号在不同部门可能被定义为整数或字符型，不同部门对零件号的编码也不同。另外，年龄也可以有不同的表示方式。
   - 属性取值单位冲突：属性的取值单位不同。例如，零件的重量可能以公斤、斤或克为单位表示。

2. 命名冲突:
   命名冲突包含两类冲突：
   - 同名异义：不同意义的对象在不同的局部应用中具有相同的名称。
   - 异名同义（一义多名）：相同意义的对象在不同的局部应用中具有不同的名称。例如，不同部门对科研项目的称呼可能不同。

3. 结构冲突:
   结构冲突包含三类冲突：
   - 同一对象在不同应用中具有不同的抽象：例如，职工在某一应用中被当作实体，在另一应用中被当作属性。解决方法可以将属性变换为实体或将实体变换为属性，使得对象在不同应用中具有相同的抽象。
   - 同一实体在不同子系统的E-R图中所包含的属性个数和排列次序不同：解决方法是将实体的属性取各子系统E-R图中属性的并集，然后适当调整属性的次序。
   - 实体间的联系在不同E-R图中为不同类型：解决方法是根据应用的语义对实体联系的类型进行综合或调整。

在概念结构设计阶段，需要消除不必要的冗余并设计基本的E-R图。冗余数据是指可以由基本数据导出的数据，冗余联系是指可以由其他联系导出的联系。消除冗余的方法包括分析方法和规范化理论。分析方法是根据数据字典和数据流图中数据项之间的逻辑关系来消除冗余。规范化理论利用函数依赖的概念提供了形式化工具，通过确定函数依赖集合并逐一考察来消除冗余。

以上是关于各子系统E-R图之间冲突的分类和解决方法，以及概念结构设计阶段的冗余消除和基本E-R图设计的介绍。

7.4.2 数据模型的优化

数据库逻辑设计的结果并不是唯一的。为了进一步提高数据库应用系统的性能，还应该根据应用需要适当地修改、调整数据模型的结构，这就是数据模型的优化。关系数据模型的优化通常以规范化理论为指导。

优化的方法包括：

(1) 确定数据依赖：根据需求分析阶段得到的语义，写出每个关系模式内部各属性之间的数据依赖以及不同关系模式属性之间的数据依赖。

(2) 对于各个关系模式之间的数据依赖进行极小化处理，消除冗余的联系。

(3) 按照数据依赖的理论对关系模式逐一进行分析，确定各关系模式分别属于第几范式，检查是否存在部分函数依赖、传递函数依赖、多值依赖等。

(4) 根据需求分析阶段得到的处理要求，分析对于这样的应用环境，确定是否要对某些模式进行合并或分解。

需要注意的是，并不是规范化程度越高的关系就越优。在某些情况下，低范式的关系模型可能更合适，例如查询经常涉及多个关系模式的属性时，系统经常进行连接运算。在这种情况下，第二范式甚至第一范式也许是合适的。

另外，非BCNF的关系模式在实际应用中，如果只执行查询操作而不进行更新操作，可能不会产生实际影响。因此，在具体应用中，需要权衡响应时间和潜在问题两者的利弊来确定规范化的程度。

(5) 对关系模式进行必要的分解，以提高数据操作效率和存储空间利用率。常用的分解方法包括水平分解和垂直分解。

水平分解将关系的元组分为若干子集合，形成子关系，以提高系统的效率。根据"80/20原则”，一个大关系中，经常被使用的数据只是关系的一部分，可以将经常使用的数据分解出来，形成一个子关系。如果关系夫上具有一个事务，而且多数事务存取的数据不相交，则可以将关系分解为少于或等于一个子关系，使每个事务存取的数据对应一个关系。

垂直分解将关系模式的属性分解为若干子集合，形成子关系模式。垂直分解的原则是，将经常在一起使用的

属性从关系中分解出来形成一个子关系模式。垂直分解可以提高某些事务的效率，但也可能使其他事务不得不执行连接操作，从而降低效率。因此，是否进行垂直分解取决于分解后所有事务的总效率是否得到提高。垂直分解需要确保无损连接性和保持函数依赖，即保证分解后的关系具有无损连接性和保持函数依赖性。

7.4.3 设计用户子模式

将概念模型转换为全局逻辑模型后，根据局部应用需求和具体关系数据库管理系统的特点，设计用户的外模式。关系数据库管理系统通常提供视图的概念，可以利用这一功能设计更符合局部用户需求的用户外模式。

定义数据库全局模式主要考虑系统的时间效率、空间效率和易维护性。用户外模式与模式是相对独立的，因此在定义用户外模式时可以注重考虑用户的习惯和方便。具体包括以下几方面：

(1) 使用符合用户习惯的别名。在合并各分E-R图时，消除命名冲突是必要的，使得数据库系统中同一关系和属性具有唯一的名字。通过视图机制，在设计用户视图时可以重新定义某些属性名，使其与用户习惯一致，方便使用。

(2) 可以为不同级别的用户定义不同的视图，以确保系统的安全性。例如，针对关系模式"产品"（产品号、产品名、规格、单价、生产车间、生产负责人、产品成本、产品合格率、质量等级），可以建立以下两个视图：
- 针对一般顾客建立视图"产品1"（产品号、产品名、规格、单价）
- 针对产品销售部门建立视图"产品2"（产品号、产品名、规格、单价、车间、生产负责人）

顾客视图只包含允许顾客查询的属性，销售部门视图只包含允许销售部门查询的属性，而生产领导部门可以查询全部产品数据。这样可以防止用户非法访问不允许查询的数据，确保系统的安全性。

(3) 简化用户对系统的使用。如果某些局部应用中经常需要使用复杂的查询，为了方便用户，可以将这些复杂查询定义为视图，用户每次只需查询已定义好的视图，大大简化了用户的使用过程。

需要注意的是，扩展E-R模型是选读部分，本章没有涉及扩展E-R

图的集成以及向关系模型的转换。

7.5 物理结构设计

数据库在物理设备上的存储结构和存取方法被称为数据库的物理结构，它依赖于所选的数据库管理系统。为给定的逻辑数据模型选择最适合应用要求的物理结构，就是数据库的物理设计。

数据库的物理设计通常分为两个步骤：

(1) 确定数据库的物理结构，包括存取方法和存储结构，在关系数据库中主要指索引方法和聚簇方法。

(2) 对物理结构进行评价，重点考虑时间和空间效率。如果评价结果符合最初的设计要求，则可以进入物理实施阶段；否则，需要重新设计或修改物理结构，有时甚至需要返回逻辑设计阶段修改数据模型。

7.5.1 数据库物理设计的内容和方法

不同的数据库产品提供的物理环境、存取方法和存储结构有很大差异，设计人员可用的设计变量和参数范围也不相同，因此没有通用的物理设计方法可遵循，只能提供一般的设计内容和原则。优化的目标是设计出的物理数据库结构能够使各种事务在数据库上的运行具有较小的响应时间、较高的存储空间利用率和较大的事务吞吐率。

物理设计的第一步是对要运行的事务进行详细分析，获取选择物理数据库设计所需的参数。其次，需要全面了解所使用的关系数据库管理系统的内部特性，尤其是系统提供的存取方法和存储结构。

对于数据库查询事务，需要获得以下信息：

- 查询的关系
- 查询条件所涉及的属性
- 连接条件所涉及的属性
- 查询的投影属性

对于数据更新事务，需要获得以下信息：

- 被更新的关系
- 每个关系上的更新操作条件所涉及的属性
- 修改操作要改变的属性值

此外，还需要了解每个事务在各个关系上的运行频率和性能要求。例如，某个事务必须在10秒内完成，这对存取方法的选择具有重要影响。

以上信息是确定关系的存取方法的依据。需要注意的是，运行在数据库上的事务会不断变化、增加或减少，因此需要根据这些设计信息的变化来调整数据库的物理结构。

通常，关系数据库的物理设计内容主要包括为关系模式选择存取方法，并设计关系和索引等数据库文件的物理存储结构。

下面介绍这些设计内容和方法。

7.5.2 关系模式存

取方法的选择

数据库系统是多用户共享的系统，同一个关系需要建立多条存取路径以满足多个用户的多种应用需求。物理设计的任务之一是根据关系数据库管理系统所支持的存取方法，确定选择哪些存取方法。

存取方法是快速存取数据库中数据的技术，数据库管理系统通常提供多种存取方法。常用的存取方法包括索引方法和聚簇方法。

B+树索引和哈希索引是数据库中经典且广泛使用的存取方法。

1. B+树索引存取方法的选择

选择索引存取方法实际上是确定对关系的哪些属性列建立索引、哪些属性列建立组合索引、哪些索引需要设计为唯一索引等。一般来说：

- 如果一个属性（或一组属性）经常出现在查询条件中，可以考虑在该属性（或属性组）上建立索引（或组合索引）。
- 如果一个属性经常作为最大值和最小值等聚合函数的参数，可以考虑在该属性上建立索引。
- 如果一个属性（或一组属性）经常出现在连接操作的连接条件中，可以考虑在该属性（或属性组）上建立索引。

关系上定义的索引数量并不是越多越好，因为维护索引需要代价，查找索引也需要代价。例如，如果一个关系的更新频率很高，定义在该关系上的索引数量不能太多，因为每次更新关系时都必须相应地修改相关索引。

2. 哈希索引存取方法的选择

选择哈希存取方法的规则如下：如果一个关系的属性主要在等值连接条件或等值比较选择条件中出现，并且满足以下两个条件之一，那么可以选择哈希存取方法：

- 一个关系的大小是可预知且不变的。
- 关系的大小是动态变化的，但数据库管理系统提供了动态哈希存取方法。

3. 聚簇存取方法的选择

为了提高某个属性（或属性组）的查询速度，可以将具有相同值的元组集中存放在连续的物理块中，这称为聚簇。属性（或属性组）被称为聚簇码。聚簇功能可以显著提高按聚簇码进行查询的效率。

选择聚簇存取方法，即确定需要建立多少个聚簇，每个聚簇包含哪些关系。

首先设计候选聚簇，一般来说：

- 对经常一起进行连接操作的关系可以建立聚簇。
- 如果一个关系的一组属性经常出现在相等比较条件中

，可以将该关系作为聚簇。
- 如果一个关系的某个（或一组）属性的值重复率很高，可以将该关系作为聚簇。即平均每个聚簇码值对应的元组数不应过少，以确保聚簇的效果明显。

然后检查候选聚簇中的关系，取消其中不必要的关系：

- 从聚簇中删除经常进行全表扫描的关系。
- 从聚簇中删除更新操作远远多于连接操作的关系。
- 不同的聚簇中可能包含相同的关系，一个关系可以在某个聚簇中，但不能同时加入多个聚簇。需要从多个聚簇方案（包括不建立聚簇）中选择一个较优的，即在该聚簇上运行各种事务的总代价最小。

需要强调的是，聚簇只能提高某些应用的性能，并且建立和维护聚簇的开销相当大。对于已有关系的聚簇建立，会导致关系中元组的物理存储位置发生变化，并使原先建立的所有索引无效，必须重新建立索引。当聚簇码值改变时，相应元组的存储位置也必须相应移动，因此聚簇码值应相对稳定，以减少修改聚簇码值带来的维护开销。

因此，当通过聚簇码进行访问或连接是关系的主要应用，而与聚簇码无关的其他访问很少或者是次要的，此时使用聚簇非常有利，可以省去对结果集的排序操作。否则，可能会适得其反。

7.5.3 确定数据库的存储结构

确定数据库物理结构主要指确定数据的存放位置和存储结构，包括确定关系、索引、聚簇、日志、备份等的存储安排和存储结构，确定系统配置等。确定数据的存放位置和存储结构要综合考虑存取时间、存储空间利用率和维护代价三个方面的因素。这三个方面常常是相互矛盾的，因此需要进行权衡，选择一个折中方案。

1. 确定数据的存放位置

为了提高系统性能，应该根据应用情况将数据的易变部分与稳定部分、经常存取部分和存取频率较低部分分开存放。

例如，目前很多计算机有多个磁盘或磁盘阵列，因此可以将表和索引放在不同的磁盘上，在查询时，由于磁盘驱动器并行工作，可以提高物理I/O读写的效率。也可以将比较大的表分放在两个磁盘上，以加快存取速度，这在多用户环境下特别有效。还可以将日志文件与数据库对象（表、索引等）放在不同的磁盘上，以改进系统的性能。设计人员应仔细了解给定的关系数据库管理系统提供的方法和参数，针对应用环境的要求对数据进行适当的物理安排。

2. 确定系统配置

关系数据库管理系统产品一般都提供了一些系统配置变量和存储分配参数，供设计人员和数据库管理员对数据库进行物理优化。初始情况下，系统都为这些变量赋予了合理的默认值。但是这些值不一定适合每一种应用环境，在进行物理设计时需要重新对这些变量赋值，以改善系统的性能。

系统配置变量很多，例如同时使用数据库的用户数，同时打开的数据库对象数，内存分配参数，缓冲区分配参数（使用的缓冲区长度、个数），存储分配参数，物理块的大小，物理块装填因子，时间片大小，数据库大小，锁的数目等。这些参数值影响存取时间和存储空间的分配，在物理设计时就要根据应用环境确定这些参数值，以使系统性能最佳。

在物理设计时对系统配置变量的调整只是初步的，在系统运行时还要根据系统实际运行情况做进一步的调整，以期切实改进系统性能。

7.5.4 评价物理结构

数据库物理设计过程中需要

对时间效率、空间效率、维护代价和各种用户要求进行权衡，其结果可以产生多种方案。数据库设计人员必须对这些方案进行细致的评价，从中选择一个较优的方案作为数据库的物理结构。

评价物理数据库的方法完全依赖于所选用的关系数据库管理系统，主要是从定量估算各种方案的存储空间、存取时间和维护代价入手，对估算结果进行权衡、比较，选择出一个较优的、合理的物理结构。如果该结构不符合用户需求，则需要修改设计。

7.6 数据库的实施和维护

完成数据库的物理设计之后，设计人员就要用关系数据库管理系统提供的数据定义语言和其他实用程序将数据库逻辑设计和物理设计结果严格描述出来，成为关系数据库管理系统可以接受的源代码，再经过调试产生目标模式，然后就可以组织数据入库了，这就是数据库实施阶段。

7.6.1 数据的载入和应用程序的调试

数据库实施阶段包括两项重要的工作，一项是数据的载入，另一项是应用程序的编码和调试。

一般数据库系统中数据量都很大，而且数据来源于部门中的各个不同的单位，数据的组织方式、结构和格式都与新设计的数据库系统有相当的差距。组织数据载入就要将各类源数据从各个局部应用中抽取出来，输入计算机，再分类转换，最后综合成符合新设计的数据库结构的形式，输入数据库。因此，这样的数据转换、组织入库的工作是相当费力、费时的。

特别是原系统是手工数据处理系统时，各类数据分散在各种不同的原始表格、凭证、单据之中。在向新的数据库系统中输入数据时还要处理大量的纸质文件，工作量就更大。

为提高数据输入工作的效率和质量，应该针对具体的应用环境设计一个数据录入子系统，由计算机来完成数据入库的任务。在源数据入库之前要采用多种方法对其进行检验，以防止不正确的数据入库，这部分的工作在整个数据输入子系统中是非常重要的。

现有的关系数据库管理系统一般都提供不同关系数据库管理系统之间数据转换的工具，若原来是数据库系统，就要充分利用新系统的数据转换工具。

数据库应用程序的设计应该与数据库设计同时进行，因此在组织数据入库的同时还要调试应用程序。应用程序的设计、编码和调试

的方法、步骤在软件工程等课程中有详细讲解，这里就不再赘述了。

7.6.2 数据库的试运行

在原有系统的数据有一小部分已输入数据库后，就可以开始对数据库系统进行联合调试了，这又称为数据库的试运行。

这一阶段要实际运行数据库应用程序，执行对数据库的各种操作，测试应用程序的功能是否满足设计要求。如果不满足，对应用程序部分则要修改、调整，直到达到设计要求为止。

在数据库试运行时，还要测试系统的性能指标，分析其是否达到设计目标。在对数据库进行物理设计时已初步确定了系统的物理参数值，但一般情况下，设计时的考虑在许多方面只是近似估计，和实际系统运行总有一定的差距，因此必须在试运行阶段实际测量和评价系统性能指标。事实上，有些参数的最佳值往往是经过运行调试后找到的。如果测试的结果与设计目标不符，则要返回物理设计阶段重新调整物理结构，修改系统参数，某些情况下甚至要返回逻辑设计阶段修改逻辑结构。

这里特别要强调两点。第一，上面已经讲到组织数据入库是十分费时、费力的事，如果试运行后还要修改数据库的设计，还要重新组织数据入库。因此应分期分批地组织数据入库，先输入小批量数据做调试用，待试运行基本合格后再大批量输入数据，逐步增加数据量，逐步完成运行评价。第二，在数据库试运行阶段，由于系统还不稳定，硬、软件故障随时都可能发生；而系统的操作人员对新系统还不熟悉，误操作也不可避免，因此要做好数据库的转储和恢复工作。一旦故障发生，能使数据库尽快恢复，尽量减少对数据库的破坏。

7.6.3 数据库的运行和维护

数据库试运行合格后，数据库开发工作就基本完成，可以投入正式运行了。但是由于应用环境在不断变化，数据库运行过程中物理存储也会不断变化，对数据库设计进行评价、调整、修改等维护工作是一个长期的任务，也是设计工作的继续和提高。

在数据库运行阶段，对数据库经常性的维护工作主要是由数据库管理员完成的。数据库的维护工作主要包括以下几方面。



1. 数据库的转储和恢复

数据库的转储和恢复是系统正式运行后最重要的维护工作之一。数据库管理员要针对不同的应用要求制定不同的转储计划，以保证一旦发生故障能尽快将数据库恢复到某种一致的状态，并尽可能减少对数据库的破坏。

2. 数据库的安全性、完整性控制

在数据库运行过程中，由于应用环境的变化，对安全性的要求也会发生变化，比如有的数据原来是机密的，现在则可以公开查询，而新加入的数据又可能是机密的。系统中用户的密级也会改变。这些都需要数据库管理员根据实际情况修改原有的安全性控制。同样，数据库的完整性约束条件也会变化，也需要数据库管理员不断修正，以满足用户要求。

3. 数据库性能的监督、分析和改造

在数据库运行过程中，监督系统运行，对监测数据进行分析，找出改进系统性能的方法是数据库管理员的又一重要任务。目前有些关系数据库管理系统提供了监测系统性能参数的工具，数据库管理员可以利用这些工具方便地得到系统运行过程中一系列性能参数的值。数据库管理员应仔细分析这些数据，判断当前系统运行状况是否为最佳，应当做哪些改进，例如调整系统物理参数或对数据库进行重组织或重构造等。

4. 数据库的重组织与重构造

数据库运行一段时间后，由于记录不断增删改，将会使数据库的物理存储情况变坏，降低数据的存取效率，使数据库性能不断降低，这时数据库管理员就要对数据库进行重组织或部分重组织（只对频繁增删的表进行重组织）。关系数据库管理系统通常都提供数据重组织用的实用程序。在重组织的过程中，按原设计要求重新安排存储位置、回收垃圾、减少指针链等，提高系统性能。

数据库的重组织并不修改原设计的逻辑和物理结构，而数据库的重构造则不同，它是指部分修改数据库的模式和内模式。由于数据库应用环境发生变化，增加了新的应用或新的实体，取消了某些应用，有的实体与实体间的联系也发生了变化等，使原有的数据库设计不能满足新的需求，需要调整数据库的模式和内模式。例如，在表中增加或删除某些数据项，改变数据项的类型，增加

或删除某个表，改变数据库的容量，增加或删除某些索引等。当然，数据库的重构也是有限的，只能做部分修改。如果应用变化太大，重构也无济于事，说明此数据库应用系统的生命周期已经结束，应该设计新的数据库应用系统了。

7.7 结束

本章主要讨论数据库设计的方法和步骤，列举了较多的实例，详细介绍了数据库设计各个阶段的目标、方法以及应注意的事项，其中重点是概念结构的设计和逻辑结构的设计，这也是数据库设计过程中最重要的两个环节。

概念结构的设计着重介绍了E-R模型的基本概念和图示方法。应重点掌握实体型、属性和联系的概念，理解实体型之间的一对一、一对多和多对多联系，掌握E-R模型的设计以及把E-R模型转换为关系模型的方法。

学习本章要努力掌握书中讨论的基本方法，还要能在实际工作中运用这些思想设计符合应用需求的数据库模式和数据库应用系统。
