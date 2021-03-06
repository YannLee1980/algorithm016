# 44. 通配符匹配
# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
# https://leetcode-cn.com/problems/wildcard-matching/

# 这是一个超时的解法：

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        if not s and not p: return True
        
        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if j == len(p): return i == len(s)
            
            first = len(s) > i and p[j] in [s[i], '?']
            
            if len(p) > j and p[j] == '*':
                ans = False
                for k in range(i, len(s)+1):
                    ans = ans or dp(k, j+1)
            else:
                ans = first and dp(i+1, j+1)
            memo[(i, j)] = ans
            
            return ans
        
        return dp(0, 0)