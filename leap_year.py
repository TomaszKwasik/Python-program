# Sprawdzenie czy dany rok przestęony

rok=int(input('Podaj rok: '))
miesiac=int(input('Podaj miesiąc w postaci liczby: '))
    
p=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
np=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
if rok%4 == 0 and miesiac >= 1 and miesiac <= 12:
    print('Podany rok jest przestępny.')
    for i in range(len(p)+1):
        if i==miesiac:
            print('Liczba dni dla podanego miesięca wynosi: ',p[i-1])
elif rok%4 != 0 and miesiac >= 1 and miesiac <= 12:
    print('Podany rok jest nieprzestępny')
    for i in range(len(np)+1):
        if i==miesiac:
            print('Liczba dni dla podanego miesięca wynosi: ',np[i-1])
else:
    print(None)
    
        
    
    



    
        



