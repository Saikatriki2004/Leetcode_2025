class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)

        # Helper function to validate a given starting value
        def validate(start):
            original = [start]
            for i in range(n - 1):
                original.append(derived[i] ^ original[-1])
            # Check the circular condition
            return original[-1] ^ original[0] == derived[-1]

        # Try both possible starting values for original[0]
        return validate(0) or validate(1)
