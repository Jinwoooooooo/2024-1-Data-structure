from dbllist import *

dlist = DList()
print(dlist.isEmpty())

dlist.append(100)
dlist.append(200)
dlist.append(300)
dlist.append(400)
dlist.append(500)
dlist.append(600)
dlist.showList()

print(dlist.find(200))
# ==== insertBefore ====
n = dlist.find(200)
dlist.insertBefore(n , 150)
dlist.showList()
n = dlist.find(400)
dlist.insertBefore(n , 350)
dlist.showList()

# ==== insertAfter ====
n = dlist.find(500)
dlist.insertAfter(n , 550)
dlist.showList()
n = dlist.find(600)
dlist.insertAfter(n , 650)
dlist.showList()

# ==== insertSorted ====
dlist.insertSorted(250)
dlist.insertSorted(450)
dlist.insertSorted(0)
dlist.insertSorted(50)
dlist.showList()

dlist.remove(0)

dlist.showList()
n = dlist.find(600)
dlist.remove2(n)
dlist.showList()
print(dlist.isEmpty())
