
# Funkcja zwraca ciąg liczb naturalnych zakończonych wartością 1
def collatz(number):
	if number%2==0:
		return number/2
	else:
		return 3*number+1

print('Podaj liczbę:')


num=int(input())

print('Ciąg liczb:')

while num!=1:
        collatz(num)
        
        print(collatz(num))
        
        num=collatz(num)

        
        
        
    
