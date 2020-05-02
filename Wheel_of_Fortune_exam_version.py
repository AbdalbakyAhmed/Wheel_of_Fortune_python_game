VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self,name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
        
    def addMoney(self,amt):
        self.prizeMoney = self.prizeMoney + amt
    
    def goBankrupt(self):
        self.prizeMoney = 0
    
    def addPrize(self,prize):
        self.prizes.append(prize)
    
    def __str__(self):
        return "{} (${})".format(self.name,self.prizeMoney)
        
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def __init__(self,name):
        WOFPlayer.__init__(self,name)
    
    def getMove(category, obscuredPhrase, guessed):
        text = """
{} has ${}

Category: {}
Phrase:  {}
Guessed: {}

Guess a letter, phrase, or type 'exit' or 'pass': """.format(self.name, self.prizeMoney ,category,obscuredPhrase,guessed)
        print(str(input(text)))

# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    #SORTED_FREQUENCIES = [letter for letter in 'ZQXJKVBPYGFWMUCLDRHSNIOATE']
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    def __init__(self,name,difficulty):
        self.name = name
        self.difficulty = difficulty
        self.prizeMoney = 0
        self.prizes = []
    
    def smartCoinFlip(self):
        val = random.randint(1, 10)
        if val > self.difficulty:
            return True
        else:
            return False
    
    def getPossibleLetters(self, guessed):
        list_Letters = list()
        if self.prizeMoney >= 250:
            for i in LETTERS:
                list_Letters.append(i)
        else:
            for i in LETTERS:
                if i not in VOWELS:
                    list_Letters.append(i)
        return list_Letters

    def getMove(self,category, obscuredPhrase, guessed):
        list_letters = self.getPossibleLetters(guessed)
        flip = self.smartCoinFlip()
        
        if len(list_letters) == 0:
            return 'pass'
        else:
            if flip == True:
                for i in self.SORTED_FREQUENCIES:
                    if i in list_letters:
                        return 1
            elif flip == False:
                return random.choice(list_letters)
