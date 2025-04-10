import math

class Solution:
  def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
    s_val = int(s)
    len_s = len(s)
    len_start = len(str(start))
    len_finish = len(str(finish))
    total_count = 0
    
    if len_start <= len_s <= len_finish and start <= s_val <= finish:
      total_count += 1
      
    for l_x in range(max(len_start, len_s + 1), len_finish + 1):
      l_prime = l_x - len_s
      power_of_10 = 10**len_s
      L_p = (start - s_val + power_of_10 - 1) // power_of_10
      R_p = (finish - s_val) // power_of_10
      lower_p = 10**(l_prime - 1) if l_prime > 0 else 0
      upper_p = 10**l_prime - 1 if l_prime > 0 else -1
      a = max(L_p, lower_p)
      b = min(R_p, upper_p)
      
      if a <= b:
        memo = {}
        def count_upto(n, limit):
          if n < 0:
            return 0
          n_str = str(n)
          length = len(n_str)
          
          def solve(index, tight):
            if index == length:
              return 1
            if (index, tight) in memo:
              return memo[(index, tight)]
            upper = int(n_str[index]) if tight else limit
            ans = 0
            for digit in range(upper + 1):
              if digit > limit:
                break
              next_tight = tight and (digit == upper)
              ans += solve(index + 1, next_tight)
            memo[(index, tight)] = ans
            return ans
            
          memo.clear()
          return solve(0, True)
          
        total_count += count_upto(b, limit) - count_upto(a - 1, limit)
        
    return total_count
