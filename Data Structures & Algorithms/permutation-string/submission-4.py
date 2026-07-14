class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            print('s1 TOO LONG')
            return False
        start = 0
        end = len(s1)-1
        freqs = [0]*26
        true_freqs = [0]*26
        for i in range(len(s1)):
            freqs[ord(s2[i])-97] += 1
            true_freqs[ord(s1[i])-97] += 1
        while end < len(s2):
            print('checking', s2[start:end+1])
            if freqs == true_freqs:
                print("DONE")
                return True
            freqs[ord(s2[start])-97] -= 1
            start += 1
            end += 1
            if end >= len(s2):
                break
            freqs[ord(s2[end])-97] += 1
        return False