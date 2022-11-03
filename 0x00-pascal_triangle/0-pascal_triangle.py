def print_triangle(n):
    """ Fonction qui definit un triangle de pascal
    args:
        n: la taille du triangle de pascal
    return:
        string - le triangle
    """
    previous = [1]
    for i in range(n):
        print(str(previous))
        ls = [1]
        if len(previous) <= 1:
            ls.append(1)
        else:
            for j in range(len(previous)-1):
                val = (previous[j] + previous[j+1])
                ls.append(val)
            ls.append(1)

        previous = ls

if __name__== '__main__':
    n = input('Entre la taille de ton triangle de pascal a creer : ')
    print_triangle(int(n))
            
            
            
        
    