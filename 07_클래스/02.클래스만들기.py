class Monster:
    def say(self):
        print('나는 몬스터다! 크오오!')

goblin = Monster()
goblin.say()

# 파이썬에서는 자료형도 클래스다
a = 10  #type(a) = <class 'int'>
b = "문자열객체"
c = True

print(b.__dir__())