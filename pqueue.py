from math import floor

class PQueue:
    def __init__(self, compare):
        self.tree = []
        self.compare = compare
    
    def insert(self, value):
        self.tree.append(value)
        self.heap_fix_up(len(self.tree) - 1)
    
    def heap_fix_up(self, i):
        p = floor((i-1)/2)

        while p >= 0 and self.compare(self.tree[i],self.tree[p]):
            self.tree[i], self.tree[p] = self.tree[p], self.tree[i]
            i = p
            p = floor((i-1)/2)
    
    def size(self):
        return len(self.tree)
    
    def minimum(self):
        minimum = self.tree[0]
        self.tree[0] = self.tree[len(self.tree) - 1]
        self.tree.pop()

        i = 0
        left_i = (i*2 + 1)
        right_i = (i*2 + 2)
        while left_i < self.size() and right_i < self.size():
            if not self.compare(self.tree[i], self.tree[left_i]) and not self.compare(self.tree[i], self.tree[right_i]):
                if self.compare(self.tree[left_i], self.tree[right_i]):
                    self.tree[i], self.tree[left_i] = self.tree[left_i], self.tree[i]
                    i = left_i
                else:
                    self.tree[i], self.tree[right_i] = self.tree[right_i], self.tree[i]
                    i = right_i
            elif not self.compare(self.tree[i], self.tree[left_i]):
                self.tree[i], self.tree[left_i] = self.tree[left_i], self.tree[i]
                i = left_i
            elif not self.compare(self.tree[i], self.tree[right_i]):
                self.tree[i], self.tree[right_i] = self.tree[right_i], self.tree[i]
                i = right_i
            else:
                return minimum
            left_i = (i*2 + 1)
            right_i = (i*2 + 2)
        
        if left_i < self.size() and not self.compare(self.tree[i], self.tree[left_i]):
            self.tree[i], self.tree[left_i] = self.tree[left_i], self.tree[i]
            i = left_i
        
        return minimum
        