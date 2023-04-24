kitu='@#$'
mk=input()
kt=False
while 6<=len(mk) and len(mk)<=17:
    if any(i for i in mk if i in kitu): 
        if any(i for i in mk if i.isupper()):
            if any(i for i in mk if i.isalpha()):
                kt=True
                break
    else:
        break
print(kt)