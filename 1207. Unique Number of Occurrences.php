<!-- # 整数配列arrが与えられます。
# 各要素の発生回数が全て異なっていればTrue、そうでなければFalseを返してください。

# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true -->
class Solution {
  /**
   * @param Integer[] $arr
   * @return Boolean
   */
  function uniqueOccurrences($arr) {
    $freq = array_count_values($arr);
    return count(array_flip($freq)) === count($freq);
  }
}