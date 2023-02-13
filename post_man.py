from random import randint
import matplotlib.pyplot as plt

ran = []
for _ in range(1000):
    initial, final = 0, 1000
    num = [randint(initial, final)]

    max_iter = 0
    while True:
        try:
            if num[-1]%2 == 0:
                num.pop(0)
            else:
                num.append(randint(initial, final))

            # print(len(num))
            max_iter += 1
            if len(num) == 0:
                print(f"End Loop, Max iter : {max_iter}")
                ran.append(max_iter)
                break
        except KeyboardInterrupt:
            break

plt.plot(ran, "o")
plt.show()