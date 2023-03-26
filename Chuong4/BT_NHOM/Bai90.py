def isInteger(s):
    s=s.strip()
    
    if (s[0]== "+" or s[0]== "-") and s[1:].isdigit():
        return True
    if s.isdigit():
        return True
    return False

def main():
    s= input("Nhập một chuỗi: ")
    if isInteger(s):
        print('chuỗi vừa nhập là một số nguyên')
    else:
        print("chuỗi vừa nhập không phải là một số nguyên")  
if __name__=="__main__":
    main()