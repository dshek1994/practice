#!/usr/local/bin/python3

def is_match(s, p):
    # Create a 2D dp table
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

    # Base case: an empty pattern matches an empty string
    dp[0][0] = True

    # Handle patterns that start with '*'
    for j in range(2, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    # Fill in the dp table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
    
    return dp[-1][-1]

# Example usage
s = "ab"
p = ".*"
match = is_match(s, p)
print("Match:", match)
