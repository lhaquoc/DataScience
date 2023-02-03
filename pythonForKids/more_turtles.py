import turtle
t = turtle.Pen()
# t.reset()
# for x in range(1, 9):
#     t.forward(100)
#     t.left(225)

# i = int(input('Enter 1 to continue'))
# t.reset()
# if i == 1:
#     for x in range(1, 38):
#         t.forward(100)
#         t.left(175)
# i = int(input('Enter 2 to countinue'))
# t.reset()
# if i == 2:
#     for x in range(1, 38):
#         t.forward(100)
#         t.left(175)
# i = int(input('Enter 3 to countinue'))
# t.reset()
# if i == 3:
#     for x in range(1, 20):
#         t.forward(100)
#         t.left(95)

# t.reset()

for x in range(1, 19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)
