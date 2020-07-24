'''调用数据方法'''
import csv


def read_txt(file_name):
    with open(file_name,"r+",encoding="utf-8") as f:
        lines = f.readlines()
        data_list = []
        print(lines)
        for line in lines:
            line = line.split()
            data_list.append(line)
        return data_list
# r = read_txt()
# print(r)

def read_csv(file_name):
    with open(file_name,'r',encoding="utf-8") as f:
        data = csv.reader(f)
        lst = []
        for user in data:
            user = user[0].split()
            lst.append(user)
        return lst
# data = read_csv(r"D:\git_root\5kCRM\data\business.csv")
# print(data)