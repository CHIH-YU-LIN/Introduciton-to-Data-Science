x = int(input("請輸入起始的整數:"))
y = int(input("請輸入終止的整數:"))
i = x # start
while i <= y: # stop
    # task
    if i % 2 == 1:
        print(i)
    i += 1 # step

x = int(input("請輸入起始的整數:"))
y = int(input("請輸入終止的整數:"))
odd_counter = 0 # 歸零
i = x # start
while i <= y: # stop
    # task
    if i % 2 == 1:
        #odd_counter = odd_counter + 1 # = NOT ==
        odd_counter += 1 # 計數累計
    #print(odd_counter)
    i += 1 # step
print("======")
print(odd_counter)

x = int(input("請輸入起始的整數:"))
y = int(input("請輸入終止的整數:"))
odd_summation = 0 # 歸零
i = x # start
while i <= y: # stop
    # task
    if i % 2 == 1:
        odd_summation = odd_summation + i # 數值累加
    i += 1 # step
print("======")
print(odd_summation)

x = int(input("請輸入起始的整數:"))
y = int(input("請輸入終止的整數:"))
odd_summation = 0 # 歸零
odd_counter = 0
i = x # start
while i <= y: # stop
    # task
    if i % 2 == 1:
        odd_counter += 1 # 計數累計
        odd_summation += i # 數值累加
        print("現在的整數是:{}, 奇數計數為{}個, 總和為{}".format(i, odd_counter, odd_summation))
    else:
        print("現在的整數是:{}, 奇數計數為{}個, 總和為{}".format(i, odd_counter, odd_summation))
    i += 1 # step
print("======")
print(odd_counter)
print(odd_summation)

x = int(input("請輸入一個正整數:"))
i = 1 # start
divisor_counter = 0 # 歸零
while i <= x: # stop
    if x % i == 0:
        divisor_counter += 1
        print("{}可以被{}整除".format(x, i))
        print("因數個數目前有{}個".format(divisor_counter))
        print("======")
    i += 1 # step
print("### Answer ###")
print("總共執行了{}次迴圈".format(i - 1))
print("{}共有{}個因數".format(x, divisor_counter))
if divisor_counter == 2:
    print("{}是質數".format(x))
else:
    print("{}不是質數".format(x))

x = int(input("請輸入一個正整數:"))
i = 1 # start
divisor_counter = 0 # 歸零
while i <= x: # stop
    if x % i == 0:
        divisor_counter += 1
        print("{}可以被{}整除".format(x, i))
        print("因數個數目前有{}個".format(divisor_counter))
        print("======")
    i += 1 # step
    if divisor_counter > 2:
        break
print("### Answer ###")
print("總共執行了{}次迴圈".format(i - 1))
if divisor_counter == 2:
    print("{}是質數".format(x))
else:
    print("{}不是質數".format(x))

i = 1 # start
while i <= 100: # stop
    if i % 15 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1 # step
