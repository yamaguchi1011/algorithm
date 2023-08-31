# Radiant党とDire党があり、どちらかの勝利を決める。
# 各党員は以下のどちらかを行うことができる。
# ・相手チームを1人永遠に行動不能にする
# ・相手チームが0人だったら勝利宣言を行う
# 全員の行動が終わったら残っているチームメンバー(banされた人以外)で第二、第三ラウンドと繰り返す。

# なので、相手チームのメンバーを全員行動不能にすることを考える。

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # きゅーsematorsにsenateを入れる
        senators = deque(senate)
        # バンの権利が使われた回数を保持する変数
        # DireがRadiantをbanした回数(Radiantがbanされた数)
        r_banned_count = 0
        # RadinatがDireをbanした回数(Direがbanされた数)
        d_banned_count = 0
        #RとDの数(両党の党員数)を保持する変数
        r = 0
        d = 0

        #RとDの数を数えてr,dに保持
        for i in range(len(senate)):
            if senate[i] == "R":
                r += 1
            if senate[i] == "D":
                d += 1
        #権利行使可能な党員がいる限り繰り返す
        #一度権利行使した後も、再度キューsenatorsの最後尾に入ることで2,3ラウンド目へ進む
        while senators:
            #Radiant党員が0になったらDireを返す
            if r == 0:
                return "Dire"
            if d == 0:
                return "Radiant"
            #キューの先頭を取得して変数voterに保持 popleft()でキューの先頭から要素を取り出す
            voter = senators.popleft()
            #voter(今回の権利行使者)がRなら
            if voter == "R":
                #（Radiantがbanされた数が０より大きい時）
                if r_banned_count > 0:
                    #Radiant党員の残り人数をデクリメント
                    r -= 1
                    #Radiantがbanされたのでそれに合わせて、カウントを一つ減らす
                    r_banned_count -= 1
                  #Dire党員が行使したbanの権利が0の場合
                else:
                    #Dire党員をbanする権利を使う
                    d_banned_count += 1
                    #自分自身(voter)はキューの最後尾に入って次のラウンドを待つ
                    senators.append(voter)
            #voterがDなら
            if voter == "D":
                # Direがbanされた数が0より大きい時
                if d_banned_count > 0:
                    # Dire党員の数を1減らす
                    d -= 1
                    # Direがbanされたのでそれに合わせて、カウントを一つ減らす
                    d_banned_count -= 1
                  #Radiant党員が行使したbanの権利がない場合
                else:
                    #Radiant党員をbanする権利を使う
                    r_banned_count += 1
                    #自分自身(voter)はキューの最後尾に入って次のラウンドを待つ
                    senators.append(voter)

solution_instance = Solution()
result = solution_instance.predictPartyVictory(senate = "RD")
print(result)

# キューとは
# キュー（Queue）は、データを格納するための抽象的なデータ構造の一種であり、
# データを特定の順序で保持するものです。
# キューは、先入れ先出し（First-In-First-Out、FIFO）と呼ばれるルールに従って動作します。
# これは、最初に追加された要素が最初に取り出されるという意味です。

# 具体的には、キューは要素を追加するための「エンキュー（enqueue）」操作と、
# 要素を取り出すための「デキュー（dequeue）」操作をサポートします。
# 新しい要素はキューの末尾に追加され、取り出す際には先頭から取り出されます。
# この動作は、例えば列に並んでいる人々や、待ち行列に似ています。

# キューは、多くのコンピュータプログラムで使用される重要なデータ構造です。
# 例えば、プロセススケジューリングや、タスクの管理、ネットワーク通信など、さまざまなアプリケーションで活用されます。
# Pythonでは、キューを効果的に操作するための組み込みのデータ構造である collections モジュールの deque（double-ended queue）が提供されています。