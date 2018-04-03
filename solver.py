from clause import Clause
import itertools

'''
Solver
    Solves the KB to find whether it can be resolved or not
'''
class Solver:
    def __init__(self):
        self.clauses = []
        self.resolvedClauses = []

    '''
    Add clause from text file KB into Solver
    '''
    def addClause(self, clauseText):
        self.clauses.append(Clause(clauseText, len(self.clauses) + 1))

    '''
    Are the two clauses resolvable?
    '''
    def isResolvable(self, clause1, clause2):

        # Don't continue if the clauses have been resolved already
        if set([clause1, clause2]) in self.resolvedClauses:
            return False

        matchingClauses = False;

        # Get union of clauses to remove duplicates
        resultList = list(set(clause1.literals) | set(clause2.literals))
        matched = []

        # Determine if the clause is resolvable
        for literal in resultList:

            # Ignore if the literal has already been matched to another
            if set(['~' + literal, literal]) in matched or set([literal, literal[1:]]) in matched:
                continue

            # Search matches on ~ literals
            if '~' in literal and literal[1:] in resultList:
                matched.append(set([literal, literal[1:]]))
                if matchingClauses:
                    return False
                else:
                    matchingClauses = True

            # Search matches on true literals
            elif '~' + literal in resultList:
                matched.append(set(['~' + literal, literal]))
                if matchingClauses:
                    return False
                else:
                    matchingClauses = True

        # If there is a literal to resolve, test if the new clause is already in the KB
        if matchingClauses:
            newClauseLiterals = self.getResolution(clause1, clause2)
            for c in self.clauses:
                if newClauseLiterals == c.literals:
                    return False
            return True
        else:
            return False

    '''
    Run the solver
    '''
    def solve(self):

        # Print the KB as is
        for c in self.clauses:
            self.printLine(c.id, ' '.join(c.literals), False)

        # Keep resolving until a solution is found or there are no more clauses to resolve
        resolvedRound = True
        empty = False
        while resolvedRound and not empty:

            # Heuristic: attempt to resolve shorter clauses first
            self.clauses.sort(key = lambda x: len(x.literals))
            resolvedRound = False

            # Search resolution for each combination of clauses
            for c1, c2 in itertools.combinations(self.clauses, 2):
                if self.isResolvable(c1, c2):
                    empty = self.resolve(c1, c2)
                    if empty:
                        break
                    resolvedRound = True
        if empty:
            print 'Size of final clause set: ' + str(len(self.clauses))
        else:
            print 'Cannot be resolved'

    '''
    Resolve the two clauses
    '''
    def resolve(self, clause1, clause2):

        # Store that these two clauses have been resolved
        self.resolvedClauses.append(set([clause1, clause2]));

        # Get the resolution of the two clauses
        newClauseLiterals = self.getResolution(clause1, clause2)

        # Create a new Clause object
        newClause = Clause(' '.join(newClauseLiterals), len(self.clauses) + 1)
        self.clauses.append(newClause)

        printedClause = ' '.join(newClauseLiterals) if  len(newClause.literals) > 0 else 'False';

        # Print the resolution info
        self.printLine(newClause.id, printedClause, True, clause1.id, clause2.id)

        return len(newClause.literals) == 0

    '''
    Get the result of two clauses resolving
    '''
    def getResolution(self, clause1, clause2):
        newClauseLiterals = []

        # Get union of two clauses to remove duplicates
        resultList = list(set(clause1.literals) | set(clause2.literals))

        # Get the new clause by adding all literals to new clause except the resolved literals
        for literal in resultList:
            if '~' in literal and literal[1:] in resultList or '~' + literal in resultList:
                continue
            newClauseLiterals.append(literal)

        # Return the resolution
        return newClauseLiterals

        '''
        Print the new resolution with the line numbers that resolved
        '''
    def printLine(self, id, printedClause, resolved, c1Id='', c2Id=''):
        resolvedClausesNote = ' {' + str(c1Id) + ',' + str(c2Id) + '}' if resolved else ' {}'
        print str(id) + '. ' + printedClause + resolvedClausesNote
