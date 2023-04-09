L='''
--Người---đâu-gặp---gỡ-làm-chi---
Trăm----năm-biết-có---duyên---gì--hay--không.
Ngổn-ngang---trăm-mối---bên---lòng----
----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình.
'''

L=''.join(L.split('----'))
L=' '.join(L.split('---'))
L=' '.join(L.split('--'))
L=' '.join(L.split('-'))
print(L[2:])