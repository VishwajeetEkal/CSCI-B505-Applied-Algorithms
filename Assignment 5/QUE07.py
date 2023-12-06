import heapq as hp

class Huffman():
    def __init__(self):
        self.huffman_codes = {}
        self.source_string = ""
    
    def set_source_string(self, src_str):
        self.source_string = src_str
   
    def generate_codes(self):
        huffman_codes = {}
        characterCount = {}
        for sourceStringItr in self.source_string:
            if sourceStringItr not in characterCount:
                characterCount[sourceStringItr] = 1
                huffman_codes[sourceStringItr] = ""
            else:
                characterCount[sourceStringItr] += 1
        
        characterCountHeap = []

        for i in characterCount:
            hp.heappush(characterCountHeap,(characterCount[i],i))
        
        while len(characterCountHeap) > 1 :
            firstLowFreq, firstLowString = hp.heappop(characterCountHeap)
            secondLowFreq, secondLowString = hp.heappop(characterCountHeap)

            for itrString in firstLowString:
                huffman_codes[itrString]= '0'+huffman_codes[itrString]
            
            for itrString in secondLowString:
                huffman_codes[itrString]= '1'+huffman_codes[itrString]

            hp.heappush(characterCountHeap,(firstLowFreq+secondLowFreq, firstLowString+secondLowString))

        self.huffman_codes = huffman_codes
   
    def encode_message(self, message_to_encode):
        encoded_msg = ""
        
        for msgChar in message_to_encode:
            encoded_msg += self.huffman_codes[msgChar]

        return encoded_msg

    def decode_message(self, encoded_msg):
        decoded_msg = ""
        invertedHuffman = dict(zip(self.huffman_codes.values(), self.huffman_codes.keys()))
        currenString=''
        for msgChar in encoded_msg:
            currenString +=msgChar
            if currenString  in invertedHuffman:
                    decoded_msg += invertedHuffman[currenString]
                    currenString =''
        return decoded_msg
    


    


