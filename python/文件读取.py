# 文件读取

dir = "d:\\test.txt"
f = open(dir, "w+")  # 创建文件

f.write("测试\nPython\n文件读写\n")  # 写入数据
value = ('www.runoob.com', 14)
f.write(str(value))

f = open(dir, "r+")
# print(f.read())  # 读取所有内容
# print(f.readline()) # 读取一行内容
str = f.readlines() # 读取所有数据，返回列表
print(str)
print({s.replace("\n", "") for s in str})
f.close()


# 序列化&反序列化
import pickle # pickle 模块：实现了基本的数据序列和反序列化

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
data2 = [1, 2, 3]
output = open('d:\\data.txt', 'wb')
pickle.dump(data1, output)
pickle.dump(data2, output)
output.close()


# 使用pickle模块从文件中重构python对象
pkl_file = open('d:\\data.txt', 'rb')
data1 = pickle.load(pkl_file)
print(data1)
data2 = pickle.load(pkl_file)
print(data2)
pkl_file.close()
