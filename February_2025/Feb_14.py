from typing import List

class ProductOfNumbers:
    def __init__(self):
        # Start with an initial product of 1.
        self.prod = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Reset the product list if 0 is added.
            self.prod = [1]
        else:
            # Append the product so far times the new number.
            self.prod.append(self.prod[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is greater than or equal to the number of elements added since last zero,
        # then the product must be 0.
        if k >= len(self.prod):
            return 0
        # Otherwise, return the ratio of the total product by the product before the last k elements.
        return self.prod[-1] // self.prod[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
