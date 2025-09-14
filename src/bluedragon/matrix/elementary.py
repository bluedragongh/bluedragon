import torch
import numpy as np
def row_swap(m, i, j):
	"""Swap rows i and j of matrix m in place."""
	new_m = m.clone()

	if i != j:
		new_m[[i, j]] = new_m[[j, i]]
	return new_m


def row_scale(m, i, f):
	"""Scale row i of matrix m by factor f in place."""
	new_m = m.clone()
	new_m[i] = new_m[i] * f
	return new_m


def row_replacement(m, i, j, s_i, s_j):
	new_m = m.clone()
	new_m[j] = s_i * new_m[i] + s_j * new_m[j]
	return new_m

def rref(m, tol=1e-6):
	a = np.asarray(m).astype(float)
	#a = np.array(m).astype(float)
	rows, cols = a.shape
	r = 0
	for col in range(cols):
		pivot = np.argmax(np.abs(a[r:rows, col])) + r
		if abs(a[pivot, col]) < tol:
			continue
		a[[r, pivot]] = a[[pivot, r]]
		a[r] = a[r] / a[r, col]
		for i in range(rows):
			if i != r:
				a[i] = a[i] - a[i, col] * a[r]

		r+=1
		if r == rows:
			break
	a[np.abs(a) < tol] = 0.0
	return a

if __name__ == "__main__":
	m = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	print(row_swap(m, 0, 2))
	print(row_scale(m, 1, 10))
	print(row_replacement(m, 0, 1, 2, 3))
	print(rref(m))
