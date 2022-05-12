l1 = []
n = int(input("Enter size of list : "))
for j in range(0,n):
	l1.append(int(input("Enter value of list : ")))
print(f"Original list {l1}")
print("first method : ")
l2 = l1.copy()
l2.reverse()
print(l2)

print("Second method : ")
l3 = l1.copy()
l3 = l3[ : : -1]
print(l3)

l4 = l1.copy()
print("Third Method : ")

# Using For loop

#for i in range(len(l4)//2):
#	l4[i],l4[len(l4) -i -1] = l4[len(l4) -i -1],l4[i]
#print(l4)


# Using While loop
i = 0
while(i < (len(l4)-(n//2))):
	l4[i],l4[n-1] = l4[n-1],l4[i]
	if l4 == l3 :
			break
	i += 1
	n -= 1
print(l4)
if l2 == l3 and l3 == l4:
	print("All method gives same result")


	