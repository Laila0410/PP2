f = open("demofile.txt", "r")
print(f.readline().strip())
f.close()
print(f.closed)