def check(a,b):
    return all(a[j] >= b[j] for j in range(ord('z')-ord('A')+1))

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        freq_s = [0]*(ord('z')-ord('A')+1)
        freq_t = [0]*(ord('z')-ord('A')+1)
        
        for i in range(len(t)):
            freq_s[ord(s[i])-ord("A")] += 1
            freq_t[ord(t[i])-ord("A")] += 1
        
        end = len(t)
        start = 0
        min_len = len(s)+1
        min_string = ""
        while end <= len(s):
            changed = False
            while check(freq_s, freq_t):
                changed = True
                # print(s[start:end],"is good! shortening...")
                if min_len > end-start:
                    min_len = end-start
                    min_string = s[start:end]
                freq_s[ord(s[start])-ord("A")] -= 1
                start += 1
            if changed:
                freq_s[ord(s[start-1])-ord("A")] += 1
                start -= 1
            if end < len(s):
                freq_s[ord(s[end])-ord("A")] += 1
                end += 1
            else:
                break
            # print("now", s[start:end])
        return min_string
            
            
