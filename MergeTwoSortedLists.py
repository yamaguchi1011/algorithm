# 2つのソート済み連結リストlist1とlist2の先頭が与えられている。
# この2つのリストを1つのソート済みリストに結合しなさい。このリストは、最初の2つのリストのノードをつなぎ合わせたものでなければならない。
# マージされた連結リストの先頭を返せ。
# 制約
# 両リストのノード数は[0, 50]の範囲にある。
# -100 <= Node.val <= 100
# list1とlist2の両方が減らない順序でソートされている。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 新しい連結リストのヘッドとなるダミーノードを作成
        dummy_head = ListNode(0)#0を入れない場合はNoneがデフォルトで設定される。ダミーノードは基本的にnextだけが操作の対象になるから0を入れなくてもいいけど、理解しやすさのために明示的な初期化が行われていることを示して読み手がわかりやすいようにしている。
        current = dummy_head

        # 両方のリストが空でない限りループ(各リストの要素が空になっていないかを見ている)
        while list1 and list2:
            # list1の先頭ノードの値が小さい場合(valでlistの一番最初の値を取得する)
            if list1.val < list2.val:
                current.next = list1  # ノードを連結
                list1 = list1.next    # list1を次のノードに進める(この記述がないと、ノードが先に進まないので、今回の場合だとlist1が１で無限ループに入る)
            else:
                current.next = list2  # ノードを連結
                list2 = list2.next    # list2を次のノードに進める
            current = current.next   # 新しい連結リストの最後のノードを更新

        # どちらかのリストが残っている場合、残りのノードを連結
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # ダミーノードの次のノードが新しい連結リストの先頭
        return dummy_head.next
    
solution_instance = Solution()

# リストを作成して ListNode オブジェクトを生成
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# 単純にprint(result)で連結リストの先頭ノードを指すポインタは表示できない。
# result は mergeTwoLists メソッドの戻り値であり、連結リストの先頭ノードを指すポインタです。
# 連結リストの各ノードの値を表示するには、result をたどりながらノードの値を取得して表示する必要があります。
# このコードは、current ポインタを使って連結リストのノードをたどり、各ノードの値を表示しています。表示は「値 -> 値 -> ... -> None」という形式で行われます。
result = solution_instance.mergeTwoLists(list1, list2)
current = result
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")


# 感想
# ノードっていう概念があって、ListNode（連結リスト）のクラスを自分で作って使う。連結リストとは、データ構造の一種であるリストの中で自分の次、および前の要素を示す情報（リンク情報）をもつことで要素を連結（リンク）させたリストのことである。それはval（ノードが保持する値を示す属性）やnext(次のノードへのポインタを示す属性)などを持っている。
# デメリット
# リンクを辿らないと各々の要素にアクセスができない！
# リンクのためのメモリを余分に持つ必要がある。
# メリット
# データの個数がダイナミックに増やせる
# データの追加や削除が頻繁に発生する場合は便利
# 連結リスト（各要素が一つ前や後ろの他所へのリンクを持っている）とリスト（値のみ）は全然違うもの