# 실습문제 5.1.4

k = int(input('국어 >>>'))
m = int(input('수학 >>>'))
e = int(input('영어 >>>'))

total = k + m + e
avg = total / 3

# 방법 1
if 0 <= k <= 100 and 0 <= m <= 100 and 0 <= e <= 100 :
    if avg >= 80:
        print("불합격")
    else:
        print("합격")
else:
    print("잘못 입력하였습니다!")

# 방법 2
if k < 0 or k > 100 or m < 0 or m > 100 or e < 0 or e > 100:
    print("잘못 입력하였습니다.")
elif avg >= 80:
    print("불합격")
else:
    print("합격")