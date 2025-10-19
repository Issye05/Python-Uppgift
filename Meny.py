import Function

def Meny():
    Top_Line = '\u2554' + '\u2550' * 25 + '\u2557'
    Bottom_Line = '\u255A' + '\u2550' * 25 + '\u255D'
    Vertical_Line = '\u2551'
    Choice = ''

    Books = {'Gostaberlingssaga': 'GostaBerlingsSaga.txt',
             'Jakobbocken': 'länk2',
             'Isakavnjutare': 'länk3',
    }
                
    while Choice != 'Exit':
        
        print(f'{'Choose a book':^25}')
        print(Top_Line)

        for Name in Books:
            print(f'{Name:^25}')
            
        print(f'{'Exit':^25}')
        print(Bottom_Line)
        print()
        
        Choice = input('==>>')
        Choice = Choice.capitalize().strip().replace(' ','')


        if Choice in Books:
            print()
            
            Link = Books[Choice]
            
            while Choice != 'Back':
                print(f'{'Type what chooise you want':^25}')
                print(Top_Line)
                
                print(f'{'Basic Statistics':^25}')
                print(f'{'Word Analysis':^25}')
                print(f'{'Character nalysis':^25}')
      
                print(f'{'Back':^25}')
                print(Bottom_Line)
                print()
                
                Choice = input('==>>')
                Choice = Choice.capitalize().strip().replace(' ','')

                if Choice == 'Basicstatistic':
                    print('Gör en funktion till varje')
                    
                    print()
                elif Choice == 'Wordanalysis':
                    print()
                    print(f'Type the word you want to search for in the text:')
                    Word = input('==>>')
                    print()
                    
                    Result = Function.Word_Frequency(Link, Word)

                    print(f'Word Analysis for {Link}')

                    print(f'{Word} appears {Result[2]} in the text')
                    print(f'Words appering only once: {Result[1]}')
                    print()

                    print(f'Top 10 most common worlds:')
                    for Word, Count in Result[0]:
                        print(f'{Word: <10} {Count}')
                    
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