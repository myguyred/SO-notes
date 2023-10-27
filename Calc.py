import math, os

def cls():
	if os.name == "nt":
		os.system("cls")

	else:
		os.system("clear")

## Main ##
cls()
print("1. Velocity")
print("2. Acceleration")

ans = input("-> ")

if ans == "1":
	cls()
	d = int(input("Distance-> "))
	t = int(input("Time-> "))
	cls()
	print(f"Ans: {d/t}")

if ans == "2":
	cls()
	vf = int(input("vf-> "))
	vi = int(input("vi-> "))
	tf = int(input("tf-> "))
	ti = int(input("ti-> "))
	cls()
	print(f"Ans: {(vf - vi) / (tf - ti)}")
