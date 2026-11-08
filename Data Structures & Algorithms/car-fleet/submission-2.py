class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_positions, sorted_speeds = zip(
            *sorted(
                zip(position, speed),
                reverse=True
            )
        )
        count = 0
        last_time = 0
        for position, speed in zip(sorted_positions, sorted_speeds):
            time = (target - position)/speed
            if time > last_time:
                count += 1
                last_time = time
        return count