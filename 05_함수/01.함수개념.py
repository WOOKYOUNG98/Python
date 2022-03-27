# 함수를 사용하는 이유

# 함수를 사용하지 않은 경우
print("안녕하세요. 우경님")
print("현재 프리미엄 서비스 사용기간이 30일 남았습니다.")

print("안녕하세요. 민수님")
print("현재 프리미엄 서비스 사용기간이 15일 남았습니다.")

print("안녕하세요. 영희님")
print("현재 프리미엄 서비스 사용기간이 7일 남았습니다.")

# 함수를 사용한 경우
def printMessage(name, data):
    print("안녕하세요. ", name, "님")
    print("현재 프리미엄 서비스 사용기간이", data, "일 남았습니다.")

printMessage("우경", 30)
printMessage("민수", 15)
printMessage("길동", 5)


