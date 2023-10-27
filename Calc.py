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
print("3. Area Finder")

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

if ans == "3":
	cls()
	print("1. Triangle")
	print("2. Square")
	print("3. Rectangle")

	ans = input("-> ")

	if ans == "1":
		cls()
		w = int(input("Width-> "))
		h = int(input("Height-> "))
		cls()
		print(f"Ans: {(w * h) / 2}")

	if ans == "2":
		cls()
		w = int(input("Width-> "))
		cls()
		print(f"Ans: {w * w}")

	if ans == "3":
		cls()
		w = int(input("Width-> "))
		h = int(input("Height-> "))
		cls()
		print(f"Ans: {w * h}")
