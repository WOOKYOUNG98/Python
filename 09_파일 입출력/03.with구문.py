# with 구문을 사용하면 자동으로 file close 해준다.
with open("./myvenv/09_파일 입출력/data.txt", "r", encoding="utf8") as file:
    data = file.read()
    print(data)
