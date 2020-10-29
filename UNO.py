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
        else:
            print('Invalid player, Psycho!!')
        if winnerName == playersName[0]:
            BtoA = BtoA + u
        else:
            AtoB = AtoB + u
    if BtoA >= AtoB:
        amount = abs(BtoA - AtoB)
        print( playersName[1], " le ", playersName[0], " lai Rs.",amount, " dinu parcha.")
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
        else:
            print('Invalid player, Psycho!!')
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
    elif AtoB>= BtoA and CtoB>= BtoC:
        amount = abs(AtoB - BtoC)
        amount1 = abs(CtoB - BtoC)
        print( playersName[0], ' le ', playersName[1], ' lai ', amount, ' dinu parcha.')
        print( playersName[2], ' le ', playersName[1], ' lai ', amount1, ' dinu parcha.')
    elif AtoC>= CtoA and BtoC>= CtoB:
        amount = abs(AtoC - CtoA)
        amount1 = abs(BtoC - CtoB)
        print( playersName[0], ' le ', playersName[2], ' lai ', amount, ' dinu parcha.')
        print( playersName[1], ' le ', playersName[2], ' lai ', amount1, ' dinu parcha.')

    
elif totalPlayers == 4:
    while True:
        winnerName = str.lower(input('Who is the winner of this round? : '))
        if winnerName == 'done':
            break
        elif winnerName in playersName:
            winners.append(winnerName)
        else:
            print('Invalid player, Psycho!!')
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
        else:
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
    elif AtoB>= BtoA and CtoB>= BtoC and DtoB>= BtoD:
        amount = abs(AtoB - BtoA)
        amount1 = abs(CtoB - BtoC)
        amount2 = abs(DtoB - BtoD)
        print( playersName[0], ' le ', playersName[1], ' lai ', amount, ' dinu parcha.')
        print( playersName[2], ' le ', playersName[1], ' lai ', amount1, ' dinu parcha.')
        print( playersName[3], ' le ', playersName[1], ' lai ', amount2, ' dinu parcha.')
    elif AtoC>= CtoA and BtoC>= CtoB and DtoC>=CtoD:
        amount = abs(AtoC - CtoA)
        amount1 = abs(BtoC - CtoB)
        amount2 = abs(DtoC - CtoD)
        print( playersName[1], ' le ', playersName[0], ' lai ', amount, ' dinu parcha.')
        print( playersName[2], ' le ', playersName[0], ' lai ', amount1, ' dinu parcha.')
        print( playersName[3], ' le ', playersName[0], ' lai ', amount2, ' dinu parcha.')
    elif AtoD>= DtoA and BtoD>= DtoB and CtoD>= DtoC:
        amount = abs(AtoD - DtoA)
        amount1 = abs(BtoD - DtoB)
        amount2 = abs(CtoD - DtoC)
        print( playersName[0], ' le ', playersName[3], ' lai ', amount, ' dinu parcha.')
        print( playersName[1], ' le ', playersName[3], ' lai ', amount1, ' dinu parcha.')
        print( playersName[2], ' le ', playersName[3], ' lai ', amount2, ' dinu parcha.')



   
else:
    print("Invalid number of player.")

