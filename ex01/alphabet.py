import random,string

def main():
    global count
    count=1
    kaitou()
    print("挑戦回数"+str(count))

def genemoji(n):
    global mojilis,after_moji,kessonmoji
    mojilis=[random.choice(string.ascii_uppercase) for i in range(n)]
    after_moji=random.sample(mojilis,random.randint(2,len(mojilis)-1))
    kessonmoji=list(set(mojilis)^set(after_moji))

def shutudai():
    print("対象文字\n"+" ".join(mojilis))
    print("欠損文字\n"+" ".join(kessonmoji))
    print("表示文字\n"+" ".join(after_moji))

def kaitou():
    global count
    n=1 #ループを止めるスイッチ
    while n==1:
        #文字列の生成～出題
        genemoji(random.randint(3,8))
        shutudai()
        print(len(kessonmoji))
        ans1=input("欠損文字はいくつあるでしょうか?\n")       
        #文字数の判定
        if ans1 != str(len(kessonmoji)):
            print("不正解です、またチャレンジしてください")
            count+=1
            continue
        print("正解です。具体的文字を入力してください(1文字ずつ)")
        #欠損文字を入力させる（失敗したら24行目に戻る）
        while True:
            ans2=input()
            if ans2 not in kessonmoji:
                count+=1
                print("不正解です、またチャレンジしてください")
                break
            else:
                kessonmoji.remove(ans2)
                if len(kessonmoji)==0:
                    print("正解、おわり")
                    n=0
                    break
        continue

if __name__=="__main__":
    main()