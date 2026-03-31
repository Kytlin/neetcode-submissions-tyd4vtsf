class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        num_fleets, last_arrival = 0, 0
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > last_arrival:
                num_fleets += 1
                last_arrival = time
        return num_fleets