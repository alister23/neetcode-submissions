class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = [0]*26
        freq2 = [0]*26

        for i in range(len(s1)):
            freq1[ord(s1[i])-ord('a')] += 1
            freq2[ord(s2[i])-ord('a')] += 1
        if freq2 == freq1:
            return True
        
        for i in range(1,len(s2)-len(s1)+1):
            # print(freq2)
            freq2[ord(s2[i-1])-ord('a')] -= 1
            freq2[ord(s2[i+len(s1)-1])-ord('a')] += 1
            if freq2 == freq1:
                return True
        return False