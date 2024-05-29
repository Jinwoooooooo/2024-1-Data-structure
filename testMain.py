from dbllist import *
#======================================================================
dlist = DList()
print(dlist.isEmpty())



dlist.insertSorted(100)
dlist.insertSorted(50)
dlist.insertSorted(200)
dlist.insertSorted(120)
dlist.insertSorted(115)
dlist.insertSorted(300)
dlist.insertSorted(250)
dlist.showList()
n = dlist.find(120)
dlist.remove(n)
dlist.showList()

