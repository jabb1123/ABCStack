from BJ_Base import *

word_mark = "|"
letter_mark = "*"
ditdah_mark = ","

import International_Morse_Code as Morse
MorseCode = dict(Morse.Code)

MorseCode[word_mark] = word_mark
MorseCode[letter_mark] = letter_mark
MorseCode[ditdah_mark] = ditdah_mark


msg2words = BJ_Layer(
    fn=lambda msg:(word+word_mark for word in msg.upper().split(" ") if len(word)),
    fn_inv = lambda words:" ".join([word[:-1] for word in words]))

word2letters = BJ_Layer(
    fn = lambda word: (letter+letter_mark for letter in word),
    fn_inv = lambda letters: "".join([letter[:-1] for letter in letters]))

letter2dotsanddashes = BJ_Dict(MorseCode)

dotordashormark2pulse = BJ_Dict(
    {".":(1,1),
     "-":(1,3),
     ditdah_mark:(0,1),
     letter_mark:(0,2),
     word_mark:(0,4)
     }
    )

if __name__ == "__main__":
    MorseCodeStack = BJ_Stack((
        msg2words,
        word2letters,
        letter2dotsanddashes,
        dotordashormark2pulse
        ))
    
    


    



