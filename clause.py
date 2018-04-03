'''
Clause
    Is one clause with literals and an ID
'''
class Clause():
    def __init__(self, clauseText, lineNumber):
        self.literals = []
        self.id = lineNumber
        self.parseText(clauseText)

    '''
    Parses clause text into an internal list
    '''
    def parseText(self, clauseText):
        self.literals = clauseText.split()
