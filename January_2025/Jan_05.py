class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_effects = [0] * (n + 1)  # Array to store net shifts for each character range

        # Apply the shifts using a difference array
        for start, end, direction in shifts:
            if direction == 1:
                shift_effects[start] += 1
                shift_effects[end + 1] -= 1
            else:
                shift_effects[start] -= 1
                shift_effects[end + 1] += 1

        # Compute the prefix sum to get the actual shift values for each character
        net_shifts = [0] * n
        current_shift = 0
        for i in range(n):
            current_shift += shift_effects[i]
            net_shifts[i] = current_shift

        # Apply the net shifts to the string
        result = []
        for i in range(n):
            shift = net_shifts[i]
            new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)
