Num = int(input())
divide = 2
while True:
    if (Num % divide) == 0:
        print(divide)
        Num /= divide
    else:
        divide += 1
    
    if Num <= 1:
        break
    