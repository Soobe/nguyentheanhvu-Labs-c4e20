def get_even_list(l):
    numb_list = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
           numb_list.append(l[i])
         
    return numb_list
