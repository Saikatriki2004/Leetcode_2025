class Solution:
    def clearDigits(self, s: str) -> str:
        # Convert the string to a list of characters for easier in-place deletion.
        arr = list(s)
        
        # Continue until there is no digit left in the list.
        while any(ch.isdigit() for ch in arr):
            # Step 1: Find the index of the first digit.
            first_digit_index = None
            for i, ch in enumerate(arr):
                if ch.isdigit():
                    first_digit_index = i
                    break
            
            # Step 2: From first_digit_index-1 down to 0, find the closest non-digit.
            # Since input is valid, we expect to always find one.
            closest_non_digit_index = None
            for j in range(first_digit_index - 1, -1, -1):
                if not arr[j].isdigit():
                    closest_non_digit_index = j
                    break
            
            # Step 3: Remove both the digit and the found non-digit.
            # Delete the element with the larger index first so that indices of earlier elements don't change.
            indices_to_delete = sorted([first_digit_index, closest_non_digit_index], reverse=True)
            for idx in indices_to_delete:
                del arr[idx]
        
        # Return the resulting string after joining the list.
        return "".join(arr)
