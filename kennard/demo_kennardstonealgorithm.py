# -*- coding: utf-8 -*- %reset -f
"""
@author: MFSantos
Demonstration of Kennard-Stone algorighm
"""

import matplotlib.pyplot as plt
import numpy as np

import kennardstonealgorithm

number_of_samples = 100
number_of_selected_samples = 35

# Gerando amostras para demonstração
X = np.random.rand(number_of_samples, 2)
print("Dados X selecionados")
print(X)
# standarize X
autoscaled_X = (X - X.mean(axis=0)) / X.std(axis=0, ddof=1)
print("Dados X autoescalado")
print(autoscaled_X)

# Seleciona as Amostras utilizando o Algoritimo de Kennard Stonne
selected_sample_numbers, remaining_sample_numbers = kennardstonealgorithm.kennardstonealgorithm(
    autoscaled_X, number_of_selected_samples)
print("número de amostras selecionadas")
print(selected_sample_numbers)
print("---")
print("números de amostra restantes")
print(remaining_sample_numbers)

# plot samples
plt.figure()
plt.scatter(autoscaled_X[:, 0], autoscaled_X[:, 1], label="all samples")
plt.scatter(autoscaled_X[selected_sample_numbers, 0], autoscaled_X[selected_sample_numbers, 1], marker="*",
            label="all samples")
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend(loc='upper right')
plt.show()
