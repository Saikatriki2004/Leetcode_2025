from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # Dictionary to store the current color of each ball.
        ball_to_color = {}
        # Dictionary to count how many balls have a given color.
        color_count = {}
        result = []
        
        for query in queries:
            ball, color = query
            
            # If the ball is already colored, we may need to update its color.
            if ball in ball_to_color:
                old_color = ball_to_color[ball]
                # If the ball already has the queried color, nothing changes.
                if old_color == color:
                    result.append(len(color_count))
                    continue
                # Otherwise, decrement the count for the old color.
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]
            
            # Update the ball's color.
            ball_to_color[ball] = color
            # Increment the count for the new color.
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1
            
            # The number of distinct colors is the number of keys in color_count.
            result.append(len(color_count))
        
        return result
