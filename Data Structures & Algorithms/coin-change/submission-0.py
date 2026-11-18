class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        arr = [amount + 1] *(amount+1)
        arr[0]=0

        for coin in coins:

            for i in range(coin, amount+1):
                curr = arr[i-coin] + 1
                arr[i]=min(curr, arr[i])

        return arr[amount] if arr[amount]!=amount+1 else -1



                
