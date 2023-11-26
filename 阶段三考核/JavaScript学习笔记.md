### 1. JavaScript是什么？

- JavaScript是一种轻量级的脚本语言，用于网页开发，可为网页添加交互性。
- 它是一种高级语言，运行在客户端浏览器上。
- JavaScript与Java没有直接关系，尽管名字相似，但它们是完全不同的语言。

### 2. JavaScript的用途

- 提供网页交互性：控制HTML元素、处理用户交互、表单验证等。
- 创建动态内容：根据用户行为改变页面内容。
- 开发Web应用程序：如游戏、动态图表等。

### 3. JavaScript基本语法

#### 变量和数据类型

- **变量声明**

- ```javascript
  var x = 5; // 声明一个变量x并赋值为5
  let y = "Hello"; // 使用let声明变量（ES6新增）
  const PI = 3.14; // 使用const声明常量
  
  ```

- ```javascript
  一个变量x并赋值为5
  let y = "Hello"; // 使用let声明变量（ES6新增）
  const PI = 3.14; // 使用const声明常量
  ```

- **数据类型**

  - **基本数据类型：**
    - 字符串（String）
    - 数字（Number）
    - 布尔（Boolean）
    - Null
    - Undefined
  - **复杂数据类型：**
    - 对象（Object）
    - 数组（Array）

#### 运算符和表达式

- **算术运算符**

  ```javascript
  javascriptvar sum = 5 + 10;
  ```

- **逻辑运算符**

  ```
  javascriptvar isTrue = (10 > 5) && (5 < 3); // && 表示逻辑与
  ```

- **条件语句**

  ```javascript
  javascriptif (condition) {
    // 如果条件为真，执行这里的代码
  } else {
    // 如果条件为假，执行这里的代码
  }
  ```

- **循环语句**

  ```javascript
  javascriptfor (var i = 0; i < 5; i++) {
    // 循环执行的代码
  }
  ```

#### 函数

- **函数声明和调用**

  ```javascript
  javascriptfunction greet(name) {
    return "Hello, " + name + "!";
  }
  
  var greeting = greet("Alice");
  console.log(greeting);
  ```

- **函数参数和返回值**

  - 函数可以接受参数并返回一个值。

### 4. JavaScript与HTML/CSS的关系

- **HTML（结构）**
  - HTML定义了网页的结构，表示内容。
- **CSS（样式）**
  - CSS负责网页的外观和样式。
- **JavaScript（行为）**
  - JavaScript用于处理网页的行为和交互性。