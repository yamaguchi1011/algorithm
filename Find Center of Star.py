# n個のノードがそれぞれ1からnまでのラベルづけされた無向スターグラフがあります。
# スターグラフは1つ中央のノードとn-1個の中央ノードとだけつながる周辺ノードがあります。
# 2次元の整数配列edgesが与えられます。
# それぞれの要素edges[i]=[ui, vi]はノードuiとノードviの間に辺があることを示します。スターグラフの中央のノードを返してください。

class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        # 空の辞書作る。各ノードの出現回数を記録するために使用
        dic = {}
        # １から順番にnまでの数字が使われているということ、n-1個のエッジがあるというのが条件なので、
        # nが４だった場合、中心のノードは固定（つまり中心に使われている数字以外の数字でエッジを作るので、４から中心になる数字分を引いて３のエッジがあるということになる。
        # nが４だった場合、与えられるedgesは３つなので、辞書を作る場合は4つ作成すればいいのでそのためのコードを実装する。
        for i in range(1, len(edges)+2):
            dic[i] = 0
        # iとvにedgesから値を入れていくiとvはキーになる。
        # キーとなる数字が何回出てきたかをカウントしている。１回以上、その数字が出てきたらそれが中心のノードになる。
        for i, v in edges:
            dic[i] += 1
            dic[v] += 1

        print(dic)
        # 1で初期化
        answer = 1
        # 現状のanswerより多い数字が出てきたらその都度answerに格納していき、最終的にanswerに入っていた数字が解答になる。
        for i in dic.keys():
            if dic[i] > answer:
                answer = i

        return answer
    
solution_instance = Solution()
result = solution_instance.findCenter(edges = [[1,2],[2,3],[4,2]])
# ちなみに問題文の条件から外れて、中心以外で同じノードが出てきても結果は変わらない。
# result = solution_instance.findCenter(edges = [[1,2],[2,3],[4,2],[1,2]])
print(result)
