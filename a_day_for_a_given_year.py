
#funkcja zwraca dzień dla podanych liczb

def rok_miesiac_dzien(rok,miesiac,dzien): 

    p=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    np=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    d_t=['poniedziałek','wtorek','środa','czwartek','piątek','sobota','niedziela']

    d_t_365=53*d_t 
    d_t_365=d_t_365[:-6] #lista zawierająca 365 dni, 

    d_t_366=53*d_t
    d_t_366=d_t_366[:-5] #lista zawirająca 366 dni

    s=0
    d=0
    if rok%4 == 0 and miesiac >= 1 and miesiac <= 12:
        for i in range(len(p)+1):
            if i==miesiac:
                for j in range(miesiac):
                    s=s+p[j]
                    
                d=s-(dzien-p[miesiac-1])*(-1)
                

                print('Szukany dzień to:',d_t_366[d-1])
    

    elif rok%4 != 0 and miesiac >= 1 and miesiac <= 12:
        for i in range(len(np)+1):
            if i==miesiac:
                for j in range(miesiac):
                    s=s+np[j]
                    
                d=s-(dzien-np[miesiac-1])*(-1)
                

                print('Szukany dzień to:',d_t_365[d-1])
    else:
        return None


rok_miesiac_dzien(2000,2,29)
rok_miesiac_dzien(2001,2,28)
print(rok_miesiac_dzien(2002,13,28))

                
