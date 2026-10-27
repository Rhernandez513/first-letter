import time

class Solution:
    def repeatedCharacter(self, s: str) -> str:

      # O(N) Time
      # O(N) Space
      seen = set()
      for ch in s:
        if ch in seen:
          return ch
        else:
           seen.add(ch)
        

def time_repeated_character():
    s = "abcdefgahijklmno"
    solution = Solution()
    start = time.perf_counter()
    _ = solution.repeatedCharacter(s)
    end = time.perf_counter()
    duration_ns = (end - start) * 1_000_000_000
    print(f"Duration in Nanoseconds: {duration_ns:.1f} ns")

time_repeated_character()
