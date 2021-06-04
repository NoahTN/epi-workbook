from typing import OrderedDict

class ISBNCache:
   def __init__(self, size):
      self.cache = OrderedDict()
      self.size = size

   # O(1)
   def lookup(self, isbn):
      if isbn in self.cache:
         self.cache.move_to_end(isbn)
         return self.cache[isbn]
      return -1

   # O(1)
   def insert(self, isbn, price):
      if isbn in self.cache:
         del self.cache[isbn]
      self.cache[isbn] = price
      
      if len(self.cache) > self.size:
         self.cache.popitem(last=False) # Remove least recent isbn
   
   # O(1)
   def remove(self, isbn):
      return self.cache.pop(isbn, None) is not None
