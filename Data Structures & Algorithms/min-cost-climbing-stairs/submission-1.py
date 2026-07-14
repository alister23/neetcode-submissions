class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1]*len(cost)
        def recur(index):
            nonlocal dp
            if dp[index] != -1:
                return dp[index]
            if index >= (len(cost)):
                return 0
            if index == len(cost)-1:
                dp[index] = cost[index]
                return cost[index]
            if index == len(cost)-2:
                answer = cost[index]
                dp[index] = answer
                return answer
            answer = cost[index] + min(recur(index+1), recur(index+2))
            dp[index] = answer
            # print(index, answer)
            return answer
        
        return min(recur(0), recur(1))
