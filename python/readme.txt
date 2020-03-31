
空格的使用

1、使用空格来表示缩进而不要用制表符（Tab），在Python中分支和循环结构都使用缩进来表示哪些代码属于同一个级别，鉴于此Python代码对缩进以及缩进宽度的
依赖比其他很多语言都强得多。在不同的编辑器中，Tab的宽度可能是2、4或8个字符，甚至是其他更离谱的值，用Tab来表示缩进对Python代码来说可能是一场灾难。
2、和语法相关的每一层缩进都用4个空格来表示。
3、每行的字符数不要超过79个字符，如果表达式因太长而占据了多行，除了首行之外的其余各行都应该在正常的缩进宽度上再加上4个空格。
4、函数和类的定义，代码前后都要用两个空行进行分隔。
5、在同一个类中，各个方法之间应该用一个空行进行分隔。
6、二元运算符的左右两侧应该保留一个空格，而且只要一个空格就好。


标识符命名

1、变量、函数和属性应该使用小写字母来拼写，如果有多个单词就使用下划线进行连接。
2、类中受保护的实例属性，应该以一个下划线开头。
3、类中私有的实例属性，应该以两个下划线开头。
4、类和异常的命名，应该每个单词首字母大写。
5、模块级别的常量，应该采用全大写字母，如果有多个单词就用下划线进行连接。
6、类的实例方法，应该把第一个参数命名为self以表示对象自身。
7、类的类方法，应该把第一个参数命名为cls以表示该类自身。


表达式和语句

1、采用内联形式的否定词，而不要把否定词放在整个表达式的前面。例如if a is not b就比if not a is b更容易让人理解。
2、不要用检查长度的方式来判断字符串、列表等是否为None或者没有元素，应该用if not x这样的写法来检查它。
3、就算if分支、for循环、except异常捕获等中只有一行代码，也不要将代码和if、for、except等写在一起，分开写才会让代码更清晰。
4、import语句总是放在文件开头的地方。
5、引入模块的时候，from math import sqrt比import math更好。
6、如果有多个import语句，应该将其分为三部分，从上到下分别是Python标准模块、第三方模块和自定义模块，每个部分内部应该按照模块名称的字母表顺序来排列。


Python编程惯例

1、让代码既可以被导入又可以被执行。

    if __name__ == '__main__':

2、用下面的方式判断逻辑“真”或“假”。

    if x:
    if not x:

    好的代码：

        name = 'jackfrued'
        fruits = ['apple', 'orange', 'grape']
        owners = {'1001': '骆昊', '1002': '王大锤'}
        if name and fruits and owners:
            print('I love fruits!')

    不好的代码：

        name = 'jackfrued'
        fruits = ['apple', 'orange', 'grape']
        owners = {'1001': '骆昊', '1002': '王大锤'}
        if name != '' and len(fruits) > 0 and owners != {}:
            print('I love fruits!')

3、善于使用in运算符。

    if x in items: # 包含
    for x in items: # 迭代

    好的代码：

        name = 'Hao LUO'
        if 'L' in name:
            print('The name has an L in it.')

    不好的代码：

        name = 'Hao LUO'
        if name.find('L') != -1:
            print('This name has an L in it!')

4、不使用临时变量交换两个值。

    a, b = b, a

5、用序列构建字符串。

    好的代码：

        chars = ['j', 'a', 'c', 'k', 'f', 'r', 'u', 'e', 'd']
        name = ''.join(chars)
        print(name)  # jackfrued

    不好的代码：

        chars = ['j', 'a', 'c', 'k', 'f', 'r', 'u', 'e', 'd']
        name = ''
        for char in chars:
            name += char
        print(name)  # jackfrued

6、使用enumerate进行迭代。

    好的代码：

        fruits = ['orange', 'grape', 'pitaya', 'blueberry']
        for index, fruit in enumerate(fruits):
            print(index, ':', fruit)

    不好的代码：

        fruits = ['orange', 'grape', 'pitaya', 'blueberry']
        index = 0
        for fruit in fruits:
            print(index, ':', fruit)
            index += 1

7、用生成式生成列表。

    好的代码：

        data = [7, 20, 3, 15, 11]
        result = [num * 3 for num in data if num > 10]
        print(result)  # [60, 45, 33]

    不好的代码：

        data = [7, 20, 3, 15, 11]
        result = []
        for i in data:
            if i > 10:
                result.append(i * 3)
        print(result)  # [60, 45, 33]

8、用zip组合键和值来创建字典。

    好的代码：

        keys = ['1001', '1002', '1003']
        values = ['骆昊', '王大锤', '白元芳']
        d = dict(zip(keys, values))
        print(d)

    不好的代码：

        keys = ['1001', '1002', '1003']
        values = ['骆昊', '王大锤', '白元芳']
        d = {}
        for i, key in enumerate(keys):
            d[key] = values[i]
        print(d)