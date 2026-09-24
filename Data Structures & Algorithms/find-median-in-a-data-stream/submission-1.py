class Heap:

    def __init__(self):
        self.heap = []
        self.size = 0
        
        # parent of i: (i - 1) // 2
        # left child of i: 2i + 1
        # right child of i: 2i + 2
    
    def push(self, elem):
        # push elem to bottom of heap
        # bubble elem up to spot (heapify)
        # heap must be complete bin tree
        # parent must always be >= child
        
        self.heap.append(elem)
        ind = len(self.heap) - 1
        self.size += 1
        

        while ind != 0 and self.heap[ind] > self.heap[(ind - 1) // 2]:
            # swap current elem and its parent
            current = self.heap[ind]
            parent_ind = ((ind - 1) // 2)
            self.heap[ind] = self.heap[parent_ind]
            self.heap[parent_ind] = current
            ind = parent_ind


 
    def pop(self):
        # swap root and bottom elem
        # drop bottom elem
        # trickle down (heapify)
        if self.heap:
            
            top = self.heap[0]
            self.heap[0] = self.heap[len(self.heap) - 1]
            self.heap = self.heap[:len(self.heap) - 1]
            self.size -= 1

            ind = 0
            
            # trickle down
            while True:
                
                # find left and right child
                # set a largest pointer to decide swap
                left = 2 * ind + 1
                right = 2 * ind + 2
                # largest prevents more swaps when correct
                # swap was made.
                largest = ind

                # check swap side comparing against value at index: largest
                if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                    largest = left
                if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                    largest = right
                
                # complete swap if largest isnt curr ind
                if largest != ind:
                    current = self.heap[ind]
                    self.heap[ind] = self.heap[largest]
                    self.heap[largest] = current
                    ind = largest
                    continue
                
                break

                # repeat until heap prop restored

            return top
        
        else:
            
            return None
    
    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None


    

class MedianFinder:

    def __init__(self):
        self.min_heap = Heap()
        self.max_heap = Heap()

    def addNum(self, num: int) -> None:
        self.max_heap.push(num)
        
        if self.min_heap.size and self.max_heap.peek() > -1 * self.min_heap.peek():
            temp = self.max_heap.pop()
            self.min_heap.push(-1 * temp)
        
        if self.max_heap.size > self.min_heap.size + 1:
            temp = self.max_heap.pop()
            self.min_heap.push(-1 * temp)

        if self.min_heap.size > self.max_heap.size:
            temp = self.min_heap.pop()
            self.max_heap.push(-1 * temp)

    def findMedian(self) -> float:
        total = self.max_heap.size + self.min_heap.size
        if total % 2 == 0:
            med = (self.max_heap.peek() + -1 * self.min_heap.peek()) / 2
        else:
            med = self.max_heap.peek()
        
        return med
        
        