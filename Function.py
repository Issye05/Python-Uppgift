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



    Word_Count = sorted(Word_Count.items(), key=lambda x: x[1], reverse=True)
    Word_Count = Word_Count[:10]

    Word_Length_Distribution = Word_Length / Words_Appearing_Only_Once
    Word_Length_Distribution = round(Word_Length_Distribution, 2)

    return Word_Count, Words_Appearing_Only_Once, Unique_Word_Count, Word_Length_Distribution