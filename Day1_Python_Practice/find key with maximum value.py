marks={'a':10,'b':20, 'c':320, 'd':97 }
maxkey=list(marks.keys())[0]
maxvalue=marks[maxkey]
for key,value in marks.items():
    if value>maxvalue:
        maxkey=key
        maxvalue=value 

print(maxkey)