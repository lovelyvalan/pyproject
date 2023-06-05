a, b = 12, 5
if a + b:
    print('True')
else:
    print('False')

if -3:
    print("True")

# x = 0
# a = 5
# b = 5
# if a > 0:
#     if b < 0:
#         x = x + 5
#     elif a > 5:
#         x = x + 4
#     else:
#         x = x + 3
# else:
#     x = x + 2
# print(x)


x = 0
for i in range(10):
  for j in range(-1, -10, -1):
    x += 1
    print(x)

    numbers = [10, 20]
    items = ["Chair", "Table"]

    for x in numbers:
        for y in items:
            print(x, y)



print(bin(-10))

x = 0
while x > 10 and x <= 0:
    print()