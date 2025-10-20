def Word_Frequency(Link, Unique_Word):
    Word_Count = {}
    Words_Appearing_Only_Once = 0
    Unique_Word_Count = 0
    Word_Length = 0
    
    with open(Link, "r", encoding="utf-8") as Book:

        for Line in Book:
            Words = Line.split()

            for Word in Words:
                Word = Word.lower()
                Unique_Word = Unique_Word.lower()

                if Word == Unique_Word:
                    Unique_Word_Count += 1

                if Word in Word_Count:
                    Word_Count[Word] += 1
                    
                else:
                    Word_Count[Word] = 1
                    Word_Length += len(Word)
                    Words_Appearing_Only_Once += 1

    Word_Count = sorted(Word_Count.items(), key=lambda x: x[1], reverse=True) #items gör de till en turple, key - x[1] sorterar det i storleks ordning, rev vänder de baklänges
    Word_Count = Word_Count[:10]

    Word_Length_Distribution = Word_Length / Words_Appearing_Only_Once
    Word_Length_Distribution = round(Word_Length_Distribution, 2)

    return Word_Count, Words_Appearing_Only_Once, Unique_Word_Count, Word_Length_Distribution


def Character_Analysis(Link):
    Letter_Frequency_Distribution = {}
    Punctuation_Statistics = {}
    Small_Letter = 0
    Big_Letter = 0
    
    with open(Link, "r", encoding="utf-8") as Book:

        for Line in Book:

            for Letter in Line:

                if 'a' <= Letter <= 'z':
                    Small_Letter += 1
                    
                elif 'A' <= Letter <= 'Z':
                    Big_Letter += 1
                    
                Letter = Letter.lower()

                if 'a' <= Letter <= 'z':
                    if Letter in Letter_Frequency_Distribution:
                        Letter_Frequency_Distribution[Letter] += 1
                        
                    else:
                        Letter_Frequency_Distribution[Letter] = 1
                        
                else:
                    if Letter in Punctuation_Statistics:
                        Punctuation_Statistics[Letter] += 1
                        
                    else:
                        Punctuation_Statistics[Letter] = 1
                    

    Letter_Frequency_Distribution = sorted(Letter_Frequency_Distribution.items(), key=lambda x: x[1], reverse=True)
    Letter_Frequency_Distribution = Letter_Frequency_Distribution[:10]

    Punctuation_Statistics = sorted(Punctuation_Statistics.items(), key=lambda x: x[1], reverse=True)
    Space = Punctuation_Statistics[:1]
    Punctuation_Statistics = Punctuation_Statistics[2:8]

    return(Letter_Frequency_Distribution, Punctuation_Statistics, Small_Letter, Big_Letter, Space)

    