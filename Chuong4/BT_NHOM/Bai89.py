def VietHoa(s):
    xet=['.','?','!']
    s=s.capitalize() 
    for i in range(len(s)):
        if s[i] in xet:
            for j in range(i+1,len(s)):
                if s[j]!=' ': 
                    s=s[:j]+s[j:].capitalize()
                    break
                    
        if s[i] == 'i' and (i == 0 or s[i-1].isspace()) and (i == len(s)-1 or s[i+1].isspace()):
            s = s[:i] + 'I' + s[i+1:]
    return s

print(VietHoa(input()))