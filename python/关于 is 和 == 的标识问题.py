# （1）只要是变量的值相同，标识都相同，没有-5~256的限制，看下面的例子：
a = 100000000000000000000000000000000000000000000000
b = 100000000000000000000000000000000000000000000000
if a is b:
    print('a 和 b 标识相同，标识为：', id(a))
else:
    print('a 和 b 标识不相同,a 标识为：', id(a), 'b 标识为：', id(b))

# （2）同样的如果是负数，仍然没有上述限制：
a = -100000
b = -100000
if a is b:
    print('a 和 b 标识相同，标识为：', id(a))
else:
    print('a 和 b 标识不相同,a 标识为：', id(a), 'b 标识为：', id(b))

# （3）列表也是一样的，只要是列表项数值一样，那么标识也是一样的。例子如下：
list1 = [10000, 20000, 30000]
list2 = [10000, 12000, 15000]
if list1[0] is list2[0]:
    print('list1[0] 和 list2[0] 标识相同，标识为：', id(list1[0]))
else:
    print('list1[0] 和 list2[0] 标识不相同,list1[0]标识为：', id(list1[0]), 'list2[0]标识为：', id(list2[0]))

# （4）元组的标识是跟着变量名的，变量名不一样，标识也不一样，上例子：
# tuple1 = (10000, 20000, 30000) # 两者id不同
# tuple2 = (10000, 12000, 15000)
tuple1 = ("test", 20000, 30000)  # 两者id相同
tuple2 = ("test", 12000, 15000)
if tuple1[0] is tuple2[0]:
    print('tuple1[0] 和 tuple2[0] 标识相同，标识为：', id(tuple1[0]))
else:
    print('tuple1[0] 和 tuple2[0] 标识不相同,tuple1[0] 标识为：', id(tuple1[0]), 'tuple2[0]标识为：', id(tuple2[0]))

# （5）字典和列表是一样的，只要是列表项数值一样，那么标识也是一样的。例子如下：
dict1 = {1: 10000, 2: 20000, 3: 30000}
dict2 = {1: 10000, 2: 12000, 3: 15000}
if dict1[1] is dict2[1]:
    print('dict1[1] 和 tuple2[1] 标识相同，标识为：', id(dict1[1]))
else:
    print('dict1[1] 和 tuple2[1] 标识不相同,dict1[1] 标识为：', id(dict1[1]), 'tuple2[1] 标识为：', id(dict2[1]))

original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
original_dict = {1: [0, 1, 2, 3, 4, 5, 6, 7, 8]}
copy_list = original_list.copy()
copy_dict = original_dict.copy()
for i in range(5):
    copy_list[i] = 0
    copy_dict[1][i] = 0
copy_list = copy_list + ['a', 'b', 'c']
print("original_list:", original_list)
print("copy_list modify:", copy_list)
print("original_dict:", original_dict)
print("copy_dict modify:", copy_dict)
