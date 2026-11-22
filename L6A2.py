a = 10
b = 15
c = 15

print(not(a == b))
print(not(b == c))



d = "Python"
e = "programming"

if not(d == e):
    print(e, "and" ,d, "are different words.")



f = 5
g = 4

if not((f == g) == (g == 4)):
    print("Hi, hello and bye.")



h = int(input("Enter a number: "))
if not (h % 2 == 0):
    print(h, " is an odd number")
