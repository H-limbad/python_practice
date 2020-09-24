st = ["1","2","3"]
n=len(st)
for x in range(n):
	for y in ["3","2","1"]:
		for z in reversed(st):
			print(x,y,":-",st[x])
