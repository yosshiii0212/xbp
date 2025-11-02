for i in range(1,3): #コロンが入っていることに注意
    print(i,"人目") #タブでずらしていることに注意！
    name=input("名前を教えてください")
    waist=float(input("胸囲は"))
    age=int(input("年齢は"))

    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

    if waist>84 :
        if age> 44  :
            print(name,"さん、内臓脂肪蓄積注意です")
        else:
            print(name,"さん、腹囲は問題ありません")
    else:
        print(name,"さん、そのまま強く生きてください")

