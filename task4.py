# sides given are 3,4,5 return value must be 6
#calculating the area of a triangle
task4 = (3 + 4 + 5)/2
area = (task4*(task4-3)*(task4-4)*(task4-5))**0.5
import math
#rounding down using math.trunce.
print(math.trunc(area))

# for the second triangle, side are 7,8,10 must return 27.
task4 = (7 + 8 + 10)/2
area = (task4*(task4-7)*(task4-8)*(task4-10))**0.5
import math
print(math.trunc(area))