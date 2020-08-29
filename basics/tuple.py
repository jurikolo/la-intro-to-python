print("Docs: https://docs.python.org/3.7/tutorial/datastructures.html#tuples-and-sequences")
point_2d = (1.0, 2.0)
print("Simple 2d tuple: ", point_2d)
point_3d = point_2d + (3.0,)
print("Simple 3d tuple: ", point_3d)
x, y, z = point_3d
print("Tuples can be unpacked, see x = ", x, ", y = ", y, ", z = ", z)
print("My name is %s %s" % ("Jurijs", "Kolomijecs"))
point_2d = (2.0, 3.0)