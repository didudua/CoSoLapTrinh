def isInteger(s):
    s = s.strip()
    if len(s) == 0:
        return False
    if s[0] in ['+', '-']:
        s = s[1:]
    for i in s:
        if not i.isdigit():
            return False
    return True

def thuc_hien():
    s = input("Nhập một chuỗi: ")
    if isInteger(s):
        print('Chuỗi vừa nhập là một số nguyên')
    else:
        print("Chuỗi vừa nhập không phải là một số nguyên")

if __name__=="__main__":
    thuc_hien()
