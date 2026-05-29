import random

print("选择难度: 1=简单(1-50)  2=中等(1-100)  3=困难(1-200)")
level = input("输入 1/2/3: ")

limits = {"1": 50, "2": 100, "3": 200}
limit = limits.get(level, 100)

answer = random.randint(1, limit)
tries = 0
max_tries = 10

print(f"猜一个 1 到 {limit} 之间的数字，你只有 {max_tries} 次机会")

while tries < max_tries:
    guess = int(input("你的猜测: "))
    tries += 1

    if guess < answer:
        print("太小了！")
    elif guess > answer:
        print("太大了！")
    else:
        print(f"猜对了！你用了 {tries} 次。")
        break
else:
    print(f"机会用完了！答案是 {answer}")
