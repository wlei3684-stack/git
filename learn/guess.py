import random

answer = random.randint(1, 100)
tries = 0

print("猜一个 1 到 100 之间的数字")

while True:
    guess = int(input("你的猜测: "))
    tries += 1

    if guess < answer:
        print("太小了！")
    elif guess > answer:
        print("太大了！")
    else:
        print(f"猜对了！你用了 {tries} 次。")
        break
