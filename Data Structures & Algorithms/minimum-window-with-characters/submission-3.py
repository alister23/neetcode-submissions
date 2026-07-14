class Solution:
    def to_index(char):
        if ord(char) <= 90:
            return ord(char)-65
        else:
            return ord(char)-97+26
    
    def check(freqs, window_freqs):
        for i in range(52):
            if freqs[i] > window_freqs[i]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        shortest = s+"0"
        freqs = [0]*52
        for char in t:
            freqs[Solution.to_index(char)] += 1
        start = 0
        end = 0
        window_freqs = [0]*52
        while end < len(s):
            window_freqs[Solution.to_index(s[end])] += 1
            while Solution.check(freqs, window_freqs):
                print(s[start:end+1])
                if end-start+1 < len(shortest):
                    shortest = s[start:end+1]
                window_freqs[Solution.to_index(s[start])] -= 1
                start += 1
            end += 1
        if shortest == s+'0':
            return ''
        return shortest

        