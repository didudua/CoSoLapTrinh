L='''
--Người---đâu-gặp---gỡ-làm-chi---
Trăm----năm-biết-có---duyên---gì--hay--không.
Ngổn-ngang---trăm-mối---bên---lòng----
----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình.
'''

def XuLyDong(L) :
    L=L.split("-")
    while '' in L : L.remove("")
    return " ".join(L)
def xuly(L):
    L=L.split("\n")
    for i in L:
        print(XuLyDong(i))
xuly(L)