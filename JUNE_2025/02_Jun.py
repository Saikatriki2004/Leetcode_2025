class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        # Step 0: Give each child 1 candy initially.
        candies = [1] * n

        # Step 1: Left->Right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Step 2: Right->Left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # Take max to avoid reducing any value set in the first pass
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # The answer is the sum of all candies assigned.
        return sum(candies)
