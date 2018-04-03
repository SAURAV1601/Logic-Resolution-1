from solver import Solver
import sys

s = Solver()

# Get KB filename from arguments
filename = sys.argv[1]

# Add each clause from the KB to the solver
for line in open(filename, 'r'):
    s.addClause(line)

# Run resolution
s.solve()
