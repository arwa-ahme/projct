x = int(input("num of list: "))
l = []
even = 0
odd = 0

for i in range(x):
    y = int(input("list: "))
    l.append(y)
    if y % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"the even numbers is {even}\n and the odd numbers is {odd}")

