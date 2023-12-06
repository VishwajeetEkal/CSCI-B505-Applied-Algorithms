def amountPoliceGets(people):
  stack = []
  total_sum = 0
  for i in people:
    if not stack:
      stack.append(i)
    elif stack[-1][0] == 1 and i[0] == 0:
      while stack and stack[-1][0] == 1:
          total_sum += stack[-1][1]
          stack.pop()
      stack.append([0,i[1]])
    elif stack[-1][0] == 1 and i[0] == -1:
      while stack and stack[-1][0] == 1:
          total_sum += stack[-1][1]
          stack.pop()
      total_sum +=i[1]
      stack.append([0,i[1]])
      stack.append([0,sum])
    elif stack[-1][0] == 0 and i[0] == -1:
      total_sum += i[1]
      stack.pop()
      stack.append([0,i[1]])
    else:
      stack.append(i)

  print(total_sum)

class Queue:
  DEFAULT_SIZE = 10

  def __init__(self):
    self.max = self.DEFAULT_SIZE
    self.que = [0]*self.max
    self.front, self.end = 0,0
    self.size = 0
  pass

  def enque(self, value):
    if self.size >= self.max:
      return False
    self.que[(self.end)%self.max] = value
    self.end +=1
    self.size+=1
    print(self.que)
    return True

  def deque(self):
    if self.front == self.end:
      return -1
    value = self.que[(self.front%self.max)]
    self.front+=1
    self.size-=1
    print(self.que,"#")
    return value

def isItPossible(initial: list[str], final: list[str]) -> bool:
  in_ind = 0
  inm = []
  fn_ind = len(final)-1
  while fn_ind>=0 or in_ind <len(initial):
    print(in_ind, fn_ind)
    if in_ind== len(initial):
      if initial[inm[-1]] != final[fn_ind]:
        return False
      fn_ind -=1
      inm.pop()
    elif initial[in_ind] == final[fn_ind]:
        in_ind +=1
        fn_ind -=1
    else:
      if inm and initial[inm[-1]] == final[fn_ind]:
        fn_ind -=1
        inm.pop()
      elif not inm or inm:
        inm.append(in_ind)
        in_ind+=1
    print(inm)

  return True

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    self.down = None
  
class SkipList:
  def __init__(self):
    self.start = Node(float("-inf"))
    self.level = 1
    
  def getProb(self):
    height= 1  
    while random.random() < 0.5:
        height += 1

    return height 

  def buildSentinelLevel(self,p):
    if p >= self.level:
      i = 0
      while i< p-self.level:
        nS = Node(float("-inf"))
        nS.down = self.start
        self.start = nS
        i+=1
      self.level= p

  def buildLevel(self,p, update, num):
    update = update[-p:]
    dNode = None
    for i in range(len(update)-1,-1,-1) :
      new_node = Node(num)
      new_node.next = update[i].next
      new_node.down = dNode
      update[i].next = new_node
      dNode = new_node

  def search(self, target: int) -> bool:
      cur = self.start
      while cur:
          while cur.next and cur.next.val < target:
              cur = cur.next
          if cur.next and cur.next.val == target:
              return True
          cur = cur.down  
      return False

  def insert(self, num: int) -> None:
    update = []
    p = self.getProb()
    self.buildSentinelLevel(p)
    cur = self.start
    while cur:
      while cur.next and cur.next.val < num:
        cur = cur.next
      update.append(cur)
      cur = cur.down
    self.buildLevel(p,update,num)

  def display(self):
    cur = self.start
    print("***************")
    while cur:
      temp = cur
      while temp:
        print(temp.val,end=" ")
        temp = temp.next
      print("")
      cur = cur.down
