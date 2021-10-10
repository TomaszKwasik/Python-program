def czy_pierwsza(liczba):
    j=2
    while liczba%j!=0:
        j=j+1
       
    if j==liczba:
        return True
    else:
        return False

a=int(input('Podaj wartość większą równą dwa:'))    
b=2

print('W zakresie od 2 do',a,'występują liczby pierwsze:')

while a>=b:
    
    if czy_pierwsza(b) == True:
        print(b)
   
    b=b+1
