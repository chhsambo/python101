with open('hello.txt', mode='a+') as f1:
    f1.write('Hello World!\n')
    f1.write('Hello Python\n')

    f1.seek(0)
    print(f1.read())
