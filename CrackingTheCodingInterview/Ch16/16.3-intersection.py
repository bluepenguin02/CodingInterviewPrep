from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def line_intersection(points1: tuple, points2: tuple) -> Point | None:
    line1 = Line(points1)
    line2 = Line(points2)
    
    return intersection(line1, line2)


class Line:
    def __init__(self, points: tuple):
        self._start = points[0]
        self._end = points[1]
        self._m = 0
        self._b = 0
        self._slope_and_intercept()
        
    @property
    def start(self):
        return self._start
    
    @property
    def end(self):
        return self._end
    
    @property
    def m(self):
        return self._m
    
    @property
    def b(self):
        return self._b
    
    def _slope_and_intercept(self):
        if self._start.x == self._end.x:
            self._m = float('inf')
            self._b = float('inf')
        else: 
            self._m = (self._start.y - self._end.y) / (self._start.x - self._end.x)
            self._b = self._start.y - self._m * self._start.x
            
    def is_vertical(self):
        return self._m == float('inf')
            
    def y_from_x(self, x: float):
        if x < self._start.x or self._end.x < x:
            return None
        else:
            return self._m * x + self._b
    
def intersection(line1: Line, line2: Line) -> Point | None:
    if line1._m == line2._m:
        if line1._b != line2._b:
            return None
        
        if is_between(line1._start, line2._start, line1._end):
            return line2._start
        elif is_between(line1._start, line2._end, line1._end):
            return line2._end
        elif is_between(line2._start, line1._start, line2._end):
            return line1._start
        elif is_between(line2._start, line1._end, line2._end):
            return line1._end
        else:
            return None
        
    if line1.is_vertical() or line2.is_vertical():
        x = line1._start.x if line1.is_vertical() else line2._start.x
    else:
        x = (line2._b - line1._b) / (line1._m - line2._m)
        
    y = line1.y_from_x(x) if line2.is_vertical() else line2.y_from_x(x)
    
    intersect = Point(x, y)
    if is_between(line1._start, intersect, line1._end) and is_between(line2._start, intersect, line2._end):
        return intersect
    return None
        
def is_between(start: Point, middle: Point, end: Point):
    return is_between_on_axis(start.x, middle.x, end.x) and is_between_on_axis(start.y, middle.y, end.y)
        
def is_between_on_axis(start: float, middle: float, end: float):
    if start < end:
        return start <= middle <= end
    else:
        return start >= middle >= end

if __name__ == '__main__':
    segment1 = (Point(1, 1), Point(3, 3))
    segment2 = (Point(3, 3), Point(5, 1))
    print(line_intersection(segment1, segment2))