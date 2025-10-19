import Function

def Meny():
    Line = '\u2550' * 18
    CornerTopLeft = '\u2554'
    CornerTopRight = '\u2557'
    CornerBottomLeft = '\u255A'
    CornerBottomRight = '\u255D'
    Line2 = '\u2551'
    
    Choice = ''

    Books = {'Gostaberlingssaga': 'GostaBerlingsSaga.txt',
             'Jakobbocken': 'länk2',
             'Isakavnjutare': 'länk3',
    }
                
    while Choice != 'Exit':
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
            
            Link = Books[Choice]
            
            while Choice != 'Back':
                print(f'{'Type what chooise you want':^20}')
                print(CornerTopLeft + Line + CornerTopRight)
                
                print(f'{'Basic Statistics':^20}')
                print(f'{'Word Analysis':^20}')
                print(f'{'Character nalysis':^20}')
      
                print(f'{'Back':^20}')
                print(CornerBottomLeft + Line + CornerBottomRight)
                print()
                
                Choice = input('==>>')
                Choice = Choice.capitalize().strip().replace(' ','')

                if Choice == 'Basicstatistic':
                    print('Gör en funktion till varje')
                    print()
                elif Choice == 'Wordanalysis':
                    Word = input(f'Type the word you want to search for in the text.')
                    
                    Result = Function.Word_Frequency(Link, Word)

                    print(f'Word appering only once: {Result[1]}')
                    print(f'{Word} was: {Result[2]} times')

                    for Word, Count in Result[0]:
                        print(f'{Word: >5} {Count}')
                    
                    
                    print()
                elif Choice == 'Characteranalysis':
                    print('Gör en funktion till varje')
                    print()
                elif Choice == 'Back':
                    print()
                else:
                    print('Didnt find your choice')
                    print()
                
        elif Choice == 'Exit':
            print('Exit program') 
            print()
        else:
            print('Error, Try again')
            print()
Meny()