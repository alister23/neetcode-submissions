class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0], reverse=True)
        max_time = 0
        for p, s in cars:
            time = (target-p)/s
            if time > max_time:
                fleets += 1
                max_time = time
        return fleets