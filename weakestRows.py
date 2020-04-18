import re
class Solution:
        
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dicx = dict()
        ct = 0
        for matl in mat:
            dicx[ct] = matl.count(1)
            ct += 1      
        dicxitems = dicx.items()
        outl = []
        ct = 0
        for j in {a: b for a, b in sorted(dicxitems, key=lambda item: item[1])}:
            outl.append(str(j))
            ct += 1
            if ct >= k:
                break
        return outl
