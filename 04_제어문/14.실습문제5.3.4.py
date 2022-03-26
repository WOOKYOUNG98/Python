# 실습문제 5.3.3
# Learning Korean
# 전체 문제 개수와 맞힌 문제, 틀린 문제 개수 출력까지 기능 추가 !

# 한국어 리스트
word_list = ["사랑해", "귀엽다", "고마워", "행복해"]

# 점수
score = 0

print("Let's Learning Korean")
for word in word_list:
    print(word)
    data = input()
    if data == word: # 문제를 맞힐 경우
        score += 1 # 점수를 1씩 증가 !

print("전체 문제 개수 : ", len(word_list))
print("맞힌 개수 : ", score)
print("틀린 개수 : ", len(word_list)- score)
    