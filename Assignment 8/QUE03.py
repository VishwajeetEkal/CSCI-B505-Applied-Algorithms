def findCircusStrings(circusString):
    def hash_string(s):
        
        hash_value = 0
        for char in s:
            hash_value = hash_value * 31 + ord(char)
        
        return hash_value

    seen_substrings = set()
    output = []

    
    for i in range(len(circusString) - 9):
        current_substring = circusString[i:i + 10]
        current_hash = hash_string(current_substring)

    
        if current_hash in seen_substrings and current_substring not in output: 
            output.append(current_substring)
        else:
            seen_substrings.add(current_hash)


    sorted(output)
    return output


print(findCircusStrings("WWWWWXXXXXWWWWWXXXXXXWWWWWYYYZZZ"))


print(findCircusStrings("WWWWWWWWWWWWW"))

print(findCircusStrings("YWYWYWYWYWYW"))

print(findCircusStrings("YWYWYWYWYWYWY"))

print(findCircusStrings("XXYYXXYYXXYYXX"))

print(findCircusStrings("XXYYXXYYXXYYXXYY"))

print(findCircusStrings("WWYWZXXYZXXXXXXWWYWZXXYZX"))

print(findCircusStrings("WWWWWYYYYYWWWWWYYYYYYWWWWWXXXXZZZ"))

print(findCircusStrings("XYWXYXWWZZZWYWWXYYYXXYXWXZYXWWXXWZZYXZXWYWXWWXYXWZYWYZZWWWZZZXWXWWYZYWZWYZYYXZZYXYWYWXYZYYYZZYYZYYZWYXYZWXYXXXYXZWZZXYXXXXZWWXYZYWXYYYWZZWZWWYYZXYXZZXXXYYWWZYXYXWYWXYWYZXZXXYYZZZWYXXZWYWXYZXZXWXYXYXYXWWYYXYZXWYZZXZXWXZWZXZXYXWXWYYZYZWZZXZWZZWYZZWZYYYZZXZXWXZWXWYZXYYZZWXZZXXZXWZXXWZZZXZYXWZWXYYYZXWWXZWWXWYZYZXWZYYYYZWZZYYYWWYYWZYXYZZZZZWWWXXXZXZXWYZWYXYXYWYYWZYXXXWXWWWZWXYWXYYXYYXXWXYYWZXZWWZYXYWWYXZWYXYWXYXZZZXXWYXWWXYWYXYXXXXWXZZWZYWXZYXYZYYYYXYXZXXYXZZZXXZWYWYWWXWZWYWZYYZYZZZZXYWWZXYZWWXXWXZZW"))
