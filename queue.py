
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
        item = input(" pls enter your number and you for exit enter (off) \n (number or off) ->")
        if item == 'off':
            break
        queue.additem(int(item))      
    items = queue.show()
    print(items)    
    
if __name__ == "__main__":
    main()
    
    
         			    ###########################################
                                    #     + +++++ +                           #
                                ### #    +         +              + +++ +     # ###
                                #   #   +     $     +           +    _    +   #   #
                                ### #    +         +  _python_  +         +   # ###
                                    #     + +++++ +               + +++ +     #
                                    #                                         #                                  
                                    #     https://github.com/mahdikhaligh     #
                                    #                                         #
                                    ###########################################
    
