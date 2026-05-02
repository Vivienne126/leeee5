n=int(input("Enter number"))
binary=bin(n)[2:]
print(binary)
maxx=max(binary.split("0"))
print(f"Max consequetive ones {maxx}")