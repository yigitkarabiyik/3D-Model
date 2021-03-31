# tridi

The project that reads the 3D model include stl extension was created.
All the area of triangles were calculated.
The two-dimensional array was created by sorting the triangles whose areas were calculated from small to large.
The two-dimensional sorted array contains both the area of the triangle and the library given index of the triangle.
Results were saved as two different extensions as "npy" and "json".

The project was tested by writing the algorithm that generates a random index number.

## Requirements

pip install trimesh

pip install numpy

## Run

python tridi.py
