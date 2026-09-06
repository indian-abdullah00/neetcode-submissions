from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.dc = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dc[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.dc[key])-1
        res = ""
        while l <=r:
            mid = (l+r)//2
            if self.dc[key][mid][0] == timestamp:
                res = self.dc[key][mid][1]
                break
            elif self.dc[key][mid][0] < timestamp:
                l = mid+1
                res = self.dc[key][mid][1]
                
            else: 
                r = mid -1

        return res


        
