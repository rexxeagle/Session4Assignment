# Created by Rendy Elang Lesmana - TI23I - 20230040044

x = 100
y = 10
z = 68

print(f"value of x is {x}, y is {y}, and z is {z}")
print(f"value of x in binary is {format(x, '08b')}")
print(f"value of y in binary is {format(y, '08b')}")
print(f"value of z in binary is {format(z, '08b')}")

and_op = x & y & z
print(f"Result of AND operator for variable x & y & z is {format(and_op, '08b')}")

xor_op = x ^ y
print(f"Result of XOR operator for variable x^y in binary is {format(xor_op, '08b')}")