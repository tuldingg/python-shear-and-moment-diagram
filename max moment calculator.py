#Maximum Moment Calculator

beamQuantity = 0

while True:
    beamQuantity += 1
    beamLength = []
    print(f'Specify Length for Beam No. {beamQuantity} (meters) (type n if done adding): ')
    userInput1 = input('> ')

    if userInput1 == 'n':
        break
    elif userInput1 != int or userInput1 != float:
        print('Please input a valid value')
       
    