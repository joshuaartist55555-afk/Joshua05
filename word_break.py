def wordBreak(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)  # For O(1) lookups
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is segmentable

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # No need to check further if s[0:i] is segmentable

    return dp[n]
