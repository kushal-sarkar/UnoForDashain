#UNO winner counter.
AtoB = 0
AtoC = 0
AtoD = 0
BtoA = 0
BtoC = 0
BtoD = 0
CtoA = 0
CtoB = 0
CtoD = 0
DtoA = 0
DtoB = 0
DtoC = 0
print('Instructions:\n 1) To print the winners list, type w. \n 2) To end the game and show result, type done.\n 3) "Someone le Someone lai 0 dinu parxa" is a DRAW.')

print('')
print('-- Enter 2-4 Players --')
totalPlayers = int(input('How many players are playing UNO?: ')) #takes number of player.


playersName = []
u = int(input('Kati bot ko khelne ho?: '))
winners = []
for i in range(totalPlayers):
    name = str.lower(input('Enter Player name: '))
    playersName.append(name)

print('')

if totalPlayers == 2:
    while True:
        winnerName = str.lower(input('Who is the winner of this round? : '))
        if winnerName == 'done':
            break
        elif winnerName in playersName:
            winners.append(winnerName)
        elif winnerName == 'w':
            print(winners)
        else:
            print('Invalid player, Psycho!!')
        print('')
        if winnerName == playersName[0]:
            BtoA = BtoA + u
        else:
            AtoB = AtoB + u
    if BtoA > AtoB:
        amount = abs(BtoA - AtoB)
        print( playersName[1], " le ", playersName[0], " lai Rs.",amount, " dinu parcha.")
    elif BtoA == AtoB:
        print('DRAW')
    else:
        amount = abs(AtoB -BtoA)
        print( playersName[0], " le ", playersName[1], " lai Rs.",amount, " dinu parcha.")
    
elif totalPlayers == 3:
    while True:
        winnerName = str.lower(input('Who is the winner of this round? : '))
        if winnerName == 'done':
            break
        elif winnerName in playersName:
            winners.append(winnerName)
        elif winnerName == 'w':
            print(winners)
        else:
            print('Invalid player, Psycho!!')
        print('')
        if winnerName == playersName[0]:
            BtoA = BtoA + u
            CtoA = CtoA + u
        elif winnerName == playersName[1]:
            AtoB = AtoB + u
            CtoB = CtoB + u
        else:
            AtoC = AtoC + u
            BtoC = BtoC + u
    if BtoA>= AtoB and CtoA>= AtoC:
        amount = abs(BtoA - AtoB)
        amount1 = abs(CtoA - AtoC)
        print( playersName[1], ' le ', playersName[0], ' lai ', amount, ' dinu parcha.')
        print( playersName[2], ' le ', playersName[0], ' lai ', amount1, ' dinu parcha.')
        if CtoB>= BtoC:
            next_amt = abs(CtoB - BtoC)
            print( playersName[2], ' le ', playersName[1], ' lai ', next_amt, ' dinu parcha.' )
        else:
            next_amt = abs(BtoC - CtoB)
            print( playersName[1], ' le ', playersName[2], ' lai ', next_amt, ' dinu parcha.' )
    elif AtoB>= BtoA and CtoB>= BtoC:
        amount = abs(AtoB - BtoC)
        amount1 = abs(CtoB - BtoC)
        print( playersName[0], ' le ', playersName[1], ' lai ', amount, ' dinu parcha.')
        print( playersName[2], ' le ', playersName[1], ' lai ', amount1, ' dinu parcha.')
        if CtoA>= AtoC:
            next_amt = abs(CtoA - AtoC)
            print( playersName[2], ' le ', playersName[0], ' lai ', next_amt, ' dinu parcha.' )
        else:
            next_amt = abs(AtoC - CtoA)
            print( playersName[0], ' le ', playersName[2], ' lai ', next_amt, ' dinu parcha.' )
        
    elif AtoC>= CtoA and BtoC>= CtoB:
        amount = abs(AtoC - CtoA)
        amount1 = abs(BtoC - CtoB)
        print( playersName[0], ' le ', playersName[2], ' lai ', amount, ' dinu parcha.')
        print( playersName[1], ' le ', playersName[2], ' lai ', amount1, ' dinu parcha.')
        if AtoB>= BtoA:
            next_amt = abs(AtoB - BtoA)
            print( playersName[0], ' le ', playersName[1], ' lai ', next_amt, ' dinu parcha.' )
        else:
            next_amt = abs(BtoA - AtoB)
            print( playersName[1], ' le ', playersName[0], ' lai ', next_amt, ' dinu parcha.' )

    
elif totalPlayers == 4:
    while True:
        winnerName = str.lower(input('Who is the winner of this round? : '))
        if winnerName == 'done':
            break
        elif winnerName in playersName:
            winners.append(winnerName)
        elif winnerName == 'w':
            print(winners)
        else:
            print('Invalid player, Psycho!!')
        print('')
        if winnerName == playersName[0]:
            BtoA = BtoA + u
            CtoA = CtoA + u
            DtoA = DtoA + u
        elif winnerName == playersName[1]:
            AtoB = AtoB + u
            CtoB = CtoB + u
            DtoB = DtoB + u
        elif winnerName == playersName[2]:
            AtoC = AtoC + u
            BtoC = BtoC + u
            DtoC = DtoC + u
        elif winnerName == playersName[3]:
            AtoD = AtoD + u
            BtoD = BtoD + u
            CtoD = CtoD + u
    
    if BtoA>= AtoB and CtoA>= AtoC and DtoA>= AtoD:
        amount = abs(BtoA - AtoB)
        amount1 = abs(CtoA - AtoC)
        amount2 = abs(DtoA - AtoD)
        print( playersName[1], ' le ', playersName[0], ' lai ', amount, ' dinu parcha.')
        print( playersName[2], ' le ', playersName[0], ' lai ', amount1, ' dinu parcha.')
        print( playersName[3], ' le ', playersName[0], ' lai ', amount2, ' dinu parcha.')
       
        if DtoB>= BtoD and CtoB>= BtoC:
            next_amt1 = abs(DtoB - BtoD)
            next_amt2 = abs(CtoB - BtoC)
            print( playersName[3], ' le ', playersName[1], ' lai ', next_amt1, ' dinu parcha.')
            print( playersName[2], ' le ', playersName[1], ' lai ', next_amt2, ' dinu parcha.')
            if DtoC>= CtoD:
                next_amt3 = abs(DtoC - CtoD)
                print( playersName[3], ' le ', playersName[2], ' lai ', next_amt3, ' dinu parcha.')
            else:
                next_amt3 = abs(CtoD - DtoC)
                print( playersName[2], ' le ', playersName[3], ' lai ', next_amt3, ' dinu parcha.')

        elif DtoC>= CtoD and BtoC>= CtoB:
            next_amt1 = abs(DtoC - CtoD)
            next_amt2 = abs(BtoC - CtoB)
            print( playersName[3], ' le ', playersName[2], ' lai ', next_amt1, ' dinu parcha.')
            print( playersName[1], ' le ', playersName[2], ' lai ', next_amt2, ' dinu parcha.')
            if DtoB>= BtoD:
                next_amt3 = abs(DtoB - BtoD)
                print( playersName[3], ' le ', playersName[1], ' lai ', next_amt3, ' dinu parcha.')
            else:
                next_amt3 = abs(BtoD - DtoB)
                print( playersName[1], ' le ', playersName[3], ' lai ', next_amt3, ' dinu parcha.')
       
        elif BtoD>= DtoB and CtoD>= DtoC:
            next_amt1 = abs(BtoD - DtoB)
            next_amt2 = abs(CtoD - DtoC)
            print( playersName[1], ' le ', playersName[3], ' lai ', next_amt1, ' dinu parcha.')
            print( playersName[2], ' le ', playersName[3], ' lai ', next_amt2, ' dinu parcha.')
            if CtoB>= BtoC:
                next_amt3 = abs(CtoB - BtoC)
                print( playersName[2], ' le ', playersName[1], ' lai ', next_amt3, ' dinu parcha.')
            else:
                next_amt3 = abs(BtoC - CtoB)
                print( playersName[1], ' le ', playersName[2], ' lai ', next_amt3, ' dinu parcha.')


# 0, 2, 3
    elif AtoB>= BtoA and CtoB>= BtoC and DtoB>= BtoD:
        amount = abs(AtoB - BtoA)
        amount1 = abs(CtoB - BtoC)
        amount2 = abs(DtoB - BtoD)
        print( playersName[0], ' le ', playersName[1], ' lai ', amount, ' dinu parcha.')
        print( playersName[2], ' le ', playersName[1], ' lai ', amount1, ' dinu parcha.')
        print( playersName[3], ' le ', playersName[1], ' lai ', amount2, ' dinu parcha.')

        if CtoA>= AtoC and DtoA>= AtoD:
            next_amt1 = abs(CtoA - AtoC)
            next_amt2 = abs(DtoA - AtoD)
            print( playersName[2], ' le ', playersName[0], ' lai ', next_amt1, ' dinu parcha.')
            print( playersName[3], ' le ', playersName[0], ' lai ', next_amt2, ' dinu parcha.')

            if DtoC>= CtoD:
                next_amt3 = abs(DtoC - CtoD)
                print( playersName[3], ' le ', playersName[2], ' lai ', next_amt3, ' dinu parcha.')
            else:
                next_amt3 = abs(CtoD - DtoC)
                print( playersName[2], ' le ', playersName[3], ' lai ', next_amt3, ' dinu parcha.')
            
        elif AtoC>= CtoA and DtoC>= CtoD:
            next_amt1 = abs(AtoC - CtoA)
            next_amt2 = abs(DtoC - CtoD)
            print( playersName[0], ' le ', playersName[2], ' lai ', next_amt1, ' dinu parcha.')
            print( playersName[3], ' le ', playersName[2], ' lai ', next_amt2, ' dinu parcha.')

            
            if DtoA>= AtoD:
                next_amt3 = abs(DtoA - AtoD)
                print( playersName[3], ' le ', playersName[0], ' lai ', next_amt3, ' dinu parcha.')
            else:
                next_amt3 = abs(AtoD - DtoA)
                print( playersName[0], ' le ', playersName[3], ' lai ', next_amt3, ' dinu parcha.')

        elif AtoD>= DtoA and CtoD>= DtoC:
            next_amt1 = abs(AtoD- DtoA)
            next_amt2 = abs(CtoD - DtoC)
            print( playersName[0], ' le ', playersName[3], ' lai ', next_amt1, ' dinu parcha.')
            print( playersName[2], ' le ', playersName[3], ' lai ', next_amt2, ' dinu parcha.')

            
            if CtoA>= AtoC:
                next_amt3 = abs(CtoA - AtoC)
                print( playersName[2], ' le ', playersName[0], ' lai ', next_amt3, ' dinu parcha.')
            else:
                next_amt3 = abs(AtoD - DtoA)
                print( playersName[0], ' le ', playersName[2], ' lai ', next_amt3, ' dinu parcha.')

# 0, 1, 3
    elif AtoC>= CtoA and BtoC>= CtoB and DtoC>=CtoD:
        amount = abs(AtoC - CtoA)
        amount1 = abs(BtoC - CtoB)
        amount2 = abs(DtoC - CtoD)
        print( playersName[0], ' le ', playersName[2], ' lai ', amount, ' dinu parcha.')
        print( playersName[1], ' le ', playersName[2], ' lai ', amount1, ' dinu parcha.')
        print( playersName[3], ' le ', playersName[2], ' lai ', amount2, ' dinu parcha.')

        if BtoA>= AtoB and DtoA>= AtoD:
            next_amt1 = abs(BtoA - AtoB)
            next_amt2 = abs(DtoA - AtoD)
            print( playersName[1], ' le ', playersName[0], ' lai ', next_amt1, ' dinu parcha.')
            print( playersName[3], ' le ', playersName[0], ' lai ', next_amt2, ' dinu parcha.')

            if DtoB>= BtoD:
                next_amt3 = abs(DtoB - BtoD)
                print( playersName[3], ' le ', playersName[1], ' lai ', next_amt3, ' dinu parcha.')
            else:
                next_amt3 = abs(BtoD - DtoB)
                print( playersName[1], ' le ', playersName[3], ' lai ', next_amt3, ' dinu parcha.')

        elif AtoB>= BtoA and DtoB>= BtoD:
            next_amt1 = abs(AtoB - BtoA)
            next_amt2 = abs(DtoB - BtoD)
            print( playersName[0], ' le ', playersName[1], ' lai ', next_amt1, ' dinu parcha.')
            print( playersName[3], ' le ', playersName[1], ' lai ', next_amt2, ' dinu parcha.')

            if DtoA>= AtoD:
                next_amt3 = abs(DtoA - AtoD)
                print( playersName[3], ' le ', playersName[0], ' lai ', next_amt3, ' dinu parcha.')
            else:
                next_amt3 = abs(AtoD - DtoA)
                print( playersName[0], ' le ', playersName[3], ' lai ', next_amt3, ' dinu parcha.')
       
        elif AtoD>= DtoA and BtoD>= DtoB:
            next_amt1 = abs(AtoD- DtoA)
            next_amt2 = abs(BtoD - DtoB)
            print( playersName[0], ' le ', playersName[3], ' lai ', next_amt1, ' dinu parcha.')
            print( playersName[1], ' le ', playersName[3], ' lai ', next_amt2, ' dinu parcha.')

            if BtoA>= AtoB:
                next_amt3 = abs(BtoA - AtoB)
                print( playersName[1], ' le ', playersName[0], ' lai ', next_amt3, ' dinu parcha.')
            else:
                next_amt3 = abs(AtoB - BtoA)
                print( playersName[0], ' le ', playersName[1], ' lai ', next_amt3, ' dinu parcha.')
#0, 1, 2
    elif AtoD>= DtoA and BtoD>= DtoB and CtoD>= DtoC:
        amount = abs(AtoD - DtoA)
        amount1 = abs(BtoD - DtoB)
        amount2 = abs(CtoD - DtoC)
        print( playersName[0], ' le ', playersName[3], ' lai ', amount, ' dinu parcha.')
        print( playersName[1], ' le ', playersName[3], ' lai ', amount1, ' dinu parcha.')
        print( playersName[2], ' le ', playersName[3], ' lai ', amount2, ' dinu parcha.')

        if BtoA>= AtoB and CtoA>= AtoC:
            next_amt1 = abs(BtoA - AtoB)
            next_amt2 = abs(CtoA - AtoC)
            print( playersName[1], ' le ', playersName[0], ' lai ', next_amt1, ' dinu parcha.')
            print( playersName[2], ' le ', playersName[0], ' lai ', next_amt2, ' dinu parcha.')

            if CtoB>= BtoC:
                next_amt3 = abs(CtoB - BtoC)
                print( playersName[2], ' le ', playersName[1], ' lai ', next_amt3, ' dinu parcha.')
            else:
                next_amt3 = abs(BtoC - CtoB)
                print( playersName[1], ' le ', playersName[2], ' lai ', next_amt3, ' dinu parcha.')

        elif AtoB>= BtoA and CtoB>= BtoC:
            next_amt1 = abs(AtoB - BtoA)
            next_amt2 = abs(CtoB - BtoC)
            print( playersName[0], ' le ', playersName[1], ' lai ', next_amt1, ' dinu parcha.')
            print( playersName[2], ' le ', playersName[1], ' lai ', next_amt2, ' dinu parcha.')

            if CtoA>= AtoC:
                next_amt3 = abs(CtoA - AtoC)
                print( playersName[2], ' le ', playersName[0], ' lai ', next_amt3, ' dinu parcha.')
            else:
                next_amt3 = abs(AtoC - CtoA)
                print( playersName[0], ' le ', playersName[2], ' lai ', next_amt3, ' dinu parcha.')

        elif AtoC>= CtoA and BtoC>= CtoB:
            next_amt1 = abs(AtoC- CtoA)
            next_amt2 = abs(BtoC - CtoB)
            print( playersName[0], ' le ', playersName[2], ' lai ', next_amt1, ' dinu parcha.')
            print( playersName[1], ' le ', playersName[2], ' lai ', next_amt2, ' dinu parcha.')

            if BtoA>= AtoB:
                next_amt3 = abs(BtoA - AtoB)
                print( playersName[1], ' le ', playersName[0], ' lai ', next_amt3, ' dinu parcha.')
            else:
                next_amt3 = abs(AtoB - BtoA)
                print( playersName[0], ' le ', playersName[1], ' lai ', next_amt3, ' dinu parcha.')

    

