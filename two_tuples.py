# This function will receive two tuples 
# representing two (x,y) coordingates on
# a plane, receives parameter (x) that is 
# a new value on the x-coordinate of the plane.
# and returns a value (y) that is on the line
#created by the first two points
    
def coordinates(x1, y1, x2, y2):
    x = (x1 + x2)/2
    y = (y1 + y2)/2
    return  y

result = coordinates(0, 0, 4, 4)
print("y = " + str(result))