#EXAMPLE ON TIC-TAC-TOE
def tac(toe):
    if (toe['T1']=='X' and toe['T2']=='X' and toe['T3']=='X') or \
        (toe['M1']=='X' and toe['M2']=='X' and toe['M3']=='X') or \
        (toe['B1']=='X' and toe['B2']=='X' and toe['B3']=='X'):
        print('CONGRAGULATIONS! Player One Won The Match')
        return 1
    elif (toe['T1']=='X' and toe['M1']=='X' and toe['B1']=='X') or \
        (toe['T2']=='X' and toe['M2']=='X' and toe['B2']=='X') or \
        (toe['T3']=='X' and toe['M3']=='X' and toe['B3']=='X'):
        print('CONGRAGULATIONS! Player One Won The Match')
        return 1
    elif (toe['T1']=='X' and toe['M2']=='X' and toe['B3']=='X') or \
        (toe['T3']=='X' and toe['M2']=='X' and toe['B1']=='X'):
        print('CONGRAGULATIONS! Player One Won The Match')
        return 1
    elif (toe['T1']=='O' and toe['T2']=='O' and toe['T3']=='O') or \
        (toe['M1']=='O' and toe['M2']=='O' and toe['M3']=='O') or \
        (toe['B1']=='O' and toe['B2']=='O' and toe['B3']=='O'):
        print('CONGRAGULATIONS! Player Two Won The Match')
        return 1
    elif (toe['T1']=='O' and toe['M1']=='O' and toe['B1']=='O') or \
        (toe['T2']=='O' and toe['M2']=='O' and toe['B2']=='O') or \
        (toe['T3']=='O' and toe['M3']=='O' and toe['B3']=='O'):
        print('CONGRAGULATIONS! Player Two Won The Match')
        return 1
    elif (toe['T1']=='O' and toe['M2']=='O' and toe['B3']=='O') or \
        (toe['T3']=='O' and toe['M2']=='O' and toe['B1']=='O'):
        print('CONGRAGULATIONS! Player One Won The Match')
        return 1
    else:
        return 0
    
tic={'T1':' ','T2':' ','T3':' ',
     'M1':' ','M2':' ','M3':' ',
     'B1':' ','B2':' ','B3':' '}
print('SEE THE BELOW EXAMPLE YOU HAVE TO GIVE THE INPUT IN THE FOLLOWING MANNER')
print('T1'+'|'+'T2'+'|'+'T3')
print('--+--+--')
print('M1'+'|'+'M2'+'|'+'M3')
print('--+--+--')
print('B1'+'|'+'B2'+'|'+'B3')
print('--------------------------------------------------')
player=1
moves=0
end=0
while moves<10:
    print(tic['T1']+'|'+tic['T2']+'|'+tic['T3'])
    print('-+-+-')
    print(tic['M1']+'|'+tic['M2']+'|'+tic['M3'])
    print('-+-+-')
    print(tic['B1']+'|'+tic['B2']+'|'+tic['B3'])
    end=tac(tic)
    if end==1:
        break
    if moves!=9:
       if player==1:
         player_1=input('Player one: ')
         player_1=player_1.upper()
         if player_1 in tic and tic[player_1]==' ':
            tic[player_1]='X'
            player=2
         else:
            print('Invalid Input Please Try Again ')
            continue
       else:
         player_2=input('Player two: ')
         player_2=player_2.upper()
         if player_2 in tic and tic[player_2]==' ':
            tic[player_2]='O'
            player=1
         else:
            print('Invalid Input Please Try Again ')
    moves+=1
    print('--------------------------------------------------')
if end==0:
    print('Better Luck Next Time! Draw Match')
