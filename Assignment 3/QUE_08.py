class amor_dict():
    def __init__(self, num_list = []):
        self.amort_dict = []
        i = 1
        while 2**i < len(num_list):
            i+=1
        self.lvl = i
        
        for i in range(self.lvl):
            self.amort_dict.append([])
        

        for i in num_list:
            self.insert(i)
    
    def insert(self, num):
        if not self.amort_dict[0]:
            self.amort_dict[0].append(num)
            return 
        else:
            self.amort_dict[0] = self.merge_list(self.amort_dict[0], [num])
            self.merge_list_insert(0)

    def merge_list(self,a= [], b= []) :
        
        i =0 
        j = 0
        temp =[]
        while i < len(a) and j < len(b):
            
            if a[i]< b[j]:
                temp.append(a[i])
                i+=1
            else:
                temp.append(b[j])
                j+=1

        while j < len(b):
            temp.append(b[j])
            j+=1
        
        while i < len(a):
            temp.append(a[i])
            i+=1

        return temp
    
    def merge_list_insert(self, curLevel):
        nexLevel = curLevel+1
        if nexLevel >= self.lvl:
            self.buildLevel()
        if not self.amort_dict[nexLevel]:
            self.amort_dict[nexLevel] = self.merge_list(self.amort_dict[nexLevel],self.amort_dict[curLevel] )
            self.amort_dict[curLevel] = []
            return  
        self.amort_dict[nexLevel] = self.merge_list(self.amort_dict[nexLevel],self.amort_dict[curLevel]  )
        self.amort_dict[curLevel] = []
        self.merge_list_insert(nexLevel)

    def buildLevel(self):
        self.amort_dict.append([])
        self.lvl+=1

    def search(self, num):
        for i in zip(self.amort_dict, range(self.lvl) ):
            if i[0] and i[0][-1] >= num and i[0][0] <=num:
                left = 0
                right = len(i[0])
                while left <= right:
                    
                    mid = int( ( left+right ) / 2  )
                    if i[0][mid] == num:
                        return i[1]
                    
                    elif num >i[0][mid]      :
                        left = mid +1
                        
                    else:
                        right = mid-1
                        
        return -1

    
    
    def print(self):
        result = []
        for i in range(self.lvl):
            result+=[self.amort_dict[i][:]]
        
        return result


ad = amor_dict()
print(ad.search(75))
print(ad.print())
ad.insert(16)
print(ad.print())
print(ad.search(16))
ad.insert(74)
print(ad.print())
print(ad.search(75))
