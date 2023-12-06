def minimum_balls(c1, c2, c3, c4, c5, p):
  balls = [c1,c2,c3,c4,c5]
  count = 0
  for i in balls:
    if p <= i:
      count+=p-1
    if p > i:
      count+=i
  return count+1

def longestBlues(tiles: list[int], k) -> int:
  max = 0
  count = 0
  number_of_tiles = 0
  for i in tiles:
    if i == "blue":
      count +=1
    else:
      if max < count:
        max = count
      count = 0
  i = 0
  j,window = len (tiles),len (tiles)
  while i != j:
    if tiles[i:j].count("pink")== k:
      return j-i
    i+=1
    j+=1
    if j > len(tiles):
      i = 0
      window-=1
      j = window

def CandiesLog(s):
    a ={ key:0 for key in s if key>= 'a' and key <='z'}

    total_kids=0
    f = 0
    count = 0

    for i in s:
      if i >= 'a' and i <='z':
        temp = i
        total_kids+=1
        count = 0
        f=0
      else:
        if count:
          a[temp]-= f
          f *=10

        f += int(i)
        a[temp] +=f
        count+=1

    answer = "K"+str(total_kids)+"T"+str(sum(a.values()))

    for i in sorted(a):
      answer += i+str(a[i])

    res = answer
    return res

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class HeimdallQuest():
  def reverse_k_steps(self,head, k):
    if k > head.value or k ==1 :
      return head.next
    loop = int(head.value/k)
    count = 0
    i = 0
    prev, next, temp1, temp2 = None, None, head.next, head
    cur = head.next
    while(cur is not None and i != loop ):
      next = cur.next

      cur.next = prev

      prev = cur

      cur = next

      count+=1

      if count == k and i < loop:
          temp1.next = cur

          temp2.next = prev

          temp2 = temp1

          temp1 = cur

          i += 1

          count = 0

    #head = head.next

    return head.next

  def get_linked_list(self,head):
    temp = head
    res = []
    while True:
      res.append(temp.value)
      if temp.next != None:
        temp = temp.next
      else:
        break
    return res

  def create_linked_list(self,lst):
    temp = temp1 = Node(len(lst))
    for i in lst:
      temp1.next = Node(i)
      temp1 = temp1.next
    return temp
