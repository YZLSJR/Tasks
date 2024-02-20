# 一.查询数据类型

`type=("")`变量无类型查的是数据类型语句有返回值便可以被赋值 `name1=type(name)`

# 二.数据类型转换

|   语句   |     说明      |
| :------: | :-----------: |
|  int(x)  |  将x转成整数  |
| float(x) | 将X转成浮点数 |
|  str(x)  | 将x转成字符串 |

# 三.标识符

数字不可以作为开头

# 四.字符串拼接

1. 字符串用加号拼接，不能和其它类型用加号拼接

   ```python
   print("我是"+"黑马")
   ```

2. 占位式拼接(可以不同类型)

   ```python
   name = 999
   message = "两人%s" % name
   print(message)
   ```

   多变量占位，变量要用括号括起来，并按占位顺序填入

   ```python
   i = 2
   t = 3
   a = "我%s岁了，他%s岁了" % (i,t)
   print(message)
   ```


| 符号 |      转化      |
| :--: | :------------: |
|  %s  | 转为字符串放入 |
|  %d  |  转为整数放入  |
|  %f  | 转为浮点数放入 |

3. 精度控制

   - **.n**控制小数点精度（==**同时会对小数部分进行四舍五入**==）
   - **m**控制宽度（m若比数字本身宽度还小，则不生效）

   例：对11.35设置了**%7.2f**后，结果是：**\[空格][空格]11.35**,两空格补足宽度。

4. 快速字符串格式化 

   **语法：f"内容{要拼接的变量}"**

   ```python
   a=1
   b=4.66
   print(f"我{a}岁了，他{b}岁了")
   ```

   ==**但数字变量不做精度控制，原样输出**==

5. 表达式格式化

   表达式：一条具有明确执行结果的代码语句

   ```python
   print("1 * 1的结果是:%d" % (1 * 1))
   ```

# 六.input语句

input("提示语句")

input中不管输入什么都视为字符串

# 七.随机数

random

```python
import random
num = random.randint(1,10)
```

# 八.for循环(遍历循环，依次取出)

```python
name = yangziliang 
for x in name:
    print(x)
    
```

​	将name中的内容，挨个取出赋予x临时变量
​	就可以在循环体内对x进行处理

# 九.range

`range(num)`获得一个数字序列从0开始，不含num
`range(num1,num2)`获得一个数字序列不含num2
`range(num1,num2,step)`获得一个数字序列不含num2,且数字之间的步长，以step为准，默认step为1

# 十.continue

中断本次循环，直接进入下一次

```python
for i in range(1,100):
    语句一
    continue
    语句二
```

上面代码中语句二不会执行

# 十一.break

跳出所在循环

# 十二.函数

## 1.函数的定义

```python
def 函数名 (传入参数)：
	函数体
    return 返回值
```

## 2.函数的调用

函数名(参数)

## 3.传入参数

功能：在函数进行计算时，接受外部（调用时）提供的数据

```python
def add(x,y):
    result = x + y
    print(f"{x} + {y}的结果是：{result}")
add(5,6)
```

* `def add(x, y)`中x和y称为形参，表示函数声明将要使用两个参数
  * 参数之间用逗号隔开
* 函数调用中提供的5和6称为实参，表明函数执行时真正使用的参数值

## 4.返回值

语法：

```python
def 函数名(参数···):
    函数体
    return 返回值
变量 = 函数(参数)
```

写不写return,函数都有返回值，不写的时候返回None

* None用在if判断中，None等同于False

* 用于声明无内容的变量上

  定义变量但暂时不需要变量有具体值，可以用None来代替

  ```python
  name = None
  ```

## 5.函数说明文档

```python
def add(x y):
    """
    函数功能····
    :param x:表示
    :param y:表示
    :return:
    """
```

将鼠标悬停在函数名或者参数上可以看到说明文档

## 6.变量作用域

两类：局部变量和全局变量

* 局部变量指定义在函数体内部的变量，只在函数体内部生效，在函数体内使用完便会销毁，无法在函数体外发挥作用
* 全局变量，函数体内外都可生效，定义在函数体外即可

**如何在函数体内修改全局变量**

* **答：在函数体内写上`global 要修改的全局变量`**

# 数据容器

## 1.列表

1. 

* `变量名称 = [元素一，元素二，元素三······]`

* 空列表
  `变量名称 = []`
  `变量名称 = list()`

列表可以一次存储多个数据，**且可以为不同的数据类型，==支持嵌套==**

2. 列表下标

   * 正向从0开始，反向从-1开始

   * 嵌套下标

     ```python
     list1 = [[1,2,3],[4,5,6]]
     # 输出5的格式为
     print(list1[1][1])
     ```

3. 方法

   将函数定义为clss(类)的成员，那函数会称之为：方法

   ```python
   # 函数
   def add(x,y):
       return x + y
   ```

   ```python
   # 方法
   class Sudent:
       def add(self,x,y):
           return x + y
   ```

   方法的使用

   ```python
   student = student()
   num = student.add(1,2)
   ```

5. ==**列表的常用操作**==

   * 查找某元素的下标索引（正向）

     语法：**列表.index(元素)**

   * 修改特定位置的元素值

     语法：**列表[下标]=值**

   * 插入元素

     语法：**列表.insert(下标，元素)**，在指定的下标位置（插入后元素要代替的位置）插入指定元素

   * 追加元素（追加到队尾）

     * 语法1：列表.append(元素)
     * 语法2：列表.extend（其他数据容器），将其他数据容器中的内容追加到列表尾部

   * 删除元素

     * 语法1：del列表[下标]
     * 语法2：列表.pop(下标)，将元素提出来并将其从列表中剔除，并可以将剔除元素接收
     * 语法3：列表.remove(元素)，删除某元素在列表中的第一个匹配项（从前到后寻找第一个符合的元素并删除）

   * 清空元素

     语法：列表.clear()

   * 统计某元素在列表中的数量

     语法：列表.count(元素)

   * 列表内有多少元素

     语法：len.(列表)

6. 列表的遍历

   * while

   ```python
   index = 0
   while index < len(列表):
       元素 = 列表[index]
       对元素进行处理
       index += 1
   ```

   * for

     ```python
     for 临时变量 in 数据容器:
         对临时变量进行处理
     ```

## 2.元组

1. 定义

   变量名称 = （元素，元素，······）

   空元组

   变量名称 = （）

   变量名称 = tuple()

   **注：定义单个元素必须加一个逗号**

2. 嵌套

   ```python
   t = ((1,2,3),(4,5,6))
   # 将4取出
   t4 = t[1][0] 
   ```

3. 元组操作

   查找    `元组名.index（）`

   统计某个数据出现的次数    `元组名.count()`

   统计元素个数    `len(元组)`

4. 修改元组内容

   正常来说不可修改

   **元组内嵌套list可以被修改**

## 3.字符串

同样不可修改

* 查找     名称.index()  (若查找多个，查找到的是起始下标)

* 替换
  语法：==**字符串.replace(字符串1，字符串2)**==
  功能：将字符串内的全部：字符串1，替换为字符串2
  注：是得到了一个新字符串，可以被接收

* 字符串的分割

  语法：==**字符串.split(分隔符字符串)**==
  功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
  注意：字符串本身不变，而是得到了一个列表对象

* 字符串的规整操作

  （1）去首尾空格及换行符
  		语法：字符串.strip()

  ```python
  my_str = "  itheima  "
  print(my_str.strip("12")) # 结果："itheima"
  ```

  （2）去前后指定字符串

  ​		语法：字符串.strip(字符串)

  ```python
  my_str = "12itheima21"
  print(my_str.strip("12")) # 结果："itheima"
  ```

* 统计

  **名称.count()**

* 长度(包括空格)

  名称.len()

## 4.序列

* 切片（不会影响原本）
  语法：序列[起始下标：结束下标：步长]
  不包含结束下标，步长若为负，则从后往前
  特殊：

  ```python
  my_str = "123456"
  result = my_str[::-1]
  ```

  等同于将序列反转

  ```python
  my_str = "万过薪月，员序程马黑来，nohtyp学"
  # 得到黑马程序员
  result = my_str.split("，")[1].replace("来","")[::-1]
  ```


## 5.集合(不支持下标索引)

* 变量名={元素，元素···}

* 空集合=set()

* 操作：

  * 添加元素：名称.add()

  * 删除元素：名称.remove()

  * 随机取出一个元素（原本元素被删除）：名称.pop()

  * 清空：名称.clear（）

  * 取两个集合的差集：语法：集合1.diffience(集合2)    集合1为基准，取出集合1里有而集合2里没有的元素，集合1，2不发生变化

    ```python
    set1 = {1,2,3}
    set2 = {1,5,6}
    set3 = set1.diffience(set2)
    ```

  * 消除两个元素的差集 

    语法：集合1.diffience_update(集合2)

    功能：对比集合1和集合2，在集合1内，删除和集合2相同的元素

    结果：集合1被修改，集合2不变

  * 集合合并

    语法：集合1.unior（集合2）

    功能：将集合1和集合2合成新集合

    结果：原集合1，2不变，得到新集合

  * len（集合），求不重复元素个数



## 字典(不支持下标索引)

1. 语法

```python
my_dict = {key:value,key:value······}
```

空字典：

`my_dict = {}`

`my_dict = dict()`

2. 嵌套

   ```python
   my_dict = {
       "某1"：{
           "语文":77,
           "数学":88,
           "英语":99
       },
       "某2":{
           "语文":66,
           "数学":55,
           "英语":33
       }
   }
   ```

   若要查询某1的语文成绩

   ```python
   my_dict["某1"]["语文"]
   ```

   3. 操作

      * 新增元素

        字典[key] = value

        注：字典key不可重复，对已存在的key操作则会覆盖原有值

      * 删除元素

        字典.pop(key),结果：获得指定key的value，同时删除他

      * 清空元素

        字典.clear()

      * 获取全部的key

        字典.keys()

      * 字典内key的个数

        len()


## 数据容器通用操作

* max（容器），统计容器内最大元素
* min（容器），统计容器内最小元素
* 转换功能
  * list（容器） 转列表
  * tuple（容器） 转元组
  * str（容器） 转字符串
  * set（容器） 转集合

* 字典转字符串可以保留value

* 定容器排序功能（结果会转成列表）（a比A大）
  * sorted（容器，[reverse=Ture]）默认为false

# 函数进阶

## 多返回值

```python
def return2():
    return 1,2
x,y = return2()
print(x)
print(y)
```

## 传参

* 位置传参

  按顺序传参

* 关键字传参

  “键=值”形式传参，可以不按顺序

  注：函数调用时，如果有位置参数，位置参数必须在关键字参数之前

* 缺省参数

  在定义函数时直接为参数提供默认值**（必须都在最后）**，调用时若不传参数则使用缺省参数对应的值

  ```python
  def user_info(mame,age,gender='男')
  ```

* 不定长传参类型

  * 位置不定长传参

    \* 号

    ```python
    def user-info(*args):
        print(args)
    ```

    传进去的所有参数都会被args变量收集，他会根据传进参数的位置合并为一个元组，这就是位置传递

  * 关键字不定长传参

    以\** 标记一个形式参数，以字典的形式接收参数，形式参数一般命名为kwargs

## 匿名函数

* 函数作为参数传递

  与普通函数不同的是，确定的数据相同而计算这几个数据的逻辑不同，我们要传入的是一个计算逻辑

* lambda匿名函数

  * lambda关键字可以定义匿名的函数（无名称）

    只可临时使用一次

  * 语法：lambda  传入参数：函数体（只能一行代码）

# 文件操作

## 文件的编码

将内容翻译为二进制

密码本默认为UTF-8

## 文件的读取

* open函数（打开一个已经存在的文件或者创建一个新文件）  

  语法：（文件对象名）= open(name,mode,encoding)

  name:是要打开的目标文件名的字符串（可以包含文件所在的具体路径）。

  mode：设置打开文件的模式：只读，写入，追加等

  | 模式 |                             描述                             |
  | :--: | :----------------------------------------------------------: |
  |  r   |                  以只读方式打开文件（默认）                  |
  |  w   | 打开一个文件只用于写入，如果该文件已存在则打开并从头开始编辑，删除原有内容；如果该文件不存在，创建新文件 |
  |  a   | 打开一个文件用于追加。如果该文件已存在，新内容将会被写入到已有内容之后；如果该文件不存在，创建新文件进行写入 |

  encoding（用关键字传参）：编码格式（推荐UTF-8）

* 读相关方法

  * read()方法
  
    文件对象.read(num)
  
    num表示要从文件中读取的数据的长度（单位是字节），如果没有传入num,那么就表示读取文件中所有数据
  
  * readlines（）方法
  
    readlines可以按照行的方式把文件的内容进行一次性读取，并且返回的是一个列表，每一行的数据为一个元素
  
  注：如果调用多个read，下一次read会从上一次结尾处开始
  
  * readline（）方法
  
    一次读取一行内容
  
  * 遍历readline
  
    ```python
    for i in 文件对象名:
        对列表内元素的操作
    ```
  
  * 文件的关闭
  
    文件对象名.close（）
  
  * ```python
    with open(name,mode,encoding) as 文件对象名:
        对文件的操作
    ```
  
    执行完`with open`中的操作后自动关闭文件

## 文件的写入

* 文件写入

  文件对象名.write(内容)

* 内容刷新

  文件对象名.flush()

* 文件的关闭

  文件对象名.close()

  注：close中包含flush功能

* 注意：若文件不存在，则创建新文件；若存在，则删除原内容再进行写入

## 文件的追加

a模式

* 文件写入

  文件对象名.write(内容)

* 内容刷新

  文件对象名.flush()

* 文件的关闭

  文件对象名.close()

# python异常，模块与包

## 捕获常规异常

语法：

```python
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
```

## 捕获指定异常

基本语法：

```python
try:
    print(name)
except NameError as e:
    print('name变量名称未定义错误')
```

注：

1. 如果尝试执行的代码异常类型和要捕获的异常类型不一致，则无法捕获异常

2. 一般try下方只放一行尝试执行的代码

## 捕获多个异常

把要捕获的异常类型的名字，放到except后，并使用元组的方式进行书写

```python
try:
   ...
except (NameError,ZeroDivisionError) as e:
    print('...')
```

## 捕获所有异常

```python
try:
   ...
except Exception as e:
    print('...')
```

## else

```python
try:
   ...
except Exception as e:
    print('...')
else:
    没有异常就执行这个
```

## finally

```python
try:
   ...
except Exception as e:
    print('...')
else:
    没有异常就执行这个
finally:
    无论是否异常都执行
```

## python模块

> 基础语法1：
>
> import 模块名
>
> import 模块名1，模块名2
>
> 模块名.功能名（）

> 基础语法2：
>
> from 模块名 import 功能名
>
> 使用时就可以只写功能名，不用写.了
>
> from 模块名 import *
>
> *表示全部的意思
>
> 也不用写.了

> as改别名
>
> import 模块名 as 别名
>
> from 模块名 import 功能名 as 别名

## 自定义模块

main变量

模块调试的时候会执行，从其他文件调用的时候不执行

all变量

在使用*的时候会受到all变量的限制

## python包

文件夹

必须有—init—.py这个文件

调用时

import 包名.模块名

# 对象

设计类

```python
class Student:
    name = None
    gender = None
    nationality = None
    age = None
    
    def say_hi(self):
        print(f"Hi大家好，我是{self.name}")
```

class 类名称：
		类的属性（定义在类中的变量，即成员变量）
		类的行为（定义在类中的函数，成员方法）

```python
def 方法名(self,形参1，····，形参N):
    方法体
```

self在成员方法定义的时候，必须填写

* 它用来表示类对象自身的意思
* 当我们使用类对象调用方法的时候，self会被python传入
* 在方法内部，想要访问类的成员变量，必须使用self

创建一个对象

```python
stu_1.name = "······"
stu_1.gender = "·······"
```

对象 = 类名称

打印出来

```python
print(stu_1.name)
```

## 类的构造方法

_ \_init_ \_

```python
class Student:
	def __init__(self,name,age,tel):
    	self.name = name
   		self.age = age
    	self.tel = tel  /*既有赋值的功能，又有定义的功能*/
stu = Student("杨",18,"18264898985")
print(stu.name)
```

## 私有成员

在成员变量或成员方法前添加两个下划线

私有成员只能被类中的其他成员访问

# 爬取

开始的起点

```python
if __name__ =="__main__":
```

各种库的使用

bs4：网页解析，获取数据
re：正则表达式，进行文字匹配
urllib:制定URL，获取网页数据

```python
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode('utf-8')) #对获取到的网页源码进行utf-8 解码
```

xlwt：进行excel操作
sqlite3：进行SQLite数据库操作

步骤

1. 爬取网页

   超时处理

   ```python
   try:
       response = urllib.request.urlopen("网址",timeout = 时间)
       print(response.read().decode('utf-8'))
   except 异常名 as e:
       print("time out!")
   ```

   我们如果不对我们的请求对象进行一点封装的话，我们用户代理信息就会直接显示Python/urllib，显而易见我们就是爬虫，一些网站就会直接拒绝我们的请求，所以要对请求对象进行封装

   ```python
   url = "https://www.douban.com"
   headers = {"User-Agent":
   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"}
   req = urllib.request.Request(url=url,headers=headers)
   response = urllib.request.urlopen(req)
   print(response.read().decode("utf-8"))
   ```

   

2. 解析数据

3. 保存数据

## bs4

```python
bs = BeautifulSoup(要解析的文件名，"html.parser（也可以解析其他类型像js什么的）")
print(bs.标签名)
# 打印出来包含标签，只能拿到她找到的第一个标签内容
print(bs.标签名.string)
# 得到的内容不含标签 
print(bs.head.contents)
# 遍历，得到一个列表，可以用下标获取
print(bs.head.contents[1])
list = bs.find_all("a")
# 获得所有a标签
list = bs.find_all(re.compile("a")
# 使用正则表达式搜索，所有含a字样的标签及其内容
list = bs.select('title')
# css选择器，，通过标签来查找
list = bs.select(".类名")
list = bs.select("a[class='']")
# 通过属性来查找
list = bs.select("head > title")
# 通过子标签查找
list = bs.select(".类 ~ .类")
# 兄弟标签  
```

## re

| 操作符 |              说明               |                   实例                   |
| :----: | :-----------------------------: | :--------------------------------------: |
|   .    |        表示任何单个字符         |                                          |
|  [ ]   | 字符集，对单个字符给出取值范围  |   [abc]表示a,b,c,[a-z]表示a到z单个字符   |
|  [^ ]  | 字符集，对单个字符给出排除范围  |      [^abc]表示非a或b或c的单个字符       |
|   *    |   前一个字符零次或无限次扩展    |         abc*表示ab，abc，abcc等          |
|   +    |    前一个字符1次或无限次扩展    |        abc+表示abc，abcc，abccc等        |
|   ？   |     前一个字符0次或1次扩展      |                                          |
|   \|   |       左右表达式任意一个        |           abc\|def表示abc或def           |
|  {m}   |        扩展前一个字符n次        |                                          |
| {m，n} |  扩展前一个字符m至n次（含n次）  |                                          |
|   ^    |         匹配字符串开头          |     ^abc表示abc且在一个字符串的开头      |
|   $    |         匹配字符串结尾          |     abc$表示abc且在一个字符串的结尾      |
| （ ）  | 分组标记，内部只能使用\|操作符  | （abc）表示abc，（abc\|def）表示abc，def |
|   \d   |        数字，等价于[0-9]        |                                          |
|   \w   | 单词字符，等价于[A-Z,a-z,0-9,_] |                                          |

| 修饰符 |             描述              |
| :----: | :---------------------------: |
|  re.I  |     使匹配对大小写不敏感      |
|  re.S  | 使.匹配包括换行在内的所有字符 |

  `m = re.search("规则"，"被检验的字符串")`

`re.findall("规则(可以是表达式)"，"模板")`

re.sub("a","A","abcdAfg")找到a用A替换，在第三个字符串中查找

建议在被替换字符串前加一个r防止\无法正常显示

## xlwt

```python
workbook = xlwt.Workbook(encoding="utf-8")	# 创建一个文件，编码格式为utf-8
worksheet = workbook.add_sheet('sheet1')	# 创建工作表
worksheet.write(0,0,'hello')	# 数据写入，第一个参数“行”，第二个参数“列”，第三个为内容
workbook.save('student.xls')	# 保存数据表
```

