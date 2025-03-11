
# # 一串数字
# a_str=input()
#
# # 要求：计算 a_str中数字出现的次数
#
# for num in set(a_str):
#     if num!=-1:
#         temp=a_str.count(num)
#         # print(temp,num)
#         print(f'{temp}'+f"{num}",end='')


# S=input()
# T=input()
# same=0
# for t in T:
#     if t in S:
#       same+=1
#       S=S[S.index(t)+1:]
#     else:
#       break
# print(same)

# n=int(input())
# a=list(input().split())
# for num in a:
#   if num=='0':
#       a.append('0')
#       a.remove('0')
# print(n,' '.join(a),sep='\n')


# l,w=2019,324
# count1=2019//324
# count2=324//(2019-count1*324)
# count3=75//(324-count2*75)
# count4=24//(75-count3*24)
# count5=(24//3)*2
# print(count1,count2,count3,count4,count5,(count1*324*324+count2*(2019-count1*324)^2+count3*(324-count2*75)^2+count4*(75-count3*24)^2+count5*3*3*2),2019*324)
# print((2019-count1*324),324-count2*75,75-count3*24,24-count4*3)
# print(count1+count2+count3+count4+count5)


# l,w=2019,324
# count=0
# while l!=w:
#     l=l-w
#     if l<w:
#         l,w=w,l
#     count+=1
# print(count+1)

#ord 转换为ASCII码
#chr ASCII码转换为对应的数字或字母
# print(ord('L'))


# millisecondes=1618708103123 #毫秒
# secondes= millisecondes // 1000   #秒
# hours=secondes//60//60%24 #时
# mins=secondes//60%60 #分钟
# ss=secondes%60
# print(f'{hours:02d}:{mins:02d}:{ss:02d}')


# import datetime #单是这类型是导入的只是该库，并没有使用到该库中的对象
# from datetime import datetime
# millisecondes=1618708103123
# secondes=millisecondes//1000
# # utcfromtimestamp 在调用时要么使用对象类去调用，要么使用导入的函数去调用
# dt=datetime.utcfromtimestamp(secondes)
# print(dt.strftime('%H:%M:%S'))

# t=[]
# temp=1
# while temp:
#   lists=list(map(int,input().split()))
#   if lists[0]==0 and lists[1]==0 and lists[2]==0:
#     temp=0
#   else:
#     t.append(lists)
# print(t)


# days=[]
# #一年各月份所含天数(平年)，闰年的2月是29天
# md=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# while True:
#     y,m,d=map(int,input().split()) # y年  m月 d日
#     if (y,m,d)==(0,0,0):
#         break
#     if y%4==0 and y%100!=0 or y%400==0:
#         md[1]=29
#     days.append(sum(md[:m-1],d))
# print(days)
# for day in days:
#     print(day)


# n = input()
# magic = list(map(int, input().split()))
# red, blue, green = magic.count(0), magic.count(1), magic.count(2)
# temp = (blue * 2 + green * 1, red * 1 + green * 2, red * 2 + blue * 1)
# print(min(temp))


# words=input()
# for word in words:
#   if word in 'aeiou':
#     print(word.upper(),end='')
#   else:
#     print(word,end='')


# import datetime
# # 开始日期
# start_date = datetime.date(2022, 1, 1)
# # 结束日期 2022非闰年 365天   timedelta对象定义天数长度
# end_date = start_date + datetime.timedelta(days=365)
# # 计算跑步天数
# run = 0
# # single_date 遍历到的每一天
# print((start_date + datetime.timedelta(n) for n in range(365)))
# for single_date in (start_date + datetime.timedelta(n) for n in range(365)):
#   # 判断每月中的1、11、21、31号 和周六周天  single_date.weekday()中5代表周六，6代表周天
#     print(single_date)
#     if single_date.day % 10 == 1 or single_date.weekday() in (5,6):
#         run += 1
# print(run)


# 暴力枚举法：

# # 读取输入的记录数量
# n = int(input())
# # 读取由 1 和 -1 构成的记录序列，并将其转换为整数列表
# records = list(map(int, input().split()))
#
# # 用于存储合法连续子序列的数量
# count = 0
#
# # 外层循环，确定子序列的起始位置
# for i in range(n):
#     # 内层循环，确定子序列的结束位置
#     for j in range(i, n):
#         # 用于记录当前子序列的商品数量平衡情况
#         balance = 0
#         # 标记当前子序列是否合法
#         valid = True
#         # 遍历当前子序列中的每个记录
#         for k in range(i, j + 1):
#             # 更新商品数量平衡
#             balance += records[k]
#             # 如果商品数量为负数，说明在卖出商品时商店里没有商品，该子序列不合法
#             if balance < 0:
#                 valid = False
#                 break
#         # 如果子序列合法且结束时商品数量为 0，则该子序列是合法的
#         if valid and balance == 0:
#             count += 1
#
# # 输出合法连续子序列的数量
# print(count)

# n=int(input())
# res=[]
# for i in range(n):
#   b,y=map(int,input().split())
#   if b>y:
#     res.append('YI')
#   elif b<y:
#     res.append('BRIDGE')
#   else:
#     res.append('ANY')
# print(res)
# for i in res[::-1]:
#   print(i)



# n,d=map(int,input().split())
# level=list(map(int,input().split()))
# danger=0
# nomal=0
# days=0
# for peo in level:
#     if peo<=9 or peo>=80:
#         danger+=1
#     else:
#         nomal+=1
# while danger>0 or nomal>0:
#     if danger>0:
#         danger-=d
#         days+=1
#     if nomal>0:
#         nomal-=d
#         days+=1
# print(days)


# d,c=map(int,input().split())
# one=sum(list(map(int,input().split())))
# two=sum(list(map(int,input().split())))
#
# if one>=150 and two>=150 and c<2*d:
#     print('YES')
# elif (one>=150 or two>=150) and c<d:
#     print("YES")
# else:
#     print('NO')

# 30 45
# 100 100 100
# 10 20 30



# import time
#
# def fibonacci(n):
#     if n < 2:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# def dyna_fibonacci(n):
#     if n < 2:
#         return n
#     else:
#         a, b = 0, 1
#         for _ in range(n - 1):
#             a, b = b, a + b
#         return b
#
# t1 = time.time()
# print(fibonacci(30))
# t2 = time.time()
# print(dyna_fibonacci(30))
# t3 = time.time()
# print("Time required for using recursion:", t2 - t1)
# print("Dynamic Planning Duration:", t3 - t2)



from typing import List


def maxProfit(prices: List[int]) -> int:
    '''
    思路： 从最后一个点4分析，如果4要获得最大利润，那么要获取其前面最小值，才能获取最大利润
    即可以得到递推式为:f(4)=max(f(6),4-最小金额）
    动态规划:
    边界点：f(1)=0
    最优子结构：f(4)的为f(6)
    状态转移方程：f(4)=max(f(6),4-最小金额）
    '''
    min_value = prices[0]
    max_profit = [0 for i in prices]
    print(max_profit)
    for i in range(1, len(prices)):
        if prices[i] < min_value:
            min_value = prices[i]
        max_profit[i] = max(max_profit[i - 1], prices[i] - min_value)
    return max_profit[-1]
print(maxProfit(prices=[7,1,5,3,6,4]))