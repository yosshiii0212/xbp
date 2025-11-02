# 敵のHP
name = input("名前を入力してください。")
enemy1 = "スライム HP3"
warned = False  # 「もう1度入力してください」を1回しか出さないためのフラグ
print(name, "は", enemy1, "とぶつかった")
print("バトル開始!")

import random
level = 1  # 現在のレベル
lose_threshold = 3  # この値を出すと負けになるコマンド

# ---- スライム戦 ----
while True:
    hp = 3 + level * 2
    attack = input("'攻撃'と入力してください：")
    if attack == "攻撃":
        damage = random.randint(1, 10)
        print("攻撃しました！ダメージは", damage, "です。")
        if damage >= 3:
            print("敵を倒した！次のステージに行きます。")
            print("レベル2")
            level = 2
        else:
            print("攻撃が足らない。あなたの負け")
            level = 1  # ここでリセット
        break
    else:
        if not warned:
            print("そのコマンドは認識されません。もう一度入力してください。")
            warned = True

# ---- ゴブリン戦 ----
enemy2 = "ゴブリン HP5"
print(name, "は", enemy2, "とぶつかった")
print("バトル開始！")

warned = False
while True:
    hp = 5 + level * 2
    attack = input("'攻撃'と入力してください：")
    if attack == "攻撃":
        damage = random.randint(1, 10)
        print("攻撃しました！ダメージは", damage, "です。")
        if damage >= 5:
            print("敵を倒した！次のステージに行きます。")
            print("レベル3")
            level = 3
        else:
            print("攻撃が足らない。あなたの負け")
            level = 1  # ここでリセット
        break
    else:
        if not warned:
            print("そのコマンドは認識されません。もう一度入力してください。")
            warned = True

# ---- ゴーレム戦 ----
enemy3 = "ゴーレム HP7"
print(name, "は", enemy3, "とぶつかった")
print("バトル開始！")

warned = False
while True:
    hp = 7 + level * 2
    attack = input("'攻撃'と入力してください：")
    if attack == "攻撃":
        damage = random.randint(1, 10)
        print("攻撃しました！ダメージは", damage, "です。")
        if damage >= 7:
            print("敵を倒した！次のステージに行きます。")
            print("レベル4")
            level = 4
        else:
            print("攻撃力が足らない。あなたの負け")
            level = 1  # ここでリセット
        break
    else:
        if not warned:
            print("そのコマンドは認識されません。もう一度入力してください。")
            warned = True

# ---- ドラキュラ戦 ----
enemy4 = "ドラキュラ HP8"
print(name, "は", enemy4, "とぶつかった")
print("バトル開始！")

warned = False
while True:
    hp = 8 + level * 2
    attack = input("'攻撃'と入力してください：")
    if attack == "攻撃":
        damage = random.randint(1, 10)
        print("攻撃しました！ダメージは", damage, "です。")
        if damage >= 8:
            print("敵を倒した！次のステージに行きます。")
            print("レベルMAX")
            level = 5
        else:
            print("攻撃力が足らない。あなたの負け")
            level = 1  # ここでリセット
        break
    else:
        if not warned:
            print("そのコマンドは認識されません。もう一度入力してください。")
            warned = True

# ---- 魔王戦（ラスト）----
enemy5 = "ラスボス魔王 HP10"
print(name, "は", enemy5, "とぶつかった！")
print("ファイナルバトル開始！")

warned = False
while True:
    hp = 10 + level * 2
    attack = input("'攻撃'と入力してください：")
    if attack == "攻撃":
        damage = random.randint(1, 10)
        print("攻撃しました！ダメージは", damage, "です。")
        if damage >= 10:
            print("魔王を倒した！！")
            print("ゲームクリア！！おめでとう！！🎉")
        else:
            print("攻撃力が足らない…あなたの負け。")
            level = 1  # 最後もリセット
        break
    else:
        if not warned:
            print("そのコマンドは認識されません。もう一度入力してください。")
            warned = True
