import torch

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

if __name__ == "__main__":
	m = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	print(row_swap(m, 0, 2))
	print(row_scale(m, 1, 10))
	print(row_replacement(m, 0, 1, 2, 3))
