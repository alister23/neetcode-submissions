from collections import Counter

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        left = 0
        right = len(people)-1
        while left < right:
            #print(people[left:right+1])
            if people[left] + people[right] <= limit:
                #print("seating", people[left], "and", people[right])
                boats += 1
                left += 1
                right -= 1
            else:
                #print("seating", people[right], "alone")
                boats += 1
                right -= 1
        
        if left == right: boats += 1
        
        return boats