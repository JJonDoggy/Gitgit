x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())
x_3, y_3 = map(int, input().split())

x_4 = max(x_1, x_2, x_3)
y_4 = max(y_1, y_2, y_3)

myList1 = [x_1, x_2, x_3]
myList2 = [y_1, y_2, y_3]

if myList1.count(x_4) >= 2:
    x_4 = min(x_1, x_2, x_3)
if myList2.count(y_4) >= 2:
    y_4 = min(y_1, y_2, y_3)
print(x_4, y_4)
