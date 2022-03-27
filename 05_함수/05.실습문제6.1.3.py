import random

def getRandomNumber():
    number = random.randint(1, 45)
    return number

lotto_num = [] # 로또번호가 들어갈 빈 리스트 생성

count = 0 # 6회 횟수를 세는 변수 생성

while True:
    if count == 6 :
        break
    g_r_n = getRandomNumber()
    if g_r_n not in lotto_num:
        lotto_num.append(g_r_n)
        count +=1

lotto_num.sort()
for num in lotto_num :
    print(num, end = " ")