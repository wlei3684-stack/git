import random

print("=== 猜数字游戏 ===")
print("选择难度: 1=简单(1-30)  2=中等(1-100)  3=困难(1-200)")
level = input("输入 1/2/3: ")

limits = {"1": 30, "2": 100, "3": 200}
limit = limits.get(level, 100)
max_tries = {"1": 5, "2": 8, "3": 12}.get(level, 8)

answer = random.randint(1, limit)
tries = 0

print(f"范围 1~{limit}，你有 {max_tries} 次机会\n")

while tries < max_tries:
    try:
        guess = int(input(f"第 {tries + 1} 次猜测: "))
    except ValueError:
        print("⚠ 请输入数字！")
        continue
    tries += 1

    if guess < answer:
        print("↑ 太小了！")
    elif guess > answer:
        print("↓ 太大了！")
    else:
        print(f"\n🎉 猜对了！你用了 {tries} 次。")
        break
else:
    print(f"\n💥 机会用完了！答案是 {answer}")

score = max(0, (max_tries - tries + 1) * 10)
print(f"得分: {score}")

again = input("\n再来一局？(y/n): ")
if again.lower() == "y":
    print("重新运行程序吧！")
