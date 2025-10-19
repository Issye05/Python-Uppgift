def Meny():
    Line = '\u2550' * 18
    CornerTopLeft = '\u2554'
    CornerTopRight = '\u2557'
    CornerBottomLeft = '\u255A'
    CornerBottomRight = '\u255D'
    Line2 = '\u2551'
    
    Choice = ''

    Books = {'Lejonkungen': 'länk',
             'Jakobbocken': 'länk2',
             'Isakavnjutare': 'länk3',
    }
                
    while Choice != 'exit':
        print(f'{'Choose a book':^20}')
        print(CornerTopLeft + Line + CornerTopRight)

        for i in Books:
            print(f'{i:^20}')
            
        print(f'{'Exit':^20}')
        print(CornerBottomLeft + Line + CornerBottomRight)
        print()
        
        Choice = input('==>>')
        Choice = Choice.capitalize().strip().replace(' ','')


        if Choice in Books:
            print()
            #import {Books [Choice]} eller en funtion typ
            
            while Choice != 'back':
                print(f'{'Type what chooise you want':^20}')
                print(CornerTopLeft + Line + CornerTopRight)
                
                print(f'{'Basic tatistic':^20}')
                print(f'{'Word requency':^20}')
                print(f'{'Character nalysis':^20}')
      
                print(f'{'Back':^20}')
                print(CornerBottomLeft + Line + CornerBottomRight)
                print()
                
                Choice = input('==>>')
                Choice = Choice.lower().strip().replace(' ','')

                if Choice == 'basicstatistic':
                    print('Gör en funktion till varje')
                    print()
                elif Choice == 'wordfrequency':
                    print('Gör en funktion till varje')
                    print()
                elif Choice == 'characteranalysis':
                    print('Gör en funktion till varje')
                    print()
                elif Choice == 'back':
                    print()
                else:
                    print('Didnt find your choice')
                    print()
                
        elif Choice == 'exit':
            print('Exit program') 
            print()
        else:
            print('Error, Try again')
            print()
