#   
#   Copyright (c) 2020 Masaharu Kato. All rights reserved.
# 
#   line.py
#   直線・曲線を扱うクラス，および離散化関数
#

from typing import Tuple, Iterable, Callable, Collection, List
Point = Collection[float]

class Line:
    def __init__(self, pbeg:Point, pend:Point):
        self.pbeg = pbeg
        self.pend = pend
        self.pdlt = [(ev - bv) for bv, ev in zip(self.pbeg, self.pend)]


    def at(self, x:float) -> Point:
        return tuple(bv + x * dv for bv, dv in zip(self.pbeg, self.pdlt))



class CurveByLines(Line):
    def __init__(self, pts:Collection[Point]):
        self.lines = [Line(pbeg, pend) for pbeg, pend in zip(pts, pts[1:])]           


    def at(self, x:float) -> Point:
        x_with_lines = x * len(self.lines)
        li = min(int(x_with_lines), len(self.lines) - 1)
        return self.lines[li].at(x_with_lines - li)



class CurveByFormula(Line):
    def __init__(self, f:Callable[[float], Point]):
        self.f = f


    def at(self, x:float) -> Point:
        return self.f(x)



def discretize(line:Line, n:int, xbeg:float=0.0, xend:float=1.0) -> Iterable[Point]:
    xinv = xend - xbeg
    return (line.at((i / n) * xinv + xbeg) for i in range(0, n+1))

