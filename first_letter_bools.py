import time

class Solution:
    def repeatedCharacter(self, s: str) -> str | None:
        
        bool_arr = [False] * 26

        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            if bool_arr[idx]:
                return s[i]
            else:
                bool_arr[idx] = True

def time_repeated_character():
    s = "abcdefgahijklmno"
    solution = Solution()
    start = time.perf_counter()
    result = solution.repeatedCharacter(s)
    end = time.perf_counter()
    duration_ns = (end - start) * 1_000_000_000
    print(f"Duration in Nanoseconds: {duration_ns:.1f} ns")

time_repeated_character()
