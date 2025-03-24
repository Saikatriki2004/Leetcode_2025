class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Sort meetings by start day
        meetings.sort(key=lambda x: x[0])
        
        # Initialize total covered days
        total_covered = 0
        
        # Start with the first meeting
        current_start = meetings[0][0]
        current_end = meetings[0][1]
        
        # Process each subsequent meeting
        for start, end in meetings[1:]:
            if start > current_end:
                # Gap found, add the length of the completed interval
                total_covered += current_end - current_start + 1
                # Start a new interval
                current_start = start
                current_end = end
            else:
                # Overlap or adjacent, extend the current interval
                current_end = max(current_end, end)
        
        # Add the length of the last interval
        total_covered += current_end - current_start + 1
        
        # Return the number of free days
        return days - total_covered
