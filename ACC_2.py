from typing import List

def wordBreak(s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
 
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[len(s)]

# Example usage:
n = 6
s = "ilikesamsung"
wordDict = ["i", "like", "sam", "sung", "samsung", "mobile"]
result = wordBreak(s, wordDict)
print(1 if result else 0)


