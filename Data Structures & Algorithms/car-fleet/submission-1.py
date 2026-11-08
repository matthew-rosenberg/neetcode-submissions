class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_positions, sorted_speeds = zip(*sorted(zip(position, speed), reverse=True))
        count = 0
        last_time = 0
        for i in range(len(sorted_positions)):
            position = sorted_positions[i]
            speed = sorted_speeds[i]

            time = (target - position)/ speed
            if time > last_time:
                last_time = time
                count += 1
        return count

