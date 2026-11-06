class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)

        if m > len(s2):
            return False

        target = [0] * 26
        window = [0] * 26
        base = ord("a")

        for c in s1:
            target[ord(c) - base] += 1

        for right, c in enumerate(s2):
            window[ord(c) - base] += 1

            if right >= m:
                old = s2[right - m]
                window[ord(old) - base] -= 1

            if right >= m - 1 and window == target:
                return True

        return False