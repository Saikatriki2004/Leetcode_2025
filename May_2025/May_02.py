class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        right = [float('inf')] * n
        left = [float('inf')] * n
        
        # Right pass
        current_force = None
        current_time = 0
        for i in range(n):
            if dominoes[i] == 'R':
                current_force = 'R'
                current_time = 0
            elif dominoes[i] == 'L':
                current_force = None
                current_time = 0
            else:
                if current_force == 'R':
                    current_time += 1
                    right[i] = current_time
                else:
                    right[i] = float('inf')
        
        # Left pass
        current_force = None
        current_time = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                current_force = 'L'
                current_time = 0
            elif dominoes[i] == 'R':
                current_force = None
                current_time = 0
            else:
                if current_force == 'L':
                    current_time += 1
                    left[i] = current_time
                else:
                    left[i] = float('inf')
        
        result = []
        for i in range(n):
            if dominoes[i] != '.':
                result.append(dominoes[i])
            else:
                if right[i] < left[i]:
                    result.append('R')
                elif left[i] < right[i]:
                    result.append('L')
                else:
                    result.append('.')
        
        return ''.join(result)
