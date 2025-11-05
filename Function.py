import matplotlib.pyplot as plt

#--->

def Word_analysis(Link, Unique_word):
    Word_count = {}
    Word_length = []
    Words_appearing_only_once = set()
    Unique_word_count = 0
    
    Unique_word = Unique_word.lower()
    
    with open(Link, "r", encoding="utf-8") as Book:

        for Line in Book:
            Words = Line.split()

            for Word in Words:
                Word = Word.lower()

                Words_appearing_only_once.add(Word)

                Word_length.append(len(Word))

                if Word == Unique_word:
                    Unique_word_count += 1

                if Word in Word_count:
                    Word_count[Word] += 1
                    
                else:
                    Word_count[Word] = 1

    Word_count = sorted(Word_count.items(), key = lambda x: x[1], reverse = True) #items gör de till en turple, key - x[1] sorterar det i storleks ordning, rev vänder de baklänges
    Word_count = Word_count[:10]

    Words_appearing_only_once = len(Words_appearing_only_once)

    Word_length.sort()
    

    return Word_count, Word_length, Words_appearing_only_once, Unique_word_count

def Visualisations_word(Link):

    Result = Word_analysis(Link, '')
        
    x, y = zip(*Result[0])

    plt.bar(x, y, color='turquoise') #bar: fast data som i en dic
    plt.title('Top 10 most common worlds')
    plt.xlabel('Word')
    plt.ylabel('Count')
    plt.show()

    
    plt.hist(Result[1], bins=range(1, max(Result[1]) + 1), color='red') #hist: rådata, bins: delar upp datan i ''fack'' från 1 till max längd
    plt.title("Word Length Distribution")
    plt.xlabel("Word Length (characters)")
    plt.ylabel("Frequency")
    plt.show()

#--->

def Character_analysis(Link):
    Letter_count = {}
    Character_type = {'Lowercase': 0, 'Uppercase': 0, 'Digits': 0, 'Spaces': 0, 'Punctuation': 0, 'Rest': 0,}

    with open(Link, "r", encoding="utf-8") as Book:

        for Line in Book:

            for Letter in Line:

                if 'a' <= Letter <= 'z':
                    Character_type['Lowercase'] += 1
                    
                elif 'A' <= Letter <= 'Z':
                    Character_type['Uppercase'] += 1

                elif '0' <= Letter <= '9':
                    Character_type['Digits'] += 1

                elif Letter == ' ':
                    Character_type['Spaces'] += 1

                elif Letter == '.':
                    Character_type['Punctuation'] += 1

                else:
                    Character_type['Rest'] += 1

                Letter = Letter.lower()
                
                if Letter.isalpha():
                    if Letter in Letter_count:
                        Letter_count[Letter] += 1
                
                    else:
                        Letter_count[Letter] = 1

                    
    Letter_count = sorted(Letter_count.items(), key = lambda x: x[1], reverse = True)
    Letter_count = Letter_count[:10]

    return Letter_count, Character_type

def Visualisations_character(Link):

    Result = Character_analysis(Link)
        
    x, y = zip(*Result[0])

    plt.bar(x, y, color='orange')
    plt.title('Top 10 most common letters')
    plt.xlabel('Letter')
    plt.ylabel('Count')
    plt.show()

    Pie_colors = ['steelblue', 'darkorange', 'crimson', 'mediumseagreen', 'mediumpurple', 'goldenrod']          

    plt.pie(Result[1].values(), labels = Result[1].keys(), colors = Pie_colors) #Keys blir namnen och values blir hur stor varje del är
    plt.title('Character type distribution')
    plt.show()

#--->

def Basic_statistics(Link):

    Link = open(Link, 'r')
    Counters = {'Words' : 0,
                'Lines' : 0,
                'Characters' : 0,
                'Characters_all' : 0,
                'Sentences' : 0,
                'A_w_p_l' : 0,
                'A_c_p_w' : 0,
                'A_w_p_s' : 0}
    
    for Line in Link:
        Counters['Characters_all'] += len(Line)
        for Letter in Line:
            if Letter != ' ':
                Counters['Characters'] += 1
            if Letter in '.!?':
                Counters['Sentences'] += 1        
        Line = Line.split()
        Counters['Lines'] += 1
        
        for Word in Line:
            Counters['Words'] += 1

    
    Counters['A_w_p_l'] =  round(Counters['Words'] / Counters['Lines'], 2)
    Counters['A_c_p_w'] = round(Counters['Characters'] / Counters['Words'], 2)
    Counters['A_w_p_s'] = round(Counters['Words'] / Counters['Sentences'], 2)
    

    Link.close()
    
    return Counters

#--->


    