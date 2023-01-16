import time
import random
import matplotlib.pyplot as plt
import graphviz

class Node:
    def __init__(self,key=None,next=None):
        self.key = key
        self.next = next


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    
    def searchNode(self,i):
        cur = self.head
        while(i > 0):
            if(cur == None): return None
            cur = cur.next
            i = i - 1
        return cur


    # Get parent
    def get_parent(self,i):
        if i > 0:
            return self.searchNode((i-1)//2)
        else:
            return None

    # Get left child
    def get_left_child(self,i):
        return self.searchNode(2*i + 1)

    # Get right child
    def get_right_child(self,i):
        return self.searchNode(2*i + 2)


   
    def insert(self, key):
        node = Node(key)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node
        
        index = self.size
        self.size = self.size + 1
       
    
        while(index != 0):
            parent = self.get_parent(index)
            if(parent.key <= key):break
            tmp = parent.key
            parent.key = key
            node.key = tmp
            index = (index-1)//2
            node = parent

    def _has_left(self,index):
        # determine if there is a left child
        return index * 2 + 1 < self.size

        
    def _has_right(self,index):
        # determine if there is a left child
        return index * 2 + 2 < self.size


    def delMin(self):
        if self.head is None:
            return None

        self.head.key = self.tail.key
        
        cur = self.head
        index = 0
  
        self.size = self.size - 1
        self.tail = self.searchNode(self.size-1)
        self.tail.next = None

        while(self._has_left(index)):
            left = self.get_left_child(index)
            small_child = left
            small_child_index = index * 2 + 1
            if(self._has_right(index)):
                right = self.get_right_child(index)
                if(left.key > right.key):
                    small_child = right
                    small_child_index = index * 2 + 2
            if(small_child.key >= cur.key):
                return
            else:
                tmp = small_child.key
                small_child.key = cur.key
                cur.key = tmp
            cur = small_child
            index = small_child_index
        


def Q4():
    data = []
    for i in range(1000):
        data.append(random.randint(0, 100000))

    priority_queue = PriorityQueue()

    start = time.time()
    for i in data:
        priority_queue.insert(i)
    end = time.time()
    insert_time = end - start

    start = time.time()
    for i in range(len(data)):
        priority_queue.delMin()
    end = time.time()
    delMin_time = end - start

    x = ['Insert', 'DelMin']
    y = [insert_time, delMin_time]

    plt.bar(x,y)
    plt.title('Linked List based PriorityQueue Performance')
    plt.xlabel('Operation')
    plt.ylabel('Time (s)')
    plt.show()




def dfs_add_edge(priority_queue,g,cur,index):
    left = priority_queue.get_left_child(index)
    if(left == None): return
    g.edge(str(cur.key), str(left.key))
    right = priority_queue.get_right_child(index)
    if(right == None): return
    g.edge(str(cur.key), str(right.key))
    
    dfs_add_edge(priority_queue,g,left,index*2+1)
    dfs_add_edge(priority_queue,g,right,index*2+2)

def Q5():

    priority_queue = PriorityQueue() 
    for i in range(10):
        priority_queue.insert(9-i)


    # Create graph
    g = graphviz.Digraph('PriorityQueue', filename='PriorityQueue.gv', format='png')

    g.node_attr['shape'] = 'circle'
    g.node_attr['style'] = 'filled'

    cur = priority_queue.head
    while cur:
        g.node(str(cur.key),fillcolor='green')
        cur = cur.next

    cur = priority_queue.head
    index = 0

   
    dfs_add_edge(priority_queue,g,cur,index)

    g.render()


