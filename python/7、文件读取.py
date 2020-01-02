
# 文件读取

output_file1 = '/home/pc190559/demo/test.txt'
output_file2 = '/home/pc190559/demo/pickle.txt'
output_file3 = '/home/pc190559/demo/data.json'


f = open(output_file1, "w+")  # 创建文件

f.write("测试\nPython\n文件读写\n")  # 写入数据
value = ('www.runoob.com', 14)
f.write(str(value))

f = open(output_file1, "r+")
# print(f.read())  # 读取所有内容
# print(f.readline()) # 读取一行内容
str = f.readlines() # 读取所有数据，返回列表
print(str)
print({s.replace("\n", "") for s in str})
f.close()


# 序列化与反序列化（json、pickle、shelve）
# https://www.cnblogs.com/gcgc/p/10973418.html

# pickle 序列化&反序列化
import pickle

# 对象序列化到文件对象，就是存入文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
data2 = [1, 2, 3]
output = open(output_file2, 'wb')
pickle.dump(data1, output)
pickle.dump(data2, output)
output.close()

# 对象反序列化，从文件读取数据
pkl_file = open(output_file2, 'rb')
data1 = pickle.load(pkl_file) # 一次只能读取一行
print(data1)
pkl_file.close()

# 读取所有内容
def func():
    with open(output_file2, 'rb') as input_file: # 自动关闭文件流
        try:
            while True:
                data = pickle.load(input_file)
                print(data)
        except EOFError:
            input_file.close()

func()

python_data = {"a","b","c"}

pickle_data = b'\x80\x03cbuiltins\nset\nq\x00]q\x01(X\x01\x00\x00\x00cq\x02X\x01\x00\x00\x00aq\x03X\x01\x00\x00\x00bq\x04e\x85q\x05Rq\x06.'

print(pickle.dumps(python_data)) # python数据序列化成二进制格式

print(pickle.loads(pickle_data)) # 二进制格式反序列化成python数据


# json 序列化&反序列化

import json

python_data = {'a':'str', 'c': True, 'e': 10, 'b': 11.1, 'd': None, 'f': [1, 2, 3], 'g':(4, 5, 6)}

json_data = '{"default":{"a":"test"}, "c": true, "b": 11.1, "e": 10, "d": null, "g": [4, 5, 6], "f": [1, 2, 3]}'

print(json.dumps(python_data,sort_keys=True)) # python数据转json格式

print(json.loads(json_data)) # json数据转python格式


with open(output_file3,'w') as output_file:
    json.dump(python_data,output_file) # 序列化python数据到json文件

with open(output_file3,'r') as input_file:
    data = json.load(input_file) # 反序列化json文件到python数据
    print(data,type(data))
