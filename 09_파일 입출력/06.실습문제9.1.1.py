import csv

def show_profit(data):
    name = data[0] # 종목
    purchase_price = int(data[1]) # 매입가
    amount = int(data[2]) # 수량
    target_price = int(data[3]) # 목표가

    profit = (target_price - purchase_price) * amount # 수익금
    profit_ratio = (target_price/purchase_price - 1) * 100 # 수익률

    print(f"{name} {profit} {profit_ratio:.2f}%")

# 파일 열기
file = open("./myvenv/09_파일 입출력/mystock.csv", "r", encoding="utf-8-sig")

# 파일 데이터 읽기
reader = list(csv.reader(file))
for data in reader[1:] :
    show_profit(data)


# 파일 쓰기
data = [
    ["종목", "매입가", "수량", "목표가"],
    ["삼성전자", 85000, 10, 90000],
    ["NAVER", 380000, 5, 400000]
]

file = open("./myvenv/09_파일 입출력/mystock.csv", "w", newline="", encoding="utf-8-sig")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file.close



