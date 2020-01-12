import copy
import pickle
import json
from collections import namedtuple


'''
序列化与反序列化（json、pickle、shelve）
我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
https://www.cnblogs.com/gcgc/p/10973418.html
'''


output_file1 = '/home/pc190559/demo/pickle.txt'
output_file2 = '/home/pc190559/demo/data.json'


print("===== pickle 序列化&反序列化 =====")


# 对象序列化到文件对象，就是存入文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
data2 = [1, 2, 3]
output = open(output_file1, 'wb')
pickle.dump(data1, output)
pickle.dump(data2, output)
output.close()


# 对象反序列化，从文件读取数据
pkl_file = open(output_file1, 'rb')
data1 = pickle.load(pkl_file) # 一次只能读取一行
print(data1)
pkl_file.close()

# 读取所有内容
def func():
    with open(output_file1, 'rb') as input_file: # 自动关闭文件流
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


print("===== json 序列化&反序列化 =====")


python_data = {'a':'str', 'c': True, 'e': 10, 'b': 11.1, 'd': None, 'f': [1, 2, 3], 'g':(4, 5, 6)}

json_data = '{"default":{"a":"test"}, "c": true, "b": 11.1, "e": 10, "d": null, "g": [4, 5, 6], "f": [1, 2, 3]}'

print(json.dumps(python_data,sort_keys=True)) # python数据转json格式

print(json.loads(json_data)) # json数据转python格式


with open(output_file2,'w') as output_file:
    json.dump(python_data,output_file) # 序列化python数据到json文件

with open(output_file2,'r') as input_file:
    data = json.load(input_file) # 反序列化json文件到python数据
    print(data,type(data))


'重点注意：json 序列化&反序列实例对象'

'序列化：Python对象 --> dict --> JSON object'


class Teacher:

    def __init__(self):
        self.name = ""
        self.age = 0
        self.sex = ""
        self.score = 0


t1 = Teacher()
t1.name= "teacher1"
t1.age= 30
t1.sex = "男"

t2 = copy.deepcopy(t1)
t2.name = "teacher2"
t2.sex = "女"
t2.score = 90
t2.temp = "test"



temp1 = json.dumps(t1,ensure_ascii=False,default=lambda obj:obj.__dict__) # 传入实例对象属性 t1.__dict__

temp2 = json.dumps(t2,ensure_ascii=False,default=lambda obj:obj.__dict__)

print(temp1)
print(temp2)


'反序列化的过程是“JSON object -> dict --> Python对象'


json_data = '{"name":"test","age":20,"sex":"男","grade":[1,2,3],"score":{"math":90,"computer":95},"books":[{"name":"math","type":"study"},{"name":"The Little Prince","type":"literature"}]}'

print("====== 使用元祖解析json数据 =====")

Book = namedtuple('Book', ['name', 'type'])
Score = namedtuple('Score', ['math', 'computer'])
User = namedtuple('User', ['name', 'age', 'sex','grade','score','books'])

data = json.loads(json_data)

u = User(**data) #　必须保证json数据中的key值与对象属性名个数、名称一致
s = Score(**u.score)
print(u)
print(s)
book_list = u.books
for book in book_list:
    b = Book(**book)
    print(b)


print("====== 使用字典解析json数据 =====")


class Dict:

    def __init__(self, data):
        self.__dict__ = data

d = json.loads(json_data,object_hook=Dict)

print(d)
print(d.score)
print(d.books)
