from time import sleep
current_floor= eval(input("輸入現在所在樓層，若不想搭乘請輸入-1"))
max_floor=7
min_floor=1
a="電梯開門"
b="電梯關門"

while current_floor==str(current_floor):
    print("格式錯誤，請輸入數字\n")
    sleep(0.5)
    current_floor= eval(input("輸入現在所在樓層，若不想搭乘請輸入-1"))
else:        
    while current_floor != int(current_floor):
        print("格式錯誤，請輸入數字\n")
        sleep(0.5)
        current_floor= eval(input("請輸入整數"))
    else:
        print()
while current_floor == int(current_floor):
    if current_floor == -1:
        break
    elif current_floor>7 or current_floor<0:
        current_floor= eval(input("請輸入介於"+str(min_floor)+"-"+str(max_floor)+"的整數\n"))
    else:
        break
while current_floor != -1:
    target_floor=eval(input("您現在在"+str(current_floor)+"樓"+" 請問要前往哪一樓?(可選擇1-7樓,若不想搭乘請輸入-1)"))
    try: 
        target_floor==int(target_floor)
    except:
        print("格式錯誤，請輸入數字\n")
        sleep(0.5)
        continue
    if current_floor == -1:
        break
    elif target_floor == -1:
        break
    elif target_floor<1 or target_floor>7:
        print ("請輸入介於"+str(min_floor)+"-"+str(max_floor)+"的整數\n")
        sleep(0.5)
        continue
    elif target_floor == current_floor:
        print("你已在"+str(current_floor)+"樓層")
        sleep(0.5)
        continue
    elif target_floor < current_floor:
        print(b)
        sleep(0.5)
        print("電梯下樓")
        for i in range(target_floor, current_floor):
            print(current_floor)
            current_floor -=1
            sleep(0.5)
        print(current_floor)
        print(a)
    else:
        print(b)
        sleep(0.5)
        print("電梯上樓")
        for i in range(current_floor, target_floor):
            print(current_floor)
            current_floor +=1
            sleep(0.5)
        print(current_floor)
        print(a)
print(b+"，歡迎下次再搭乘電梯")
    
    
    
    