class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0], reverse=True)
        fleets = 0
        # ongoing = 1
        while cars:
            cur_p, cur_s = cars.pop(0)
            while cars:
                print("comparing to position", cur_p, "speed", cur_s)
                p, s = cars.pop(0)
                print("looking at position", p, "speed", s)
                if s == cur_s:
                    if p == cur_p:
                        # ongoing = 
                        print("same car wtf")
                        continue
                    else:
                        print("same speed :( new fleet")
                        fleets += 1
                        cur_p = p
                        # ongoing = 1
                        continue
                else:
                    if 0 < (cur_p-p)/(s-cur_s) <= (target-cur_p)/cur_s:
                        # ongoing = 1
                        print("join the fleet!")
                        continue
                    else:
                        cur_p = p
                        cur_s = s
                        fleets += 1
                        # ongoing = 1
                        print("can't join :( new fleet")
                        continue
        return fleets+1
