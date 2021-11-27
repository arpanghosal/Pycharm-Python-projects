# This is a sample Python script for numpy.

import numpy as np
#import pandas as pd
import scipy.sparse as spr
matrix = np.array([[1,2,3],[4,5,6]])
print(matrix)

matrix_sparse = spr.csr_matrix(matrix)
print(matrix_sparse)   #give element order (i,j) too :  sparse only stores non zero elements and assumes others to be 0

#Create a Matrix
matrix = np.array([[0,0],[0,1],[3,0]])
print(matrix)

#Create Compressed Sparse Row(CSR) matrix
matrix_sparse = spr.csr_matrix(matrix)
print(matrix_sparse)   #this will show only (i,j) of non zero element

print(matrix_sparse[1,1])  #Here 1

vector = np.array([1,2,3,4,3,2,3])  #creating vector as array

#Select the last element
print(vector[-1])   #Here 3
#Select the first 2 rows and all the columns of the matrix
print(matrix[:2,:])

#View the Number of Rows and Columns
print(matrix.shape)  #3X2
#View the number of elements (rows*columns)
print(matrix.size)  #6
#View the number of Dimensions
print(matrix.ndim)  #2 - row and column


#Create a Matrix
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)
print(matrix.ndim)

#Create a function that adds 100 to something
add_100 =lambda i: i+100

#Convert it into a vectorized function
vectorized_add_100= np.vectorize(add_100)

#Apply function to all elements in matrix
print(vectorized_add_100(matrix))
"""
[[101 102 103]
 [104 105 106]
 [107 108 109]]
"""
#Return the max element
print(np.max(matrix)) #9
#Return the min element
print(np.min(matrix)) #1
#To find the max element in each column
print(np.max(matrix,axis=0)) #[7 8 9]
#To find the max element in each row
print(np.max(matrix,axis=1)) #[3 6 9]

#Mean
print(np.mean(matrix))
#Standard Dev.
print(np.std(matrix))
#Variance
print(np.var(matrix))

#Reshape
print(matrix.reshape(9,1))  #9X1
#Here -1 says as many columns as needed and 1 row
print(matrix.reshape(1,-1))  #1X9 [[1 2 3 4 5 6 7 8 9]]
#If we provide only 1 value Reshape would return a 1-d array of that length
print(matrix.reshape(9))  #[1 2 3 4 5 6 7 8 9]
#We can also use the Flatten method to convert a matrix to 1-d array
print(matrix.flatten())  #[1 2 3 4 5 6 7 8 9]

#Transpose the matrix
print(matrix.T)

#Calculate the Determinant
print(np.linalg.det(matrix)) #Here 0
#Calculate the Rank - The rank of a Matrix is the number of dimensions of the ..
#.. vector space spanned by its rows or columns.
print(np.linalg.matrix_rank(matrix))  #Here 2

#Calculate its inverse
matrix = np.array([[1,2,3],[4,6,6],[8,8,9]])
print(np.linalg.inv(matrix))  #Error if matrix is Singular

#Print the Principal diagonal
print(matrix.diagonal())
#Print the diagonal one above the Principal diagonal
print(matrix.diagonal(offset=1)) #[2 6]
#Print the diagonal one below Principal diagonal
print(matrix.diagonal(offset=-1)) #[4 8]
#Print the Trace
print(matrix.trace())

# Calculate the Eigenvalues and Eigenvectors of that Matrix
eigenvalues ,eigenvectors=np.linalg.eig(matrix)
print(eigenvalues)
print(eigenvectors)


#Create vector-1
vector_1 = np.array([ 1,2,3 ])
#Create vector-2
vector_2 = np.array([ 4,5,6 ])
#Calculate Dot Product
print(np.dot(vector_1,vector_2))  #32
#Alternatively you can use @ to calculate dot products
print(vector_1 @ vector_2)


#Create Matrix-1
matrix_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
#Create Matrix-2
matrix_2 = np.array([[7,8,9],[4,5,6],[1,2,3]])
#Add the 2 Matrices
print(np.add(matrix_1,matrix_2))  #element to element addition
#Subtraction
print(np.subtract(matrix_1,matrix_2)) #m1(i,j)-m2(i,j)
#Multiplication(Element wise, not Dot Product)
print(matrix_1*matrix_2)

#Set seed
np.random.seed(2)

#Generate 3 random integers b/w 1 and 10
print(np.random.randint(0,11,3))
#Draw 3 numbers from a normal distribution with mean 1.0 and std 2.0
print(np.random.normal(1.0,2.0,3))

print(matrix.dtype)  #int64

print(np.where(matrix < 4, -1, matrix))  #wherever value is less than 4, replace with -1

