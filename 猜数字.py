import random
counts = 3
answer = random.randint(1,10)
while counts > 0 :
	guess = int(input("猜数字"))
	if answer == guess:
		print("猜对了 666")
		break
	else:
		if answer < guess:
			print("笑了")
		else:
			print("打了")
		counts-=1

print("不玩了")

