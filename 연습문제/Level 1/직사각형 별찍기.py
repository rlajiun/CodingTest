a, b = map(int, input().strip().split(' '))
print(("*" * a + "\n") * b)
==================================================
a, b = map(int, input().strip().split(' '))
for i in range(b):
    for i in range(a):
        print("*", end="")
    print("")
