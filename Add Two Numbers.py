# 2つの空ではなく非負整数を含む連結リストが与えられます。数字は逆順で入れられており、各ノードは一桁の数字を含みます。2つの数字を加え、その合計を連結リストとして返してください。

# 先頭が0から始まる数字はないと仮定して良いです。※0を除く
# 以下補足です。

# テストケースを見る限り、2つの連結リストが与えられるので、1つの数字として結合し、逆順に並べ替えた上で数字として足し算し、その結果を再度逆順に並べ替えして、連結リストとして返す必要があります。

# list1 = [1,2,3]　→321

# list2 = [4,5,6]　→654

# 321+654 = 975　→579

# 579を連結リストとして返すというイメージ

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      # それぞれのノード（連結リスト）を一つの数字として結合（最初は文字列として結合。あとで逆順にするため）
      n1 = ""
      n2 = ""
      #l1の要素がある限り各要素を文字列としてn1に代入
      while l1 is not None:
          n1 += str(l1.val)
          # 次のノードへ移る。l1.nextはListNodeクラスの属性
          l1 = l1.next
      while l2 is not None:
          n2 += str(l2.val)
          l2 = l2.next
      # 逆順に並べ替えて
      n1 = n1[::-1]
      n2 = n2[::-1]
      # 数字として足し算して、再び文字列に変換
      ans_str = str(int(n1)+int(n2))
      # 結果を再度逆順に並べ替えして
      ans_str = ans_str[::-1]
      # インスタンス化(ListNodeはリンクリストのノードを表す。)
      ans = trav = ListNode()

      # ans_strの文字数分だけ処理（連結リストのノードを作成していく）
      for i in range(len(ans_str)):
          # i番目の要素をvalに格納
          trav.val = ans_str[i]
          # 終端じゃない場合はtrav.nextを再度インスタンス化する
          if i != len(ans_str)-1:
              trav.next = ListNode()
          # 次のノードに進める
          trav = trav.next
      return ans


solution_instance = Solution()

# リストを作成して ListNode オブジェクトを生成
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
result = solution_instance.addTwoNumbers(l1, l2)
current = result
while current:
    if current.next:
        print(current.val, end=",")
    else:
        print(current.val)
    current = current.next


# スライス（slice）・・・n1 = n1[::-1] Pythonのリストや文字列を逆順にする
# n1 はリストまたは文字列と仮定します。
# スライス構文 [start:end:step] を使用して、n1 の要素を逆順に取得します。
# ・start はスライスの開始位置を指定します。ここでは指定されていないため、デフォルト値としてリストまたは文字列の最後の要素が使用されます。
# ・end はスライスの終了位置を指定します。ここでは指定されていないため、デフォルト値としてリストまたは文字列の最初の要素の前の位置が使用されます。
# ・step はスライスのステップ（刻み幅）を指定します。ここでは -1 が指定されており、逆順に取得するために要素を逆に走査しています。
# 逆順に取得した結果を新しいリストまたは文字列として、変数 n1 に再代入します。
# 結果として、n1 には元のリストまたは文字列の要素が逆順に並んだものが格納されます。このコードは、リストや文字列の要素を逆順にする際によく使用されます。