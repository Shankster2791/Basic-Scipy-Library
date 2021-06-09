from scipy.sparse import diags
from scipy import sparse
diagonals = [[1, 2, 3, 4], [1, 2, 3], [1, 2]]

A = diags(diagonals, [0, -1, 2]).toarray()
B = sparse.eye(3).toarray()

print(A)
print("\n")
print(B)

sparse.isspmatrix(A)
sparse.isspmatrix(B)


