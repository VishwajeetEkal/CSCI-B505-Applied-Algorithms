def dcdMsg(count, fs= [], ss= []) :    
        fs_itr =0 
        ss_itr = 0
        temp =[]
        while fs_itr < len(fs) and ss_itr < len(ss):
            count+=1
            if fs[fs_itr]< ss[ss_itr]:
                temp.append(fs[fs_itr])
                fs_itr+=1
            else:
                temp.append(ss[ss_itr])
                ss_itr+=1

        if ss_itr < len(ss):
            temp+=ss[ss_itr:]
            
        
        if fs_itr < len(fs):
            temp+=fs[fs_itr:]
            

        return count,temp

def decode_cryptic_message(lists):
    dcdd_msg = lists[0]
    count = 0
    for i in range(1,len(lists)):
         count,dcdd_msg = dcdMsg(count,dcdd_msg, lists[i])
    print(count,len(dcdd_msg))
    return dcdd_msg


print(decode_cryptic_message([[1, 4, 5], [1, 6, 7], [3, 3]]))
print(decode_cryptic_message([[1, 2, 8], [3, 4, 9], [1, 2], [5, 7], [2, 3, 5, 7, 9]]))
print(decode_cryptic_message([[1, 2, 8], [3, 4, 9], [1, 2], [5, 7], [2, 3, 5, 7, 9],[3, 4, 9], [1, 2], [5, 7]]))