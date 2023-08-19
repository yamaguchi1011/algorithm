# 整数 x が与えられたとき、x が回文であれば真を返す。(回文)
# そうでなければ偽を返す。
class Solution:
  # 関数を定義、返り値はboolean型
    def isPalindrome(self,x: str) -> bool:
  # xを文字列に変換
        x = str(x)
  # xをリストに変換
        x =  list(x)
  # x_reverseはxを逆順にしてリストにしたもの
        x_reverse = list(reversed(x))
  # xとx_reverseが一致している場合はtrueを返す。
        if x == x_reverse:
            return True
        else:
            return False

# 下記ターミナル実行用
solution_instance = Solution()

# テスト用のリストと目標値を指定して twoSum メソッドを呼び出す
# result = solution_instance.isPalindrome(x=121)
result = solution_instance.isPalindrome(x=-121)
# result = solution_instance.isPalindrome(x=10)
print(result)