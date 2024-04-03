fruits = ["apple", "kiwi", "mango"]

for item in fruits:
    print(item)
    print("-------")
    for item2 in item:
        print(item2)
    print("-------")
        
    
for i in range(10):
    if(i%2):
        print(i)

for i in range(1,10,2):
    print(i)

for i in range(9,0,-2):
    print(i)

for i in range(1,6):
    print(i, end = ",")
