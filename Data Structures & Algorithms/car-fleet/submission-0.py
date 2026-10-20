class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed), reverse=True)
        res=[]

        for pos,spd in cars:
            time=(target-pos)/spd
            if not res or time>res[-1]:
                res.append(time)
            
        return len(res)
        