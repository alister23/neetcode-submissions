class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            #print(f"{stack=}")
            #print("receiving", asteroid)
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) == abs(asteroid):
                    #print("destroy them both")
                    stack.pop()
                    break
                elif abs(stack[-1]) < abs(asteroid):
                    #print("destroyed stack[-1] one")
                    stack.pop()
                else:
                    #print("destroyed")
                    break
            else:
                #print("no conflict")
                stack.append(asteroid)

        return stack