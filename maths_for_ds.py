{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c9fc9ce0-7b0c-45fe-964c-0513f1fe6190",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Matrix-vector multiplication:\n",
      " [14 32 50]\n",
      "Trace of A: 15\n",
      "Eigenvalues:\n",
      " [ 1.61168440e+01 -1.11684397e+00 -4.22209278e-16]\n",
      "Eigenvectors:\n",
      " [[-0.23197069 -0.78583024  0.40824829]\n",
      " [-0.52532209 -0.08675134 -0.81649658]\n",
      " [-0.8186735   0.61232756  0.40824829]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Define the matrix A and vector B\n",
    "A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\n",
    "B = np.array([1, 2, 3])\n",
    "\n",
    "# a. Matrix-vector multiplication\n",
    "AxB = np.dot(A, B)\n",
    "print(\"Matrix-vector multiplication:\\n\", AxB)\n",
    "\n",
    "# b. Calculate the trace\n",
    "trace_A = np.trace(A)\n",
    "print(\"Trace of A:\", trace_A)\n",
    "\n",
    "# c. Find eigenvalues and eigenvectors\n",
    "eigenvalues, eigenvectors = np.linalg.eig(A)\n",
    "print(\"Eigenvalues:\\n\", eigenvalues)\n",
    "print(\"Eigenvectors:\\n\", eigenvectors)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3ab62a75-c318-4fd1-aa7e-f2f68c91ac37",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Determinant of updated A: 0.0\n",
      "The matrix is singular (non-invertible).\n"
     ]
    }
   ],
   "source": [
    "# Update the last row of matrix A\n",
    "A[2] = [10, 11, 12]\n",
    "\n",
    "# a. Compute the determinant\n",
    "det_A = np.linalg.det(A)\n",
    "print(\"Determinant of updated A:\", det_A)\n",
    "\n",
    "# b. Check if the matrix is singular or non-singular\n",
    "if det_A == 0:\n",
    "    print(\"The matrix is singular (non-invertible).\")\n",
    "else:\n",
    "    print(\"The matrix is non-singular (invertible).\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "773c2e2a-9d86-43e6-b879-d079d6d2680a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Matrix A is not invertible.\n"
     ]
    }
   ],
   "source": [
    "# Check if determinant is non-zero and calculate the inverse\n",
    "if det_A != 0:\n",
    "    A_inverse = np.linalg.inv(A)\n",
    "    print(\"Inverse of A:\\n\", A_inverse)\n",
    "else:\n",
    "    print(\"Matrix A is not invertible.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4686ed5a-da9b-4420-b9c1-7d870fc19244",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cannot solve system of equations: Singular matrix\n"
     ]
    }
   ],
   "source": [
    "# Solve A * X = B\n",
    "try:\n",
    "    X = np.linalg.solve(A, B)\n",
    "    print(\"Solution X:\\n\", X)\n",
    "except np.linalg.LinAlgError as e:\n",
    "    print(\"Cannot solve system of equations:\", e)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7614b74e-5cfd-4ebf-bc54-69dc2b0ae70a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Matrix C:\n",
      " [[ 6 16 20 12]\n",
      " [16 18  5  3]\n",
      " [ 3  1 10  4]\n",
      " [ 1  8 19  7]]\n",
      "Rank of C: 4\n",
      "Submatrix:\n",
      " [[20 12]\n",
      " [ 5  3]]\n",
      "Frobenius norm of C: 45.28796749689701\n"
     ]
    }
   ],
   "source": [
    "# Create a 4x4 matrix with random integers\n",
    "C = np.random.randint(1, 21, size=(4, 4))\n",
    "print(\"Matrix C:\\n\", C)\n",
    "\n",
    "# a. Compute the rank of C\n",
    "rank_C = np.linalg.matrix_rank(C)\n",
    "print(\"Rank of C:\", rank_C)\n",
    "\n",
    "# b. Extract the submatrix (first 2 rows, last 2 columns)\n",
    "submatrix = C[:2, -2:]\n",
    "print(\"Submatrix:\\n\", submatrix)\n",
    "\n",
    "# c. Calculate Frobenius norm\n",
    "frobenius_norm = np.linalg.norm(C, 'fro')\n",
    "print(\"Frobenius norm of C:\", frobenius_norm)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "79aecadd-af97-43de-81d9-5444f9ed58ff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Matrix multiplication result:\n",
      " [[ 47  55  60]\n",
      " [122 160 165]\n",
      " [272 370 375]]\n"
     ]
    }
   ],
   "source": [
    "# Trim C to 3x3 for compatibility with A\n",
    "C_trimmed = C[:3, :3]\n",
    "\n",
    "# Check compatibility and multiply\n",
    "if A.shape[1] == C_trimmed.shape[0]:\n",
    "    result = np.dot(A, C_trimmed)\n",
    "    print(\"Matrix multiplication result:\\n\", result)\n",
    "else:\n",
    "    print(\"Matrices are incompatible for multiplication. Reshape C as needed.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "296ab533-c82d-4e90-a860-c7ef4e506a94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Standardized D:\n",
      " [[ 0.          0.          0.          0.          0.        ]\n",
      " [-0.70710678 -0.70710678 -0.70710678 -0.70710678 -0.70710678]\n",
      " [-1.41421356 -1.41421356 -1.41421356 -1.41421356 -1.41421356]\n",
      " [ 0.70710678  0.70710678  0.70710678  0.70710678  0.70710678]\n",
      " [ 1.41421356  1.41421356  1.41421356  1.41421356  1.41421356]]\n",
      "Covariance matrix:\n",
      " [[1.25 1.25 1.25 1.25 1.25]\n",
      " [1.25 1.25 1.25 1.25 1.25]\n",
      " [1.25 1.25 1.25 1.25 1.25]\n",
      " [1.25 1.25 1.25 1.25 1.25]\n",
      " [1.25 1.25 1.25 1.25 1.25]]\n",
      "Eigenvalues:\n",
      " [0.00000000e+00 6.25000000e+00 1.09476443e-47 1.47911420e-31\n",
      " 0.00000000e+00]\n",
      "Eigenvectors:\n",
      " [[-0.89442719  0.4472136  -0.89442719 -0.65623515  0.89442719]\n",
      " [ 0.2236068   0.4472136   0.2236068   0.7525065  -0.2236068 ]\n",
      " [ 0.2236068   0.4472136   0.2236068  -0.03209045 -0.2236068 ]\n",
      " [ 0.2236068   0.4472136   0.2236068  -0.03209045 -0.2236068 ]\n",
      " [ 0.2236068   0.4472136   0.2236068  -0.03209045 -0.2236068 ]]\n",
      "D reduced to 2 principal components:\n",
      " [[ 0.00000000e+00  0.00000000e+00]\n",
      " [-2.22044605e-16 -1.58113883e+00]\n",
      " [-4.44089210e-16 -3.16227766e+00]\n",
      " [ 2.22044605e-16  1.58113883e+00]\n",
      " [ 4.44089210e-16  3.16227766e+00]]\n"
     ]
    }
   ],
   "source": [
    "# Create dataset D\n",
    "D = np.array([[3, 5, 7, 9, 11],\n",
    "              [2, 4, 6, 8, 10],\n",
    "              [1, 3, 5, 7, 9],\n",
    "              [4, 6, 8, 10, 12],\n",
    "              [5, 7, 9, 11, 13]])\n",
    "\n",
    "# a. Standardize D column-wise\n",
    "mean = D.mean(axis=0)\n",
    "std = D.std(axis=0)\n",
    "D_standardized = (D - mean) / std\n",
    "print(\"Standardized D:\\n\", D_standardized)\n",
    "\n",
    "# b. Compute covariance matrix\n",
    "covariance_matrix = np.cov(D_standardized, rowvar=False)\n",
    "print(\"Covariance matrix:\\n\", covariance_matrix)\n",
    "\n",
    "# c. Perform PCA\n",
    "eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)\n",
    "print(\"Eigenvalues:\\n\", eigenvalues)\n",
    "print(\"Eigenvectors:\\n\", eigenvectors)\n",
    "\n",
    "# Reduce D to 2 principal components\n",
    "pca_components = eigenvectors[:, :2]\n",
    "D_reduced = np.dot(D_standardized, pca_components)\n",
    "print(\"D reduced to 2 principal components:\\n\", D_reduced)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf3f0664-89c6-4c02-b1c3-97bf4253a4a3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
