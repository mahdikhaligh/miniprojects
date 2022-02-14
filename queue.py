######
# Q-3
class Queue:
    """
    init -> create  list (self.items == [])
    can your use method :
    [   
        isempty -> return (true or flase)
        additem -> add (int )
        remove ->  pop item and return items 
        sizeitems -> return len(self.items)
        show ->  return self.items (see you element)
    ]
    """
    def __init__(self):
        self.items = []
    
    def isempty(self):
        return self.items == []
    
    def  additem(self,item):
        self.items.insert(0,item)
    
    def remove (self):
        return self.items.pop()
    
    def sizeItems(self):
        return len(self.items)
    
    def show(self):
        return self.items
    

def main():
    queue = Queue()
    while True:
        item = input(" pls enter your number and you for end  enter off \n (number or off):")
        if item == 'off':
            break
        queue.additem( int(item))      
    items = queue.show()
    print(items)    
    
if __name__ == "__main__":
    main()
    
########
# Q-1
# 8,7,6,5,4,3,2,1 
#  ---->
# | 8 |
# | 7 |
# | 6 |
# | 5 |      -> stack 
# | 4 |
# | 3 |
# | 2 | 
# | 1 | 
#############
#Q-2
# isFull -> if top1[i] == top2[i]:
#                   return 1
#   yani zamani ke index khone top1,top2 be yek khone dar array eshare konanad array isfull hast 
#
#isempty -> if top1[i] <= 0 or top2[i] <= maxsize-1:
#                   return 1
# zamani ke top1[i] <= 0 bashe and baraye top2[i] <= maxsize-1 bashe mishe goft array isempty hast 
#

