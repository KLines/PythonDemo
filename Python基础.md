
Python ： 交互式编程，不需要经过编译阶段，可以直接运行。（动态语言）


## 1、基本语法 ##

**单下划线**

* 模块中使用单下划线(_)开头定义函数、全局变量和类不能被模块外部以: from module import *形式导入，但可以用：from module import _func形式单独导入

**双下划线**

* 以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数
* 带双下划线的类变量、实例变量、方法，在class类的内部具有正常访问权限，实例对象和子类对象不能被直接访问
	

**行和缩进**

* Python 的代码块不使用大括号 {} 来控制类、函数以及其他逻辑判断，而是用缩进来写模块。

**多行语句**

* Python语句中一般以新行作为语句的结束符。但是我们可以使用斜杠（ \）将一行的语句分为多行显示

		total = item_one + \
				item_two + \
				item_three

**命名规范**

* 模块尽量使用小写命名，首字母保持小写，尽量不要用下划线(除非多个单词，且数量不多的情况)
* 类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头
* 函数名一律小写，如有多个单词，用下划线隔开，私有函数在函数前加下划线__
* 变量名尽量小写，如有多个单词，用下划线隔开
* 常量采用全大写，如有多个单词，使用下划线隔开
* 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
	
		# !/usr/bin/env python3
		# -*- coding: utf-8 -*-


## 2、变量类型 ##

**变量类型**

* 变量存储在内存中的值，这就意味着在创建变量时会在内存中开辟一个空间。基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。因此，变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符。
		

**变量赋值**

* Python中的变量赋值不需要类型声明，我们所说的"类型"是变量所指的内存中对象的类型。
* 每个变量在内存中创建，都包括变量的标识，名称和数据这些信息，每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
* 变量名实际存储的是变量在内存中的地址
		

**多变量赋值**

* a = b = c = 1 ： 创建一个整型对象，值为1，三个变量被分配到相同的内存空间上
* a, b, c = 1, 2, "john" ： 创建多个对象指定多个变量
	

**标准数据类型**

* Python有六个标准的数据类型：Numbers（数字），str（字符串），list（列表），tuple（元组），set（集合），dict（字典）
	
* 1、Number（数字）：数字数据类型用于存储数值。他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。
	
		* 当你指定一个值时，Number对象就会被创建
			var1 = 1
			var2 = 10
		* 可以使用del语句删除一些对象的引用
			del var
			del var_a, var_b
		* Python支持四种数字类型：int、float、bool、complex
	
* 2、str（字符串）：从字符串中获取一段子字符串的话，可以使用 [头下标:尾下标] 来截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空
表示取到头或尾。获取的子字符串包含头下标的字符，但不包含尾下标的字符。

		* 特点：不可变对象，有序
		* python的字串列表有2种取值顺序:
			从左到右索引默认0开始的，最大范围是字符串长度-1
			从右到左索引默认-1开始的，最大范围是字符串开头（-长度大小）
		* 加号（+）是字符串连接运算符，星号（*）是重复操作
		* 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，在字符串前面添加一个r，表示原始字符串
		* 字符串不能改变，向一个索引位置赋值，比如word[0] = 'm'会导致错误

* 3、list（列表） 可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。列表用 [ ] 标识。

        * 特点：有序，可修改，元素可重复，元素可以是可变对象
        * List = ['runoob', 786, "john", 'john', 70.2, ['test1', 'test2']] 
        * list[:]、list[0:]：表示返回所有元素
        * List[::2]：表示 step 为 2，步长为正时，从左向右取值。步长为负时，反向取值。 a=[1,2,3,4]  print(a[::-1])->[4, 3, 2, 1]
        * b=a：传递引用，b=a[:]：拷贝，生成新的对象
	
* 4、tuple（元祖） 元组是另一个数据类型，类似于List（列表）。元组用 ( ) 标识。但是元组不能二次赋值，相当于只读列表。

        * 特点：有序，不可修改，元素可重复，元素可以是可变对象，元组中的元素值是不允许删除
        * Tuple = ('tuple', 123, 'test', ['test1', 'test2'])
        * 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
        * tuple所指向的内存实际上保存的是元组内数据的内存地址集合，这个集合不能修改，但元素地址映射的对象根据自身类型确定是否可以修改。
	
* 5、set（集合） 集合是另一个数据类型，属于无序的对象集合，创建时元素可重复，运行时重复的元素被自动去掉，可以使用大括号 { } 或者 set() 函数创建集合

		* 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
        * 特点：无序，可修改，元素唯一，元素必须是不可变对象
        * student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
        * s.update( "字符串" ) 与 s.update( {"字符串"} ) 含义不同:
            s.update( {"字符串"} ) 将字符串添加到集合中，有重复的会忽略。
            s.update( "字符串" ) 将字符串拆分单个字符后，然后再一个个添加到集合中，有重复的会忽略。
        * 集合对 list 和 tuple 具有排序(升序)，去重功能
	
* 6、dict（字典）是除列表以外python之中最灵活的内置数据结构类型。字典用"{ }"标识。字典由索引(key)和它对应的值value组成。

        * 特点：无序，可修改，键(key)必须使用不可变类型，键(key)必须是唯一的。
        * Dictionary = {'name': 'john','code':6734,'dept': 'sales'}
        * 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
        * dict.keys 返回的是 dict_keys 对象
	
* 7、bool（布尔值）布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值。
	
* 注意：
	* 1、Python可以通过内置函数进行数据类型的转换，从而返回一个新的对象，表示转换的值
	* 2、Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。
	* 3、不可变数据（3 个）：Number、str、tuple
	* 4、可变数据（3 个）：list、dict、set，  list、set、dict类中存在copy方法
	* 5、可迭代对象：str、list、tuple、set、dict（默认输出key值）
	* 6、有序数据：str、list、tuple    无序数据：set、dict
	* 7、Python 的所有数据类型都是类，可以通过 type() 查看该变量的数据类型，还可以用 isinstance 来判断
   	 	* isinstance(object, classinfo) object -- 实例对象，classinfo -- 可以是直接或间接类名、基本类型或者有它们组成的元组。
   		* type()不会认为子类是一种父类类型，isinstance()会认为子类是一种父类类型。
	* 8、字典和集合无序的实现方式是hash表，通过hash值来将对象放入hash表中，从而达到无序的操作。（对象的hash值是不断变化的）Python中int型的hash值就是它本身，那么set或dict中的排序方式又是通过hash表实现的，所以自然顺序就不会变。
	* 9、list和dict有以下几个特点：
		* dict查找和插入的速度极快，不会随着key的增加而变慢；list查找和插入的时间随着元素的增加而增加
		* dict需要占用大量的内存，内存浪费多；list占用空间小，浪费内存很少


## 3、运算符 ##

**算术运算符**

* +	加 - 两个对象相加	a + b 输出结果 30
* -	减 - 得到负数或是一个数减去另一个数	a - b 输出结果 -10
* *	乘 - 两个数相乘或是返回一个被重复若干次的字符串	a * b 输出结果 200
* /	除 - x除以y	b / a 输出结果 2
* %	取模 - 返回除法的余数	b % a 输出结果 0
* ** 幂 - 返回x的y次幂	a**b 为2的3次方， 输出结果 8
* // 取整除 - 返回商的整数部分（向下取整）  >>> 9//2 --> 4 >>> -9//2 --> -5

**比较运算符：==、!=、<>、>、<、>=、<=**

**赋值运算符： +=、-=**

**位运算符：&、|、^、~、<<、>>**

**逻辑运算符（重点）**

* a = 10, b = 20
* and：x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回20  (0 and "测试") 返回0
* or：x or y	布尔"或"	- 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
* not：not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False

**成员运算符**

* in：如果在指定的序列中找到值返回 True，否则返回 False。x 在 y 序列中，如果 x 在 y 序列中返回 True。
* not in：如果在指定的序列中没有找到值返回 True，否则返回 False。x 不在 y 序列中，如果 x 不在 y 序列中返回 True。

**身份运算符（重点）**

* is：判断两个标识符是不是引用自一个对象 x is y，类似 id(x) == id(y)， 如果引用的是同一个对象则返回 True，否则返回 False
* is not：判断两个标识符是不是引用自不同对象 x is not y，类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
* 注意：
	* is 与 == 区别，is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
	* a is b 相当于 id(a)==id(b)


## 4、条件语句、循环语句 ##

**条件语句**

* 1、由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现
* 2、如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功
* 3、使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
* 4、if 简单条件判断一行搞定：

		a = [1,2,3]
		b = a if len(a) != 0 else ""
		print(b)

* 5、Python 没有 switch/case 语句，可以考虑用字典映射的方法替代

		def num2Str(arg):
		    switcher={
		        0:zero,
		        1:one,
		        2:two,
		        3:lambda:"three"
		    }
		    func=switcher.get(arg,lambda:"nothing")
		    return func()

* 6、if not True：表示false， if not False：表示true
	

**while循环语句**

* 1、while 语句时 continue 用于跳过该次循环，break 则是用于退出循环
* 2、"判断条件"还可以是个常值，表示循环必定成立
* 3、while … else 在循环条件为 false 时执行 else 语句块（即 while 不是通过 break 跳出而中断的）
	

**for循环语句**

* 1、for循环可以遍历任何序列的项目，如一个列表或者一个字符串
* 2、for … else 中的 else 语句会在循环正常执行完的情况下执行（即 for 不是通过 break 跳出而中断的）


## 5、函数用法 ##

* Python程序是从上往下顺序执行的，而且碰到函数的定义代码块是不会立即执行的，只有等到该函数被调用时，才会执行其内部的代码块。
	

**函数定义**

* 函数名：foo、outer、inner
* 函数体：函数的整个代码结构
* 返回值：return后面的表达式
* 函数的内存地址：id(foo)、id(outer)等
* 函数名加括号：对函数进行调用，比如foo()、outer(foo)
* 函数名作为参数： outer(foo)中的foo本身是个函数，但作为参数被传递给了outer函数
* 函数名加括号被当做参数：其实就是先调用函数，再将它的返回值当做别的函数的参数，例如outer(foo())
* 返回函数名：return inner
* 返回函数名加括号：return inner()，其实就是先执行inner函数，再将其返回值作为别的函数的返回值。
	

**函数使用**

* 1、函数中参数传递，具体为：不可变对象和可变对象。
* 2、函数返回多个值的时候，是以元组的方式返回的
* 3、参数分为：固定参数，可变参数
	
		* 固定参数：必需参数、关键字参数、默认参数
			def printinfo(name, age=20):
			    print("名字: ", name)
			    print("年龄: ", age)
			printinfo("test", 10)  # 必须参数，根据参数顺序入参
			printinfo(age=50, name="runoob")  # 关键字参数，可根据参数名匹配
			printinfo("func")  # 使用默认参数，默认参数必须放在最后面

		* 可变参数：
			def printinfo(number, *args):  # 以元组(tuple)的形式导入
			    print(number)
			    print(args)
			printinfo(1, "test", 3, 4)
		
			def printinfo(number, **kwargs):  # 以字典(dict)的形式导入
			    print(number)
			    print(kwargs)
			printinfo(1, name="test", age=20)  # key必须是字符串
			
			def printinfo(a, b, *, c):  # 如果单独出现星号 * 后的参数必须用参数名传入
			    return a + b + c
			print(printinfo(1, 2, c=3))

* 4、lambda 表达匿名函数，也可以使用关键字参数、默认参数

		count = lambda arg1, arg2: arg1 + arg2 
		print(count(1, 2))

* 5、函数参数可以是一个函数:

		def func():
			print("func()")
		def excute(f):
			f()	
			print("excute()")
		excute(func) 

* 6、在函数中定义函数
		
		def func():
			print("func()")
		    def temp():
		        print("temp()")
			temp()
		func()

* 7、从函数中返回函数

		def func():
			print("func()")
		    def temp():
		        print("temp()")
		 	return temp
		f = func()
		f()
	

**相关函数**

* 1、range([start=0], stop, step) 函数返回的是一个可迭代对象（类型是对象），而不是列表类型，它只是在迭代的情况下返回指定索引的值，但是它并不会在内存中真正产生一个列表对象，这种对象被称为可迭代对象
* 2、enumerate(sequence, [start=0])  #第二个参数为指定索引函数：多用于在for循环中得到计数，利用它可以同时获得索引和值
* 3、id()：函数能够获取对象的内存地址
* 4、hash()：函数可以应用于数字、字符串和对象，不能直接应用于 list、set、dictionary
* 5、str()： 函数返回一个用户易读的表达形式
* 6、repr()： 产生一个解释器易读的表达形式
* 7、map()：函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
		list(map(str, [1, 2, 3, 4]))--> ['1', '2', '3', '4']
* 8、reduce()：累积函数
* 9、sorted()：排序函数
	

**直接赋值、浅拷贝、深度拷贝**

* 直接赋值：其实就是对象的引用（别名）
	* b = a: 赋值引用，a 和 b 都指向同一个对象
* 浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象
  	* b = a.copy(): 浅拷贝, a 和 b 是一个独立的对象，但他们的子对象还是指向统一对象（是引用）
* 深拷贝(deepcopy)：copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象
	* b = copy.deepcopy(a): 深度拷贝, a 和 b 完全拷贝了父对象及其子对象，两者是完全独立的


## 6、生成器函数 ##

**迭代器（Iterator）**

* 迭代器是一个可以记住遍历的位置的对象。StopIteration 异常用于标识迭代的完成
* 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
* 迭代器有两个基本的方法：iter() 和 next()
* 使用iter()函数可以将list、dict、str等由Iterable变成Iterator
	

**可迭代对象（Iterable）**

* 可以直接作用于 for 循环的对象统称为可迭代对象，数据类型有以下几种：
	* 集合数据类型，如list、tuple、dict、set、str等
	* generator，包括生成器和带yield的generator function
* 注意：
	* 如果一个对象是迭代器，那么这个对象肯定是可迭代的；但是反过来，如果一个对象是可迭代的，那么这个对象不一定是迭代器。
	* 凡是可作用于for循环的对象都是Iterable类型，凡是可用作next()函数的对象都是Iterator类型，它表示一个惰性计算的序列。
		

**生成器（generator）**

* 在Python中，使用了 yield 的函数被称为生成器（generator），生成器是一个返回Iterator对象的函数
* yield 是一个类似 return 的关键字，生成器的唯一注意事项就是：生成器只能遍历一次。
* 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
* 注意：
	* 一个带有yield的函数和普通函数不同，Python解释器会将其视为一个生成器（generator），调用函数时不会执行任何函数代码，而是返回一个Iterator对象，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。


## 7、装饰器函数 ##

**装饰器含义**

* 1、首先在Python中的函数是可以看做一个特殊变量的，而装饰器是建立在闭包的前提上的。
* 2、闭包就是将函数当做参数传入另一个函数，两个函数的嵌套，外部函数返回内部函数的引用。
* 3、装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
* 总结：装饰器就是在不改变原先函数代码的情况下，给原先的函数添加功能。

**装饰器创建**

* 1、创建一个闭包
		
		def outer(x):
		    def inner(y):
		        return x + y
		    return inner    

* 2、@符号装饰已定义的函数
	
        def func(func):
        	# 这里就直接写万能装饰器了
        	def wrapper():
        		print("装饰器")
        		func()
        	return wrapper
        
	    print("======= 未使用@装饰 ========")
	    def origin():
        	print("被装饰的函数")
        	pass
	    origin = func(origin) # 等价于 func(origin)()
	    origin()
	    
	    print("======= 使用@装饰 ========")
	    @func # 等价于 demo = func(demo)
	    def demo():
        	print("被装饰的函数")
        	pass
	    demo()
	
* 3、执行顺序：
	* 1、Python会按照自下而上的顺序把各自的函数结果作为下一个函数（上面的函数）的输入
	* 2、当解释器读到@修饰符时，会先解析@后的内容，直接就把@下一行的函数或者类作为@后边的函数的参数，然后将返回值赋值给下一行修饰的函数对象
	* 3、functools wraps：@wraps表示在装饰器里面访问在装饰之前的函数的属性。
	* 4、先执行修饰器函数，然后有return fn的时候，修饰器下的函数需要单独调用执行，没有return fn时，系统会自动执行修饰器下的函数
	

**装饰器类型**

* 1、一般装饰器
* 2、带参数的装饰器
		
		def logit(args):
		    def logging(func):
		        @wraps(func)
		        def wrapper():
		            print(args)
		            print(func.__name__+" was called")
		            func()
		        return wrapper
		    return logging
		
		@logit("使用logit")
		def test():
		    print("函数装饰器--带参数的装饰器")
		    pass
		test()
	
* 3、类装饰器（无参数、带参数）
		
		class Func(object):
		    def __init__(self,func):
		        self.func = func
		   	def __call__(self, *args, **kwargs):
		        self.func()
		        
	    @Func
	    def test():
	        pass
	    
	    test()
	* 类装饰器类似函数装饰器,创建类对象时使用一个__init__方法接收需要装饰的函数,并定义__call__方法运行需要添加的功能并执行原先的函数代码
	* 被类装饰器装饰的函数不论被调用几次，__init__ 函数只会执行一次，并且它的执行是被装饰函数声明装饰时就自动执行，不需要手动调用
	* 装饰器的参数从 __init__ 函数中传，函数的参数从 __call__ 函数中传
	* 单例模式的使用


## 8、变量作用域 ##

**4种类型**

* L （Local） 局部作用域
* E （Enclosing） 闭包函数外的函数中
* G （Global） 全局作用域
* B （Built-in） 内建作用域（一般指系统自带）
* 以 局部作用域 > 嵌套作用域 > 全局作用域 > 内置作用域 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
		
		g = 4  # 全局变量
		b =int(3.3) # 内建作用域
		def outer():
		    e = 2  # 闭包函数外的函数中
		    def inner():
		        l = 1  # 局部变量
		        print("全局作用域：",g)
		        print("内建作用域：", b)
		        print("闭包函数外的函数中："+str(e))
		        print("局部作用域：",l)
		    return inner  # 返回一个函数
		outer()()

**LEGB法则** 

* 当在函数中使用未确定的变量名时，Python会按照优先级依次搜索4个作用域，以此来确定该变量名的意义。首先搜索局部作用域(L)，之后是上一层嵌套结构中def或lambda函数的嵌套作用域(E)，之后是全局作用域(G)，最后是内置作用域(B)。按这个查找原则，在第一处找到的地方停止。如果没有找到，则会出发NameError错误。    
* 模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如if/elif/else/、try/except、for/while等）是不会引入新的作用域，这些语句内定义的变量，外部也可以访问
	    

**global和nonlocal关键字**

* 当内部作用域想修改全局变量时，则需要 global 关键字
* 当内部作用域想修改嵌套作用域（enclosing作用域，外层非全局作用域）中的变量，则需要 nonlocal 关键字
* nonlocal 只能修改外层函数的变量而不能修改外层函数所引用的全局变量


## 9、模块&关键字 ##

**import 与 from...import**

* 1、将整个模块(somemodule)导入，格式为： import somemodule
* 2、从某个模块中导入某个函数,格式为： from somemodule import somefunction
* 3、从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
* 4、将某个模块中的全部函数导入，格式为： from somemodule import *
* 模块A中的代码在模块B中进行import A时，只要B模块代码运行到该import语句，模块A的代码会被执行
	

**package**	

* 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则Python就把这个目录当成普通目录，而不是一个包
* __init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是 demo

		demo
		|---__init__.py
		|---abc.py
		|---xyz.py
		

**关键字**

* 1、循环及判断主要包括关键字：if elif　else　for　while　break　continue　and　 or　is　not　in
* 2、函数、模块、类主要包括关键字：from　import　as　def　pass　lambda　return　class
* 3、异常主要包括关键字：try　except　else  finally  assert raise 
* 4、其他关键字：print　del　global　with　assert　yield　exec


**第三方模块**

* 1、psutil：运维
* 2、chardet：判断编码类型
* 3、Pillow：图像处理


## 10、异常和断言 ##

**异常分类**
		
	BaseExcetion 
		|--SystemExit	Python解释器退出
		|--Exception    常见错误的基类
			　　|--AssertionError	断言语句失败
			　　|--AttributeError	对象没有这个属性
			　　|--EOFError	没有内建输入,到达EOF 标记
			　　|--EnvironmentError	操作系统错误的基类
		|--KeyboardInterrupt   用户中断执行
		|--GeneratorExit    生成器(generator)发生异常来通知退出

**捕获异常**

* try...except：
    * 首先，执行 try 子句（在关键字 try 和关键字 except 之间的语句）
    * 如果没有异常发生，忽略 except 子句，try 子句执行后结束
    * 执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行
    * 如果一个异常没有与任何的 excep 匹配，那么这个异常将会传递给上层的 try 中
    * 注意：
    	* 1、一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行
    	* 2、一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:
    	
	        	except (RuntimeError, TypeError, NameError):
	          	    pass

    	* 3、最后一个except子句可以忽略异常的名称，它将被当作通配符使用

* try...except...else
  
* else 子句必须放在所有的 except 子句之后，将在 try 子句没有发生任何异常的时候执行
  
* try...except...else...finally 
    * finally 语句无论是否发生异常都将执行其中的代码
    * 如果一个异常在 try 、except 、else 子句里任意一处被抛出，而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后被抛出

**执行流程**
        
	try:
	    执行代码
	except XXXError as err:
		程序异常时执行
	except:
	    程序异常时执行
	else:
	    没有异常时执行
	finally:
	    始终都会执行

**抛出异常**

* raise 唯一的一个参数指定了要被抛出的异常，它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）
* 如果只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出
	

**assert（断言）**

* assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常

		assert expression
		等价于：
		if not expression:
			raise AssertionError
		assert 1==2,'1 不等于 2'


## 11、面向对象 ##

**基本概念**

- 类(Class):用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
- 方法：类中定义的函数。封装数据的函数是和类本身是关联起来的，我们称之为类的方法
- 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
- 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
- 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
- 局部变量：定义在方法中的变量，只作用于当前实例的类。
- 实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
- 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
- 实例化：创建一个类的实例，类的具体对象。
- 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

**构造方法**		

* 1、类有一个名为 __init__() 的构造方法，该方法在类实例化时会自动调用，无返回值 
	* def __init__(self,参数1,参数2...)：参数通过 __init__() 传递到类的实例化操作上
* 2、self 代表类的实例，也就是当前对象的地址，而 self.class 则指向类
* 3、子类调用父类的构造方法：显式调用父类的构造方法，或者不重写父类的构造方法
* 4、调用父类构造函数方式：
	* super(子类，self).__init__(参数1,参数2...)
	* super().__init__(参数1,参数2...)
	* 父类名称.__init__(self,参数1,参数2...)
* 5、使用场景：
	* 子类需要自动调用父类的方法：子类不重写__init__()方法，实例化子类后，会自动调用父类的__init__()的方法。
	* 子类不需要自动调用父类的方法：子类重写__init__()方法，实例化子类后，将不会自动调用父类的__init__()的方法。
	* 子类重写__init__()方法又需要调用父类的方法：使用super关键词
* 6、super() 函数是用于调用父类(超类)的一个方法
	* super(type[, object-or-type]) type -- 类  object-or-type -- 类，一般是self
	* super().xxx = super(Class, self).xxx

**类属性和实例属性**

* 类属性有且只有1份，创建的实例都会继承自唯一的类属性。如果在类上绑定一个属性，那么所有的实例都可以访问类属性，一旦类属性改变就会影响到所有的实例
* 实例属性和方法每个实例各自拥有，相互独立，绑定在一个实例上的属性不会影响到其它的实例
* 当实例属性和类属性重名时，实例属性优先级高，它将屏蔽掉对类属性的访问
* 类或者实例可以任意绑定属性和方法，如果绑定的方法中存在属性，绑定方法且执行之后才能访问其属性

		1、绑定类属性和类方法	 
			# 给class绑定类方法和类属性
			def set_score(self, score):
			    print(self)
			    self.score = score  # 方法中的属性值实际是类属性
			Classname.set_score = MethodType(set_score,Classname)
		2、绑定实例属性和普通方法
			# 给class绑定普通方法和实例属性
			def set_sex(self, sex):
			    print(self)
			    self.sex = sex
			Classname.set_sex = set_sex
		3、单个实例绑定实例属性和普通方法
			# 给单个实例绑定一个方法
			def set_grade(self, grade):
			    print(self)
			    self.grade = grade
			m.set_grade= MethodType(set_grade,m)

**静态方法、普通方法、类方法**

* 静态方法: 用 @staticmethod 装饰的不带 self 参数的方法叫做静态方法，类的静态方法可以没有参数，可以被类和对象调用，不论任何情况都是函数--function
* 类方法: 默认有个 cls 参数，可以被类和对象调用，需要加上 @classmethod 装饰器，不论任何情况，都是方法--method
* 普通方法: 默认有个self参数，代表的是类的实例且只能被对象调用，self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。如果是实例访问就是方法，如果是类名访问就是函数


**其他属性**

* 单继承，多继承，方法重写
   		
		class DerivedClassName(modname.BaseClassName) 单继承
		class DerivedClassName(Base1, Base2, Base3)  多继承
		若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索即方法在子类中未找到时，从左到右查找父类中是否包含方法，不然就抛出异常		
	
* 私有属性和方法：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问，只能在类内部中使用 

* __slots__和__dict__
	
	__dict__：返回对象的属性名和方法名，key：value=名称:值。默认情况类对象和实例对象都会有一个dict

        * 类的dict返回类的属性和方法，并不包含其父类的属性
        * 实例的dict只返回实例的属性名，对于类的属性和方法是不保存的
        * 每次实例化一个类都要分配一个新的dict，因此存在内存空间的浪费
        * dir()返回一个对象的所有有效属性名的集合（包括从父类中继承的属性）

	__slots__：是一个元组，可定义当前能访问到的属性，相当于变成了类的描述符，类似java中的成员变量声明

		* 限制对象任意绑定属性，并且节省内存空间
 		* __slots__ = ('name', 'age'，'set_sex') # 用tuple定义允许绑定的属性名称和方法名称
 		* 类的实例只能拥有slots中定义的变量，不能再增加新的变量
 		* 类属性的添加不受__slots__的限制
 		* 父类定义__slots__对当前类实例起作用，对继承的子类是不起作用的
 		* 父类和子类中都定义__slots__，子类允许定义的属性：子类__slots__+父类__slots__
 		* 父类存在__dict__属性，子类将继承__dict__，即使该子类包含了__slots__属性，该子类的实例依然可以任意添加变量属性
 		* 给类的实例绑定方法时，不能添加__slots__限制之外的属性

    使用区别：
    
        1、每次实例化一个类都要分配一个新的dict，因此存在空间的浪费，因此有了__slots__
        2、一个普通对象使用 __dict__ 来保存它自己的属性，可以动态地向其中添加或删除属性
        3、一个普通对象使用 __slots__ 属性，则该对象用来保存其自身属性的结构一旦创建就不能再进行任何修改
        4、定义了slots后，类的实例就不再有__dict__，但是类的__dict__还可以使用
        5、__slots__ 会为声明了的变量预留空间，同时阻止该类为它的每个实例自动创建 __dict__ 和 __weakref__

* @property属性

	    1、属性名与方法名一定要区分开，不然会进入死循环（self._age，def age()）
	    2、实例化的对象使用属性时，不是调用属性（stu._age），而是用的方法名（stu.age）
	    3、@property其实就是实现了getter功能，@xxx.setter实现的是setter功能；还有一个@xxx.deleter实现删除功能
	    4、定义方法的时候@property必须在@xxx.setter之前，且二者修饰的方法名相同（age()）
	    5、如果只实现了 @property（而没有实现@xxx.setter），那么该属性为只读属性

* 专用方法

		__name__：内置类属性，用于指代当前模块
			* 当前模块时被直接执行，__name__的值就是__main__
			* 导入另一模块时，“__name__”的值就是模块的真实名称
		__del__：析构函数，释放对象时使用
		__repr__：默认打印对象内存地址，重写__repr__方法后，不管直接输出对象还是通过print打印的信息都按我们__repr__方法中定义的格式进行显示
		__str__：默认打印对象内存地址，重写__str__方法后，直接输出对象打印内存地址，通过print打印的信息都按我们__str__方法中定义的格式进行显示
		__getattr__：在没有找到属性的情况下，调用__getattr__可以返回自定义属性值
	

**面向对象模式**

* 反射机制

* @dataclass装饰器的使用
* metaclass元类、抽象类
* 对象复制、垃圾回收、循环引用和弱引用	
* Mixin模式：MixIn是基于多继承实现的一种设计模式，一般是将复杂类的一些功能拆分出来，不用__init__初始化方法，不让其单独工作，只用作混入其他类使用
* 鸭子类型

	* 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
	
			def run_twice(animal):
			    animal.run()
			    animal.run()

	* 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
	
			class Timer(object):
			    def run(self):
			        print('Start...')

	* 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。


## 12、序列化&反序列化 ##

**pickle模块**

* pickle模块是python专用的持久化模块，实现了用于对Python对象结构进行 序列化 和 反序列化 的二进制协议	
	* 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
	* 把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling

* 方法：

	    dumps 　　将对象序列化成bytes对象
	    dump 　　 对象序列化到文件对象，就是存入文件
	    loads　　 从bytes对象反序列化
	    load　　  对象反序列化，从文件读取数据
	    注意：在使用dump()序列化时，打开文件必须要以wb模式，使用load()反序列化，打开文件必须以rb模式
	

**json模块**	

* json数据与Python实例对象转换​
	* 序列化：Python对象 --> dict --> JSON object
	* 反序列化的过程是“JSON object -> dict --> Python对象

* json和Python内置的数据类型对应

		JSON类型				Python类型
		{}					dict
		[]					list
		"string"			str
		1234.56				int或float
		true/false			True/False
		null				None

* 方法：

		dumps	  python数据转json格式
		dump      序列化python数据到json文件
		loads     json数据转python格式
		load	  反序列化json文件到python数据	


## 13、多线程 ##

**创建方式**

* １、通过thread方法创建线程
	
		def func(args):
		    n = 0
		    while n < 5:
		        n = n + 1
		        print("%s 线程运行---"%threading.current_thread().name)
		        sleep(1)
	
		t = threading.Thread(target=func,args=(1,),name="thread-1")
		t.start()

* ２、通过继承Thread类创建线程

	
		class MyThread(Thread):

		    def __init__(self,name):
		        super().__init__(name=name)
		
		    def run(self):
		        n = 0
		        while n < 5:
		            n = n + 1
		            print("%s 线程运行---"%threading.current_thread().name)
		            sleep(1)
		
		t = MyThread('mythread')
		t.start()

**线程同步**

* 1、Lock锁--->处理资源共享问题
* 2、Condition锁，wait()，notify()--->生产者消费者问题
* 3、Semaphore信号量--->控制线程的并发数
* 4、Event对象
* 5、队列（Queue）

**多线程间通信**

* 1、使用全局变量，需要加锁　　
* 2、使用queue模块，可在线程间进行通信，并保证了线程安全

**线程中断问题**

* 1、退出标记
* 2、使用ctypes强行杀掉线程

**多线程使用问题**

* 1、死锁问题
* 2、生产者消费者问题
* 3、获取线程任务执行结果
* 4、threadlocal

**线程池**

* 1、concurrent.futures模块

* 当该函数执行结束后，该线程并不会死亡，而是再次返回到线程池中变成空闲状态，等待执行下一个函数
  		
		Executor
			|--ThreadPoolExecutor 用于创建线程池
				|--submit(fn, *args, **kwargs)：将 fn 函数提交给线程池，*args、*kwargs 代表 fn 函数传入参数
				|--map(func, *iterables, timeout=None, chunksize=1)：该函数将会启动多个线程，以异步方式立即对 iterables 执行 map 处理
				|--shutdown(wait=True)：关闭线程池
			|--ProcessPoolExecutor 用于创建进程池
   
		Future
			|--cancel()：取消该 Future 代表的线程任务。如果该任务正在执行，不可取消，则该方法返回 False；否则，程序会取消该任务，并返回 True。
			|--cancelled()：返回 Future 代表的线程任务是否被成功取消。
			|--running()：如果该 Future 代表的线程任务正在执行、不可被取消，该方法返回 True。
			|--done()：如果该 Funture 代表的线程任务被成功取消或执行完成，则该方法返回 True。
			|--result(timeout=None)：获取该 Future 代表的线程任务最后返回的结果。如果 Future 代表的线程任务还未完成，该方法将会阻塞当前线程
			|--exception(timeout=None)：获取该 Future 代表的线程任务所引发的异常。如果该任务成功完成，没有异常，则该方法返回 None。
			|--add_done_callback(fn)：为该 Future 代表的线程任务注册一个“回调函数”，当该任务成功完成时，程序会自动触发该 fn 函数。

* 2、threadpool第三方模块

**队列（Queue）**

* FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，优先级队列 PriorityQueue

		Queue
		    |--maxsize设置队列中，数据上限，小于或等于0则不限制，容器中大于这个数则阻塞，直到队列中的数据被消掉
		    |--qsize()	返回队列的当前大小
		    |--empty()	如果队列为空，返回True，否则返回False
		    |--full()	如果队列已满，返回True，否则返回False
		    |--put(item, block=True, timeout=None)	将项放入队列
		        1、block=True, timeout=None 在必要时阻塞，直到有空位可用，timeout 为阻止的时间，超时抛出Full异常
		        2、block=False 立即将item放入队列，队列已满引发Full异常
		    |--put_nowait(item)	相当于put(item, False)
		    |--get(block=True, timeout=None)  从队列中删除并返回一个项
		        1、block=True, timeout=None 在必要时阻塞，直到有可用数据为止，timeout 为阻止的时间，超时抛出Empty异常
		        2、block=False 立即获取队列中的可用数据，否则抛出Empty异常
		    |--get_nowait()	等价于get(False)
		    |--task_done() 向已完成的队列任务发送一个信号
		    |--join() 阻塞线程，直到队列为空才放行

**定时任务**

* 1、循环+sleep
* 2、线程模块中Timer类
* 3、schedule第三方模块
* 4、APScheduler任务框架

**Python的线程GIL锁（待深入）**

* Python解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

* GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。

* 在Python中可以使用多线程，但不要指望能有效利用多核，不过可以通过多进程实现多核任务，多个Python进程有各自独立的GIL锁，互不影响。

**进程&多线程**

* 实现多任务通常设计Master-Worker模式，Master负责分配任务，Worker负责执行任务，因此，多任务环境下，通常是一个Master，多个Worker。
* 多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程
* 多进程模式的缺点是创建进程的代价大，在Unix/Linux系统下，用fork调用还行，在Windows下创建进程开销巨大。另外，操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。
* 多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存。在Windows上，如果一个线程执行的代码出了问题，你经常可以看到这样的提示：“该程序执行了非法操作，即将关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束整个进程。


## 14、异步IO ##

**同步IO**
        
* CPU的速度远远快于磁盘、网络等IO。在一个线程中，CPU执行代码的速度极快，如果遇到IO操作，如读写文件、发送网络数据时，就需要等待IO操作完成，才能继续进行下一步操作，这种情况称为同步IO。在IO操作的过程中，当前线程被挂起，而其他需要CPU执行的代码就无法被当前线程执行了。

* 解决办法：

    * 1、使用多线程、多进程模型，缺点：1、不能无上限增加进程、线程数量  2、系统需要不停地切换线程，导致性能下降
    
    * 2、异步IO
  
    

**异步IO**
    

* 当代码需要执行一个耗时的IO操作时，只需要发出IO指令，并不等待IO结果，然后就去执行其他代码了。一段时间后，当IO返回结果时，再通知CPU进行处理，这种情况称为异步IO。
  
* 异步IO模型需要一个消息循环，在消息循环中，主线程不断地重复“读取消息-处理消息”这一过程，在消息模型中，处理一个消息必须非常迅速，否则，主线程将无法及时处理消息队列中的其他消息，导致程序看上去停止响应

        loop = get_event_loop()
        while True:
            event = loop.get_event()
            process_event(event)
    

**协程（Coroutine）**

* 定义：
        * 1、又称微线程，是单线程下的并发，是由用户程序自己控制调度的
        * 2、协程不是进程也不是线程，而是一个特殊的函数，这个函数可以在某个地方挂起，并且可以重新在挂起处外继续运行
        * 3、必须添加到事件循环中，然后由事件循环去运行，单独运行协程函数是不会有结果的
   
* 特点：

	* 1、是一个线程执行，不需要创建多线程，协程的执行是无序的
        * 2、执行效率高，因为子程序（函数）切换不是线程切换，而是由程序自身控制，因此没有线程切换的开销
        * 3、不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态

 * 使用方法：
        * 多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能
