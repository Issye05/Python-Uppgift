import Function

def Meny():
    Top_Line = '\u2554' + '\u2550' * 50 + '\u2557'
    Bottom_Line = '\u255A' + '\u2550' * 50 + '\u255D'
    Choice = ''

    Books = {'Pride And Prejudice': 'Pride And Prejudice.txt',
             'The Complete Works Of William Shakespeare': 'The Complete Works Of William Shakespeare.txt',
             'Dracula': 'Dracula.txt',
             'Alices Adventures In Wonderland': 'Alices Adventures In Wonderland.txt',
             'Adventures Of Sherlock Holmes': 'Adventures Of Sherlock Holmes.txt',
    }
                
    while Choice != 'Exit':
        
        print(f'{'Choose a book':^50}')
        print(Top_Line)

        for Name in Books:
            print(f'{Name:^50}')
            
        print(f'{'Exit':^50}')
        print(Bottom_Line)
        print()
        
        Choice = input('==>>')
        Choice = Choice.title().strip()


        if Choice in Books:
            print()
            
            Link = Books[Choice]
            
            while Choice != 'Back':
                print(f'{'Type what chooise you want':^50}')
                print(Top_Line)
                
                print(f'{'Basic Statistics':^50}')
                print(f'{'Word Analysis':^50}')
                print(f'{'Character Analysis':^50}')
      
                print(f'{'Back':^50}')
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
                    print(Top_Line)

                    print(f'{Word} appears {Result[2]} in the text')
                    print(f'Words appering only once: {Result[1]}')
                    print()

                    print(f'Top 10 most common worlds:')
                    for Word, Count in Result[0]:
                        print(f'{Word: <10} {Count}')
                        
                    print(Bottom_Line)
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