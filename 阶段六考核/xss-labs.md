添加标签得闭合前面的标签

小写转化并删除关键字可以采用双拼写法

# 第一关

观察到网址中“？”后`name=test`，

![1](https://github.com/YZLSJR/Tasks/blob/a00bb1cfb2c4e04dfaf8661ed4ad742365990ebc/%E9%98%B6%E6%AE%B5%E5%85%AD%E8%80%83%E6%A0%B8/1.png)

尝试简单的标签插入，输入`<Script>alert(1)</script>`后显示过关，查看源码发现，name的值插入到了html里头，还将输入的值的长度显示了出来

# 第二关

在搜索框里再次输入`<Script>alert(1)</script>`尝试一下发现他显示在了屏幕里没有弹窗，查看源代码得知

![2](https://github.com/YZLSJR/Tasks/blob/8f7faf5e5ff07140864126c7f9a86f4f49d8f380/%E9%98%B6%E6%AE%B5%E5%85%AD%E8%80%83%E6%A0%B8/2.png)

“<“”>“被实体转义，但是只有一个被转义，另一个被引号包裹，所以只需要将双引号闭合掉即可，输入`"> <script>alert()</script> <"`

# 第三关

查看源码，

![3](https://github.com/YZLSJR/Tasks/blob/ee1e3b9dda16702a571ce7b75260fcbfece47597/%E9%98%B6%E6%AE%B5%E5%85%AD%E8%80%83%E6%A0%B8/3.png)

发现输入的内容被单引号括起来了，所以尝试输入`'> <script>alert()</script> <'`发现特殊符号被实体转义了，所以我们可以考虑input标签的一些特殊事件如`onkeypress` `onkeydown` `onfocus` 以onfocus为例借助JavaScript伪协议输入`' onfocus=javascript:alert() '` 之后再点击一下输入框就可以了，但如果不借助伪协议的话，双引号会被实体转义

# 第四关

第四关和第三关差不多，输入`' onfocus=javascript:alert() '`后查看源码发现输入内容是被双引号包裹，所以将单引号换成双引号即可，同时查看源码得知这一关是将尖括号直接删除掉了，所以仿照第三关但不借助伪协议也可以绕过尖括号

# 第五关

尝试输入`' onfocus=javascript:alert() '`

![4](https://github.com/YZLSJR/Tasks/blob/5e4956dba32f71e70120988e2a5af017f0ed9981/%E9%98%B6%E6%AE%B5%E5%85%AD%E8%80%83%E6%A0%B8/4.png)

发现网页在on中间加了一个下划线，输入`"> <script>alert()</script> <"`发现script中间也加了下划线，但他并没有过滤尖括号所以可以尝试其他标签如a标签的href属性构造payload`"> <a href=javascript:alert()>123</a> <"`,之后再点击123即可

# 第六关

输入上一关的payload发现href被过滤掉了，再输入前几关的payload尝试发现很多都被过滤掉了，但发现大小写没有被过滤掉，所以这题可以用大小写绕过，将前几关的payload加上大小写构造新的payload`"> <sCript>alert()</sCript> <"`或`"Onfocus=javascript:alert() "`或`"> <a hRef=javascript:alert()>x</a> <"`

# 第七关

首先我们可以将之前payload的一些可能被过滤的关键字试一下如`" <sCRipt> OnFocus <a hREf=javascript:alert()> "`发现这些输入的值变成了`" <> focus <a =java:alert()> "`，

![5](https://github.com/YZLSJR/Tasks/blob/48a65a59c3b77dcc654a576e2e27c9fdd975236e/%E9%98%B6%E6%AE%B5%E5%85%AD%E8%80%83%E6%A0%B8/5.png)

所以这一关进行了小写转化并且将on，script，href都给删掉了，所以可以考虑双拼写法将on写成oonn，script写成scrscriptipt，可以绕过去，输入`"> <Scrscriptipt>alert()</scrscriptipt> <"`即可

# 第八关

先输入关键字尝试一下如`" Src DaTa <sCRipt> OnFocus <a hREf=javascript:alert()> "`查看源码

![6](https://github.com/YZLSJR/Tasks/blob/eccde3c0a2b78ee9e37c78eccdce8882063a6836/%E9%98%B6%E6%AE%B5%E5%85%AD%E8%80%83%E6%A0%B8/6.png)

我们输入的内容会直接带入href，点击友情链接的时候，就会执行我们带入的内容，同时这一关添加了小写转化函数，还过滤掉了src、data、on···、href、script、（双引号），他没有过滤[&#；]所以我们还可以对script进行HTML编码，找一个编码工具（[MaTools]([在线Unicode编码解码 - 码工具 (matools.com)](https://www.matools.com/code-convert-unicode))）把script转义一下子，

![7]()

输入`java&#115;&#99;&#114;&#105;&#112;&#116;:alert()`点一下添加友情链接然后再点击一下友情链接就可以了

# 第九关

将第八关答案输入进去发现不行，查看源码发现href标签里插入不进去再查看这一关的源码，发现有一句

![8]()

`if(false===strpos($str7,'http://')`也就是说输入的内容里如果没有http://就会执行if语句，所以我们在输入的语句中要包含http://，并且要用注释符包裹起来

# 第十关

我们再次先输入一些关键字在网址栏`" Src DaTa <sCRipt> OnFocus <a hREf=javascript:alert()> &# "`发现全部被过滤掉了，查看源码发现有三个参数，get传参可能传到任何一个里，只能看一下这一关的PHP文件，

![9]()

看到get传参t_sort,并且过滤掉了<>,标签插入之后不能闭合，但还是可以考虑onfocus事件，这里输入框添加了隐藏属性，需要添加type="text"。构造payload`t_sort=" onfocus=javascript:alert() type="text`

我们也可以对这三个参数依次进行传参，有回显的那个就是get传参对象,输入`t_link="666"&t_history="777"&t_sort="888"`

![10]()



