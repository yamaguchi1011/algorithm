# word1とword2の2つの文字列が与えられる。word1から交互に文字を追加して文字列をマージする。一方の文字列が他方の文字列より長い場合は、結合後の文字列の末尾に文字を追加する。
# Return the merged string.
# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""

        if len(word1) == len(word2):
            for i in range(len(word1)):
                merged_string += word1[i]
                merged_string += word2[i]
            return merged_string
        elif len(word1) > len(word2):
            for i in range (len(word2)):
                merged_string += word1[i]
                merged_string += word2[i]
            return merged_string + word1[i+1:]
        else:
            for i in range (len(word1)):
                merged_string += word1[i]
                merged_string += word2[i]
            return merged_string +word2[i+1:]

solution_instance = Solution()

# result = solution_instance.mergeAlternately(word1 = "abc", word2 = "pqr")
result = solution_instance.mergeAlternately(word1 = "ab", word2 = "pqrs")
# result = solution_instance.mergeAlternately(word1 = "abcd", word2 = "pq")
print(result)

