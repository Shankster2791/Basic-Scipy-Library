#Q5. Create Sparse matrices A and B and analyze various functions of sciPy sparse package.

from scipy.sparse import diags
from scipy import sparse
diagonals = [[1, 2, 3, 4], [1, 2, 3], [1, 2]]

A = diags(diagonals, [0, -1, 2]).toarray() #Construct a sparse matrix from diagonals

B = sparse.eye(4).toarray() #Sparse matrix with ones on diagonal

#Returns a sparse (m x n) matrix where the kth diagonal is all ones and everything else is zeros.

print(A)
print("\n")
print(B)
print("\n")
print(sparse.isspmatrix(A)) #Is A of a sparse matrix type?
print(sparse.isspmatrix(sparse.csr_matrix([[5]]))) #Is Given matrix of a sparse matrix type?
#CSR => Compressed Sparse Row matrix
print("\n")
C = sparse.coo_matrix([[1, 2], [3, 4]])
print("\n")
D = sparse.coo_matrix([[5, 6],[7,8]]) #A sparse matrix in COOrdinate format.
#Also known as the ‘ijv’ or ‘triplet’ format.

print(sparse.vstack([C, D]).toarray()) #Stack sparse matrices vertically (row wise)
print("\n")
print(sparse.hstack([C,D]).toarray()) #Stack sparse matrices horizontally (column wise)
print("\n")
print(sparse.find(C)) #Return the indices and values of the nonzero elements of a matrix

