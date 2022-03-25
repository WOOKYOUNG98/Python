# 1. 대입연산
# 변수이름 = 데이터

# 2. 산술연산
# - 숫자연산
x = 5
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)

# - 문자열연산
tag1 = "#할수있다"
tag2 = "#열심히 해보자"
tag3 = "#아자아자 파이팅!"

tag = tag1 + tag2 + tag3
print(tag)

message = "파이썬을 사랑합시다 \n" * 5
print(message)

# 복합할당연산자
level = 10 # (레벨 1 증가)
level += 1 # level = level + 1

health = 2000 # (체력 300 감소)
health -= 300 # health = health - 300

attack = 300
attack *= 1.5 # attack = attack * 1.5 

speed = 420
speed /= 2 # speed = speed / 2
print(level, health, attack, speed)