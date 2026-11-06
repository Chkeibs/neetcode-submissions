class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        max_freq = 0
        best = 0

        for right, c in enumerate(s):
            counts[c] = counts.get(c, 0) + 1

            max_freq = max(max_freq, counts[c])

            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best