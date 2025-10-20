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
                print(f'{'Sentence Analysis':^50}')
                print(f'{'Character Analysis':^50}')
                print(f'{'Export results':^50}')

      
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
                    
                    Word_Analysis_Result = Function.Word_Frequency(Link, Word)

                    print(f'Word Analysis for {Link}')
                    print(Top_Line)

                    print(f'{Word} appears {Word_Analysis_Result[2]} in the text')
                    print(f'Words appering only once: {Word_Analysis_Result[1]}')
                    print(f'Average word length: {Word_Analysis_Result[3]} characters')
                    print()

                    print(f'Top 10 most common worlds:')
                    for Word, Count in Word_Analysis_Result[0]:
                        print(f'{Word: <10} {Count}')
                        
                    print(Bottom_Line)
                    print()

                elif Choice == 'Sentenceanalysis':
                    print('Sentence Analysis')
                     
                elif Choice == 'Characteranalysis':
                    print()

                    Character_Analysis_Result = Function.Character_Analysis(Link)

                    print(f'Character Analysis for {Link}')
                    print(Top_Line)

                    print(f'Punctuation statistics (Top 5):')
                    for Punctuation, Count in Character_Analysis_Result[1]:
                        print(f'{Punctuation: <10} {Count}')
                        
                    print()
                    
                    print(f'Small letters: {Character_Analysis_Result[2]}')
                    print(f'Big letters: {Character_Analysis_Result[3]}')
                    print(f'Spaces: {Character_Analysis_Result[4]}')
                    
                    print()

                    print(f'Top 10 most common letters:')
                    for Letter, Count in Character_Analysis_Result[0]:
                        print(f'{Letter: <10} {Count}')
                        
                    print(Bottom_Line)
                    print()
                    
                elif Choice == 'Exportresults':
                    print('Exporting result...')

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