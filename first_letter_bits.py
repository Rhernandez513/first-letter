import time

class Solution:
    def repeatedCharacterbits(self, s: str) -> str | None:
        seen = 0  # bitmask
        for c in s:
            bit = 1 << (ord(c) - ord('a'))
            if seen & bit:
                return c
            seen |= bit

def time_repeated_character_bits():
    s = "abcdefgahijklmno"
    solution = Solution()
    start = time.perf_counter()
    result = solution.repeatedCharacterbits(s)
    end = time.perf_counter()
    duration_ns = (end - start) * 1_000_000_000
    print(f"Duration in Nanoseconds: {duration_ns:.1f} ns")

time_repeated_character_bits()
