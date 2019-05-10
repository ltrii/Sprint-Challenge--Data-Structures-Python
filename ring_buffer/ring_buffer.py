class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    self.max = 0

  def append(self, item):
    self.storage[self.current] = item
    self.current += 1
    self.current %= self.capacity
    self.max += 1 if self.max < self.capacity else self.capacity

  def get(self):
    if max < self.capacity:
      return self.storage[:self.max]
    else:
      return self.storage
