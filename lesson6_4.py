import random
def play_game():
    min=1
    max=100
    count=0
    target=random.randint(min,max)
    print("==========猜數字遊戲==========\n")
    print(f"猜數字的範圍:{min}~{max}")
    print(target)

    while True:
        try:
            guess=int(input(f"猜數字範圍:{min}~{max}: "))
        except:
            print("輸入格式錯誤")
            count+=1
            print(f"你已經猜了{count}次")
        else:
            count+=1
            if guess>=min and guess<=max:
                if guess==target:
                    print("恭喜!猜對了,答案是:",target)
                    print(f"你總共猜了{count}次")
                    break
                elif guess>target:
                    print(f"再小一點")
                    max=guess-1
                    
                    
                elif guess<target:
                    print("再大一點")
                    min=guess+1
                print(f"你已經猜了{count}次")
            else:
                print("輸入錯誤,輸入數字不在範圍內")
                print(f"你已經猜了{count}次")
while True:
    play_game()
    play_again=input("請問是否要繼續?y,n:")
  
    if play_again=='n':
        break
print("遊戲結束")

