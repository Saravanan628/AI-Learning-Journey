with (open("employees_list.txt") as file):
    data=file.read()
    words=data.split()
    maxlength=0
    word=''
    for text in words:
        if len(text)>maxlength:
            maxlength=len(text)
            word=text
    print(word)