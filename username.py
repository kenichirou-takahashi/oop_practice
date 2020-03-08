'''
データ型宣言:Ussrname
    属性：
      実際のユーザー名
    ルール：
      ユーザー名は４文字以上２０文字以下
    できること＝＞メソッド
      ユーザー名を大文字に変換する
'''


class Username:
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError(f'{name}の文字数はルール違反ですよ！')

        self.name = name

    def screen_name(self):
        return self.name.upper()


# Usernameクラスのインスタンス化
hibiki = Username(name='hibiki')

print(hibiki.screen_name())

# print(hibiki)
# print(type(hibiki))
# print(hibiki.name) #hibiki
print(hibiki.name.upper())
print(hibiki.screen_name())

# sho = Username('sho')
# print(sho.name)
