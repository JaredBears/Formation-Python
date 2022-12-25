def maxTickets(tickets):
    dp = {}
    answer = 0
    def buildSubsequence(idx, seq):
        if idx >= len(tickets):
            for num in seq:
                if num not in dp:
                    dp[num] = len(seq)
            return
        if abs(tickets[idx] - seq[-1]) <= 1:
            seq.append(tickets[idx])
        buildSubsequence(idx + 1, seq)

    tickets.sort()
    for i, num in enumerate(tickets):
        if num not in dp:
            buildSubsequence(i + 1, [num])
        answer = max(answer, dp[num])
    return answer