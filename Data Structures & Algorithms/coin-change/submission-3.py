from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        c = set(coins)

        q = deque()
        for coin in coins:
            q.append((coin, 1))
        while q:
            val, count = q.popleft()
            print("val_count", val, count)
            if val == amount:
                return count
            for coin in coins:
                total = coin + val
                print(total)
                if total <= amount and not total in c:
                    c.add(total)
                    q.append((total, count + 1))
        return -1
                
