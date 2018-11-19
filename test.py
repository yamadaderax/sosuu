"""
--問題--
一万までの数字の中から、素数を見つけるシステムをつくれ
"""


sosuu = [2]
def find_sosuu():
    num = 3

    counter = 0
    while num < 10000:
        if num % 2 == 0:
            counter += 1
            pass
        else:
            for i in range(num):
                i += 1
                if i == 1 or i == num:
                    pass
                else:
                    s = num % i
                    if s == 0:
                        counter += 1
                        break
                    else:
                        pass
        if counter == 0:
            sosuu.append(num)
        counter = 0
        num +=1
    # print(sosuu)

"""
--テスト--
１ネットで検索した素数一覧表をコピペしたテキストファイルを読み込む
２上で書いたプログラムが作った素数リストと照らし合わせて検証
３正解ならsucceedと出力する
"""

with open('sosuu.txt','r')as f:
    num = f.read()
    new_num = num.split()
    new_num = [int(i) for i in new_num]
# print(new_num)

find_sosuu()

miss_counter = 0

for i in range(len(sosuu)):
    if sosuu[i] == new_num[i]:
        pass
    if sosuu[i] != new_num[i]:
        print("miss:{}".format(sosuu[i]))
        miss_counter += 1
if miss_counter == 0:
    print("Succeed!!")
    print("miss_counter:" + str(miss_counter))
else:
    print("miss_counter:" + str(miss_counter))
