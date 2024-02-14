# 基本PHP语法

PHP脚本以`<?php`开始，以`?>`结束

PHP中每个代码行都必须以分号结尾

PHP有两种输出文本的基本指令：echo和print

## PHP变量

* 变量以$符号开始，后面跟着变量的名称
* 其他规则和C语言一样

## 声明变量

没有命令，直接赋值

## 特殊运算符

a.b相当于ab
例："hello"."world"="helloworld"

a .= b 相当于 a=a.b

## echo和print语句

echo和print的区别：

* echo-可以输出一个或多个字符
* print-只允许输出一个字符串，返回值总为1

提示：echo输出速度比print快

form表单中的action属性，但提交表单时向一个地方发送表单数据

## $_GET变量

用于收集来自method=“get”
get方法发送的信息会在浏览器的地址栏显示，对发送的信息的量也有限制

## $_POST

用于收集来自method=“post”
get方法发送的信息不会在浏览器的地址栏显示，对发送的信息的量没有限制

# PHP正则表达式

preg_match(pattern，subject，matches):在字符传中搜索匹配的模式，只返回第一个匹配项

* pattern：正则表达式模式
* subject：要搜索的字符串
* matches：（可选）用于储存匹配的结果

preg_match_all(pattern，subject，matches)：在字符传中搜索匹配的模式，返回所有匹配项

* pattern：正则表达式模式
* subject：要搜索的字符串
* matches：用于储存匹配的结果

preg_replace(pattern，replacement，subject):在字符传中搜索匹配的模式，然后进行替换

* pattern：正则表达式模式
* replacement：替换的字符串
* subject：要搜索的字符串（原字符串）

