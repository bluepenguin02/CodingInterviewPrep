"""
146. LRU Cache
https://leetcode.com/problems/lru-cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

* LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
* int get(int key) Return the value of the key if the key exists, otherwise return -1.
* void put(int key, int value) Update the value of the key if the key exists. Otherwise,
  add the key-value pair to the cache. If the number of keys exceeds the capacity from this
  operation, evict the least recently used key.
  
The functions get and put must each run in O(1) average time complexity.
"""

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from typing import Optional

class LLNode:
    def __init__(self, key, val):
      self.key = key
      self.val = val
      self.prev: Optional[LLNode] = None
      self.next: Optional[LLNode] = None
      

class LRUCache:
    def __init__(self, capacity: int):
      self.LLHead = LLNode(None, None)
      self.LLTail = LLNode(None, None)
      self.LLHead.next = self.LLTail
      self.LLTail.prev = self.LLHead
      self.capacity = capacity
      self.cache = {}
        
    def get(self, key: int) -> int:
      if key not in self.cache:
        return -1
      
      CurrNode = self.cache[key]    
      
      #removing current element
      CurrNode.next.prev = CurrNode.prev
      CurrNode.prev.next = CurrNode.next
      #attaching at tail
      CurrNode.prev = self.LLTail.prev
      self.LLTail.prev.next = CurrNode #type: ignore
      self.LLTail.prev = CurrNode
      CurrNode.next = self.LLTail
      
      return CurrNode.val
        
    def put(self, key: int, value: int) -> None:
      #if key already exists
      if key in self.cache:
        self.get(key)
        self.cache[key].val = value
        return
      
      #checking capacity
      if len(self.cache) == self.capacity:
        CurrNode = self.LLHead.next
        self.LLHead.next.next.prev = self.LLHead #type: ignore
        self.LLHead.next = self.LLHead.next.next #type: ignore
        self.cache.pop(CurrNode.key) #type: ignore
        
      NewNode = LLNode(key, value)
      self.LLTail.prev.next = NewNode #type: ignore
      NewNode.prev = self.LLTail.prev
      NewNode.next = self.LLTail #type: ignore
      self.LLTail.prev = NewNode #type: ignore
      
      self.cache[key] = NewNode
      return
  
lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(1))    # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))    # returns -1 (not found)
lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))    # return -1 (not found)
print(lRUCache.get(3))    # return 3
print(lRUCache.get(4))    # return 4
