
import sys

print("===== 文件读取 =====")


output_file = sys.path[0]+'/test.txt'

f = open(output_file, "w+")  # 创建文件

f.write("测试\nPython\n文件读写\n")  # 写入数据
value = ('www.runoob.com', 14)
f.write(str(value))

f = open(output_file, "r+")
# print(f.read())  # 读取所有内容
# print(f.readline()) # 读取一行内容
data = f.readlines() # 读取所有数据，返回列表
print(data)
print({s.replace("\n", "") for s in data})
f.close()
