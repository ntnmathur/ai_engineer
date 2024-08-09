from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int

@dataclass
class Line:
	p1: Point
	p2: Point
	def calculate_slope(self) -> float:
		return 1.0*(self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)

def find_point_of_intersection(l1: Line, l2: Line) -> Point:
	# Calculate the slopes of the two lines
    m1 = l1.calculate_slope()
    m2 = l2.calculate_slope()
    # Check if the slopes are equal
    if m1 == m2:
        # If the slopes are equal, the lines are parallel and do not intersect
        print("Lines are parallel")
        return None
    # Find the point of intersection using the formula
    x = (l2.p2.x - l1.p2.x + m1 * l1.p1.x - m2 * l2.p1.x) / (m1 - m2)
    y = m1 * (x - l1.p1.x) + l1.p1.y
    # Return the point of intersection as a Point object
    return Point(x=x, y=y)


def main() -> None:
	print("Coordinates for Line 1:")
	x1 = input("Enter x coordinate of point 1:")
	y1 = input("Enter y coordinate of point 1:")
	x2 = input("Enter x coordinate of point 2:")
	y2 = input("Enter y coordinate of point 2:")


	print("Coordinates for Line 2:")
	x3 = input("Enter x coordinate of point 3:")
	y3 = input("Enter y coordinate of point 3:")
	x4 = input("Enter x coordinate of point 4:")
	y4 = input("Enter y coordinate of point 4:")
	try:
		p1 = Point(x=int(x1),y=int(y1))
		p2 = Point(x=int(x2),y=int(y2))
		p3 = Point(x=int(x3),y=int(y3))
		p4 = Point(x=int(x4),y=int(y4))
	except:
		print("Provide integer values for coordinates. Bye!")
	l1 = Line(p1,p2)	
	l2 = Line(p3,p4)

	slope_l1 = l1.calculate_slope()
	slope_l2 = l2.calculate_slope()

	print(f"Slope of Line 1 = {slope_l1}")
	print(f"Slope of Line 2 = {slope_l2}")

	if slope_l1 == slope_l2:
		print("The 2 lines are parallel")
	elif slope_l1*slope_l2 == -1.0:
		print("The 2 lines are perpendicular")
		p = find_point_of_intersection(l1,l2)
		print(f"The 2 lines intersect at the point ({p.x,p.y})")
	else:
		p = find_point_of_intersection(l1,l2)
		print(f"The 2 lines intersect at the point ({p.x,p.y})")

if __name__=='__main__':
    main()