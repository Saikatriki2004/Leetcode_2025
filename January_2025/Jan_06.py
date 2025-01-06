class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        
        # Forward pass to calculate the cost of moving balls from the left
        count = 0
        moves = 0
        for i in range(n):
            answer[i] += moves
            count += int(boxes[i])  # Count the number of balls
            moves += count  # Add count to moves for the next position
        
        # Backward pass to calculate the cost of moving balls from the right
        count = 0
        moves = 0
        for i in range(n - 1, -1, -1):
            answer[i] += moves
            count += int(boxes[i])  # Count the number of balls
            moves += count  # Add count to moves for the previous position
        
        return answer
