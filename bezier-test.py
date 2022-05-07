from bisect import bisect
import math

def _GetBezierMovementRatio(t: float) -> float:
    # Initialise y to 0
    # y = 0

    # Iterate over the points in the list    
    # for x, y in pointList:
        # Stop when the x point is greater than the time factor
        # if x > t:
            # break

    # Get the index of t within the x points
    xPoints = [x for x, y in pointList]
    yPoints = [y for x, y in pointList]
    index = bisect(xPoints, t)

    if index == 0:
        return yPoints[0]
    elif index >= len(yPoints):
        return yPoints[-1]

    xFraction = ((xPoints[index-1] + xPoints[index]) / 2) - xPoints[index-1]
    y = yPoints[index-1] + (yPoints[index] - yPoints[index-1]) * xFraction

    # Return the y point associated with this x point
    return y

def _CalculateBezierPoint(t: float) -> tuple[float, float]:
    # Set the P0 - P3 control points
    p0 = (0.0, 0.0)
    p1 = (0.25, 0.1)
    p2 = (0.25, 1.0)
    p3 = (1.0, 1.0)

    # Initialise the returned point to 0, 0
    point: list[float] = [0, 0]

    # Calculate x and y
    for i in range(2):
        point[i] = ((1 - t)**3 * p0[i]) + (3 * (1 - t)**2 * t * p1[i]) + (3 * (1 - t) * t**2 * p2[i]) + (t**3 * p3[i])

    # Return the calculated point
    return tuple(point)

fps = 60
transitionTime = 0.25

# Create a list of points on a Bezier curve, first ensure the number of points on the curve is adequate
framesInTransition = math.ceil(fps * transitionTime)

# Calculate the points given the ideal frame numbers, storing them in point list as a lookup table
pointList = [_CalculateBezierPoint(t / framesInTransition) for t in range(framesInTransition + 1)]

print(pointList[0])
print(pointList[-1])

