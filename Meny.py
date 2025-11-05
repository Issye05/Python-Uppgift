import importlib
import Function

importlib.reload(Function)

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
        Choice = Choice.strip().title()


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
                print(f'{'Export Result':^50}')

      
                print(f'{'Back':^50}')
                print(Bottom_Line)
                print()
                
                Choice = input('==>>')
                Choice = Choice.strip().capitalize().replace(' ','')

                if Choice == 'Basicstatistics':

                    Result = Function.Basic_statistics(Link)
                    
                    print()
                    print(f'Basic Statistics for {Link}')
                    print(Top_Line)
  
                    for Word, Count in Result.items():
                        print(f'{Word: <10} {Count}')
                    
                    print(Bottom_Line)
                    print()

                    Function.Visualisations_statistics(Link)
                    
                elif Choice == 'Wordanalysis':
                    
                    print()
                    print(f'Type the word you want to search for in the text:')
                    Word = input('==>>')
                    print()
                    
                    Result = Function.Word_analysis(Link, Word)

                    Avrage = sum(Result[1]) / len(Result[1])
                    Avrage = round(Avrage, 1)

                    print(f'Word Analysis for {Link}')
                    print(Top_Line)

                    print(f'Shortest word: {min(Result[1])}')
                    print(f'Longest word: {max(Result[1])}')
                    print(f'Avrage lenght: {Avrage}')
                    print(f'Words appering only once: {Result[2]}')
                    print(f'Your word: {Word} appered {Result[3]} times in the text')
                    print()

                    print(f'Top 10 most common worlds:')
                    for Word, Count in Result[0]:
                        print(f'{Word: <10} {Count}')
                        
                    print(Bottom_Line)
                    print()

                    Function.Visualisations_word(Link)

                elif Choice == 'Sentenceanalysis':

                    Result = Function.Sentence_analysis(Link)
                
                    print()
                    print(f'Sentence Analysis for {Link}')
                    print(Top_Line)
                    
                    print(f'Longest sentance is {max(Result[0])} words:')
                    print('" ', end='')
                    for Word in Result[1][:30]:
                        print(Word, end=' ')
                    print('.."')
                    print()
                    
                    print(f'Shortest sentance is {min(Result[0])} word(s):')
                    print('" ', end='')
                    for Word in Result[2]:
                        print(Word, end=' ')
                    print('"')
                    print()
                    
                    print(f'Sentence length distribution (top 5):', sep='')
                    for Word, Count in Result[3]:
                        print(f'{Word} words: {Count: >10} sentences')

                    print(Bottom_Line)
                    print()

                    Function.Sentence_visualisation(Link)
                     
                elif Choice == 'Characteranalysis':
                    print()

                    Result = Function.Character_analysis(Link)

                    print(f'Character Analysis for {Link}')
                    print(Top_Line)

                    print(f'Top 5 most common letters:')
                    for Letter, Count in Result[0]:
                        print(f'{Letter: <10} {Count}')

                    print()

                    print(Result[1])

                    print(f'Character type:')
                    for Character, Count in Result[1].items():
                        print(f'{Character: <10} {Count}')
                        
                    print(Bottom_Line)
                    print()

                    Function.Visualisations_character(Link)
                    
                elif Choice == 'Exportresult':
                    print()
                    print('Exporting result...')

                    Function.Export(Link)
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