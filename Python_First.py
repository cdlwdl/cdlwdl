#导入random模块
import random

#随机产生IP地址四个段落的数字
IP_section1 = random.randint(0,255)
IP_section2 = random.randint(0,255)
IP_section3 = random.randint(0,255)
IP_section4 = random.randint(0,255)
#生成随机IP
random_IP = str(IP_section1) + '.' + str(IP_section2) + '.' + str(IP_section3) + '.' + str(IP_section4)

#打印输出结果
print(random_IP)

#计算1+2的结果
print(1+2)

