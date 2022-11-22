import random
import datetime

def main():
    shutudai()
    kaitou()

def shutudai():
    global qst,ans
    mondai={"「木耳」はなんと読む？":["きくらげ","キクラゲ"],
    "私は朝何を食べたでしょうか？":["米","ライス","お米","こめ","コメ"],
    "ゴリラと私、どちらが強い？":["ゴリラ","ごりら","gorilla"]}

    qst,ans=random.choice(list(mondai.items()))
    print(qst)

def kaitou():
    st = datetime.datetime.now()
    my_ans=input("答えは…：")
    if my_ans in ans:
        print("正解!!!")
    else:
        print("はずれ")
    ed = datetime.datetime.now()
    print((ed-st).seconds+"秒")
    
if __name__=="__main__":
    
    main()