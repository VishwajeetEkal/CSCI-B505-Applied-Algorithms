import copy

def generate_password(word_list):
    word_list_copy = copy.deepcopy(word_list)
    word_list_copy.sort()
    while len(word_list_copy) > 1:
        best_overlap_length = 0
        best_positions = (0, 1)

        for idx_1 in range(len(word_list_copy)):
            
            for idx_2 in range(idx_1 + 1, len(word_list_copy)):
                
                overlap_length = find_overlap(word_list_copy[idx_1], word_list_copy[idx_2])
                if overlap_length > best_overlap_length:
                    best_overlap_length = overlap_length
                    best_positions = (idx_1, idx_2)

        pos_1, pos_2 = best_positions
        if word_list_copy[pos_1] in word_list_copy[pos_2]:
            combined_word = word_list_copy[pos_2]
        elif word_list_copy[pos_2] in word_list_copy[pos_1]:
            combined_word = word_list_copy[pos_1]
        else:
            combined_word = combine_words(word_list_copy[pos_1], word_list_copy[pos_2], best_overlap_length)
        word_list_copy.pop(pos_2)
        word_list_copy[pos_1] = combined_word

    return word_list_copy[0]

def find_overlap(firstStr, secondStr):
    best_overlap_length = 0
    min_len = min(len(firstStr), len(secondStr))

    for i in range(1, min_len):
        if firstStr.endswith(secondStr[:i]):
            best_overlap_length = i

    return best_overlap_length

def combine_words(firstStr, secondStr, overlap):
    return firstStr + secondStr[overlap:]



# Example usage:
words1 = ['XYY', 'YYX']
print(generate_password(words1))  # Output: 'XYYX'

words2 = ['XYYZXY', 'ZXYXXXY', 'XYZZX']
print(generate_password(words2))  # Output: 'XYYZXYXXXYZZX'

words3 = ["XYZWX", "XZYYWZ", "WXZY", "ZZXY", "YZWXYZX"]
print(generate_password(words3))  # Output: 'WXZYYWZZXYZWXYZX'

words4 = ["XXZXY", "XZX", "YYYYYY"]
print(generate_password(words4)) 