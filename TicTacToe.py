
import random 

board={'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'}

# Funkcja, która przyjmuje jeden parametr zawierający bieżący stan tablicy
# i wyświetla go w oknie konsoli.

def display_board(board):

    print('\t',board['1']+'|'+board['2']+'|'+board['3'])
    print('\t','-----')
    print('\t',board['4']+'|'+board['5']+'|'+board['6'])
    print('\t','-----')
    print('\t',board['7']+'|'+board['8']+'|'+board['9'])

    

# Funkcja, która przyjmuje parametr odzwierciedlający biężący stan tablicy,
# prosi użytkownika o wykonanie ruchu, 
# sprawdza dane wejściowe i aktualizuje tablicę zgodnie z decyzją użytkownika.   

def enter_move(board):

    turn='X'
    
    print('Wykonaj ruch',turn,'podaj numer pola:')
    ruch=input()

    if board[ruch] != 'X' and board[ruch] != 'O':
        board[ruch]=turn
    else:
        print('Podane pole jest zajęte')
    return board[ruch]
       

# Funkcja, która wykonuje ruch za komputer i aktualizuje tablicę.

def draw_move(board):

    turn='O'

    print('Komputer wykonuje ruch\n')
    
    while True:
        ruch=str(random.randint(1,9))
        if board[ruch] != 'X' and board[ruch] != 'O':
              board[ruch]=turn
              break
        else:
            print('Podane pole jest zajęte')
        return board[ruch]

# Funkcja, która dokonuje analizy stanu tablicy w celu sprawdzenia
# czy użytkownik/gracz stosujący "O" lub "X" wygrał rozgrywkę.

def victory_for(board):
    if board['1']==board['2']==board['3']=='X':
        return board['1']
    elif board['4']==board['5']==board['6']=='X':
        return board['4']
    elif board['7']==board['8']==board['9']=='X':
        return board['7']
    elif board['1']==board['4']==board['7']=='X':
        return board['1']
    elif board['2']==board['5']==board['8']=='X':
        return board['2']
    elif board['3']==board['6']==board['9']=='X':
        return board['3']
    elif board['1']==board['5']==board['9']=='X':
        return board['7']
    elif board['3']==board['5']==board['7']=='X':
        return board['3']
    elif board['1']==board['2']==board['3']=='O':
        return board['1']
    elif board['4']==board['5']==board['6']=='O':
        return board['4']
    elif board['7']==board['8']==board['9']=='O':
        return board['7']
    elif board['1']==board['4']==board['7']=='O':
        return board['1']
    elif board['2']==board['5']==board['8']=='O':
        return board['2']
    elif board['3']==board['6']==board['9']=='O':
        return board['3']
    elif board['1']==board['5']==board['9']=='O':
        return board['7']
    elif board['3']==board['5']==board['7']=='O':
        return board['3']
    

            
n=0

turn='X'
display_board(board)

while n <= 9:
    
    if turn == 'X':
        enter_move(board)
       
                
    else:
        draw_move(board)
        
         
    display_board(board)

    if victory_for(board)=='X':
        print('Wgrał człwiek')
        break
    if victory_for(board)=='O':
        print('Wgrał komputer')
        break

    if turn == 'X':
        turn='O'
    else:
        turn='X'
    
    n=n+1
    
    if n > 9:
        print('Liczba 9 ruchów została wykorzystan. Rozgrywka jest nierozstrzygnieta')


    
    
    
          
    

    
    

    

    




    
    
        
        

    

    

    
        
    




    




