# Logic Resoultion

This program reads a text file containing the initial set of valid clauses and a clause for
each literal in the negated clause that we want to test validity of. Each line in the file defines a
single clause. The literals of each clause are separated by a blank space and ∼ is used to represent
negation.

This program implements the resolution algorithm as explained in the previous section.
The output is either “Failure” if the clause cannot be shown to be valid, or the list of clauses in the
proof tree for deducing False. In either case it also returns the size of the final set of valid
clauses.

Let us consider a correct solution for testing the validity of ¬z ∨ y for our example. The input
file would be:
∼p q
∼z y
p
z
∼y
A possible final set of valid sentences could be:

1. ∼p q {}
2. ∼z y {}
3. p {}
4. z {}
5. ∼y {}
6. ∼z {2,5}
7. False {4,6}

Note how the program keeps track of the parents of new clauses. This is used for extracting the
clauses in the proof tree. The solution returned consists of these clauses and the size of the final
set of valid clauses:

2. ∼z y {}
3. z {}
4. ∼y {}
5. ∼z {2,5}
6. False {4,6}
Size of final clause set: 7

How to run: python main.py {filename}

