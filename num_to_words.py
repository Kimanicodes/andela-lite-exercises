def num_to_words(num):
    s = str(num)
    for i in s:
        if i is '1':
            print('One')
        if i is '2':
            print('Two')
        if i is '3':
            print('Three')
        if i is '4':
            print('Four')
        if i is '5':
            print('Five')
        if i is '6':
            print('Six')
        if i is '7':
            print('Seven')
        if i is '8':
            print('Eight')
        if i is '9':
            print('Nine')
        if i is '0':
            print('Zero')

'''Testing it Out'''
num_to_words(438483478)
