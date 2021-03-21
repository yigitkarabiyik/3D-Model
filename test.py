#check result with random index number
import random
from tridi import *

num = random.randint(0, mesh.triangles.shape[0]) 
print("random index number ", num)
myIndex = sorted_array[num][0]
myArea = sorted_array[num][1]
print("Index of sorted array ", myIndex)
print("Area of sorted array ", myArea)
print("Check mesh.ares_faces ", mesh.area_faces[myIndex])
