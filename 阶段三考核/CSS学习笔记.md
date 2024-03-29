# 一.CSS简介

书写位置：**title标签下方添加style双标签**，style标签里面书写css代码

注释：`/*  */`

写法：选择器{CSS  属性}

```html
<style>
    p{
        /*文字颜色*/
        color:red;
        /*字号*/
        font-size:30px;
    }
</style>
```

# 二.CSS引入方式

* 内部样式表：见一

* 外部样式表：

  * CSS代码写在单独文件中

  * 在HTML使用`link`标签引入

    ```html
    <link rel="stylesheet"href="引入文件地址">
    ```

* 行内样式：配合JavaScript使用

  * CSS写在标签的style属性值里

    ```html
    <div style="color:red; font-size:30px;">这是div标签</div>
    ```

# 三.选择器

标签选择器：使用标签名作为选择器，无差异化

类选择器：差异化设置标签的显示效果

步骤：

* 定义类选择器--->.类名

* 使用类选择器---->标签添加class="类名"

  ```html
  <style>
      .red{
          color:red;
      }
      .size{
          font-size:20px;
      }
  </style>
  <div class="red size">这是div标签</div>
  /*一个标签可以使用多个类名*/
  ```


## id选择器

定义id选择器：#id名{···}

使用时，标签名添加**id="id名"**

同一个id标签一个页面只能用一次

## 通配符选择器

```css
*{color:red;}
```

查找页面所有标签，设置相同样式，不需要调用

# 画盒子

|      属性名      |  作用  |
| :--------------: | :----: |
|      width       |  宽度  |
|      height      |  高度  |
| background-color | 背景色 |

# 文字控制属性

|     描述     |      属性       |
| :----------: | :-------------: |
|     字体     |    font-size    |
|   字体粗细   |   font-weight   |
|   字体倾斜   |   font-style    |
|     行高     |   line-height   |
|    字体族    |   font-family   |
| 字体复合属性 |      font       |
|   文本缩进   |   text-indent   |
|   文本对齐   |   text-align    |
|    修饰线    | text-decoration |
|     颜色     |      color      |

* font-weight

  | 加粗 |  700（bold）  |
  | :--: | :-----------: |
  | 正常 | 400（normal） |

  

* font-style属性值

  正常:normal

  倾斜：italic

* 行高由上间距，文本高度，下间距组成

  若行高值是数字，则表示当前标签字体大小的倍数 

* 垂直居中技巧

  盒子高度属性与文字行高相同（只适用于单行文字）

* font-family属性值

  字体名

  sans-serif（无衬线字体）

* font

  font：是否倾斜  是否加粗   字号/行高    字体（必须按顺序写）

  **==注==：字号字体值必须写否则font属性不生效**

* text-indent属性值
  * 数字+px
  * 数字+em（推荐：1em=当前标签字号大小）

* text-align（本质：居中的是文字不是标签 ，要有父级标签）

  | 属性值 |      效果      |
  | :----: | :------------: |
  |  left  | 左对齐（默认） |
  | center |      居中      |
  | right  |     右对齐     |

* text-decoration

  |    属性值     |    效果    |
  | :-----------: | :--------: |
  |   **none**    |   **无**   |
  | **underline** | **下划线** |
  | line-through  |   删除线   |
  |   overline    |   上划线   |

  

* 颜色rgba写法

  rgba(r,g,b,a)a表示透明度，取值：0-1

# 复合选择器

## 后代选择器(所有后代及后代的后代)

写法：父选择器   子选择器{CSS属性}

## 子代选择器

写法：父选择器> 子选择器{CSS属性}

## 并集选择器

选中多组标签设置相同的样式

写法：选择器1，选择器2，···，选择器n{CSS属性}

* 交集选择器

  选中同时满足多种条件的元素

  写法：选择器1选择器2{CSS属性}，选择器之间无符号

  如果交集选择器中有标签选择器，标签选择器必须书写在最前面。

# 伪类（状态）选择器

写法：

鼠标悬停状态：选择器：hover{CSS属性}

超链接

|  选择器   |   作用   |
| :-------: | :------: |
|  ：link   |  访问前  |
| ：visited |  访问后  |
|  ：hover  | 鼠标悬停 |
| ：active  |  点击时  |

要设置多个的话顺序：lvha

# CSS特性

* 继承性

  子级继承父级的文字属性

  如果标签自己有样式则生效自己的样式

* 层叠性
  * 相同属性会覆盖
  * 不同的属性会叠加

* 优先级

  * 一个标签使用多个选择器时，匹配规则，比如用不同选择器给一个标签添加颜色，该听谁的

    通配符选择器<标签选择器<类选择器<id选择器<行内样式<!important

    (选中标签范围越大，优先级越低)

  * 叠加计算（复合选择器）规则

    叠加计算：如果是复合选择器，则需要权重叠加计算。

    公式: (每一级之间不存在进位)
    (行内样式，id选择器个数，类选择器个数，标签选择器个数)
    规则:
    从左向右依次比较选个数，同一级个数多的优先级高，如果个数相同，则向后比较

    ！important权重最高

    继承权重最低

* html简写

  类选择器：标签名.类名（div标签更简单，直接.类名）

  id选择器：标签名#类名

  同级标签：div+p

  父子级标签：div>p

  多个相同标签：标签*个数

  有内容标签：标签名{内容}

* CSS简写

  首字母

  多个用加号

# 背景属性

|      描述      |         属性          |
| :------------: | :-------------------: |
|     背景色     |   background-color    |
|     背景图     |   background-image    |
| 背景图平铺方式 |   background-repeat   |
|   背景图位置   |  background-position  |
|   背景图缩放   |    background-size    |
|   背景图固定   | background-attachment |
|  背景复合属性  |      background       |

* 背景图默认平铺（复制）效果

  |  属性值   |     效果     |
  | :-------: | :----------: |
  | no-repeat |    不平铺    |
  |  repeat   | 平铺（默认） |
  | repeat-x  | 水平方向平铺 |
  | repeat-y  | 垂直方向平铺 |

* 背景图位置

  | 关键字 | 位置 |
  | :----: | :--: |
  |  left  | 左侧 |
  | center | 居中 |
  | right  | 右侧 |
  |  top   | 顶部 |
  | bottom | 底部 |

  * 坐标（数字+px，正负都可以）
  * 提示：
    * 关键字取值方式写法可以颠倒取值顺序
    * 可以只写一个关键字，另一个方向默认居中，数字只写一个值表示水平方向，垂直方向居中

* **背景图缩放:background-size**

  * **关键字**

    **cover：等比例缩放背景图片以完全覆盖背景区，可能背景图片部分看不见**

    **contain：等比例缩放背景图片以完全装入背景区，可能背景区部分空白**

  * **百分比：根据盒子尺寸计算图片大小**

* 背景图固定

  属性名：background-attchment

  属性值：fixed


* 背景图复合

  属性值：背景色 背景图 背景平铺方式 背景图位置**/**背景图缩放（前用斜杠）

# 显示模式

* 块级元素
  * 独占一行
  * 宽度默认是父级的100%
  * 添加宽高属性生效

* 行内元素
  * 一行共存多个
  * 尺寸由内容撑开
  * 加宽高不生效

* 行内块元素
  * 一行共存多个
  * 默认尺寸由内容撑开
  * 宽高属性生效

* 转换显示模式

  属性名：display

  |      属性值      |    效果    |
  | :--------------: | :--------: |
  |    **block**     |  **块级**  |
  | **inline-block** | **行内块** |
  |      inline      |    行内    |

  
