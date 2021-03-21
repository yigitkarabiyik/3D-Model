
import numpy as np
import trimesh
from math import sqrt

'''Load data from google drive'''

#load data as npz
stl_path='moon_city_final.stl'
mesh = trimesh.load(stl_path)

''' Functions '''

def area_calculator(triangle):
  ''' This function calculate area of triangle
      by using vertices coordinate of triangle'''
  pointA = triangle[0]
  pointB = triangle[1]
  pointC = triangle[2]
  # Distance formula in 3 dimension for finding edges
  # AB = sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
  edgeA = sqrt((pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2 + (pointA[2]-pointB[2])**2 )
  edgeB = sqrt((pointA[0]-pointC[0])**2 + (pointA[1]-pointC[1])**2 + (pointA[2]-pointC[2])**2 )
  edgeC = sqrt((pointB[0]-pointC[0])**2 + (pointB[1]-pointC[1])**2 + (pointB[2]-pointC[2])**2 )
  # Area formula known edges 
  # Area = sqrt(s*(s-A)*(s-B)*(s-C))    s = (A+B+C)/2
  s = (edgeA + edgeB + edgeC)/2
  area = sqrt(s*(s - edgeA)*(s - edgeB)*(s - edgeC))
  return area

def quickSort(arr):
  '''Sort of the (n,2) shape of array according to first index
  used Selection Sort Method'''
  less = []
  pivotList = []
  more = []
  if len(arr) <= 1:
      return arr
  else:
      pivot = arr[0]
      for i in arr:
          if i[1] < pivot[1]:
              less.append(i)
          elif i[1] > pivot[1]:
              more.append(i)
          else:
              pivotList.append(i)
      less = quickSort(less)
      more = quickSort(more)
  return less + pivotList + more

def shellSort(input_list):
  '''Sort of the (n,2) shape of array according to first index
  Used Shell Sort Method'''
  
  gap = len(input_list) // 2
  while gap > 0:

    for i in range(gap, len(input_list)):
      temp = input_list[i]
      j = i
      # Sort the sub list for this gap

      while j >= gap and input_list[j - gap][1] > temp[1]:
          input_list[j] = input_list[j - gap]
          j = j-gap
      input_list[j] = temp

    # Reduce the gap for the next element
    gap = gap//2
  return input_list

# take triangles with vertices
triangles = mesh.triangles

# create array as [[index, area], ...]
i=0
index_area=[]
for triangle in triangles:
  area = area_calculator(triangle)
  arr = [i, area]
  index_area.append(arr) 
  i += 1

# sorted from small to large according to area
sorted_array = shellSort(index_area)

# save numpy array with npy extension
#with open('result.json', 'w') as f:
#    json.dump(sorted_array, f)
# save numpy array with json extension
import json
with open('result.json', 'w') as f:
    json.dump(sorted_array, f)
