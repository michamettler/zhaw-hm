import numpy as np
from numpy.linalg import norm, eig

def adjust_matrix_to_norm(matrix, target_norm, norm_type='fro'):
    """
    Passt eine Matrix so an, dass sie eine bestimmte Norm aufweist.
    :param matrix: Die zu modifizierende Matrix.
    :param target_norm: Die Zielnorm für die Matrix.
    :param norm_type: Typ der Norm ('fro', 2 oder 'inf').
    :return: Angepasste Matrix.
    """
    current_norm = norm(matrix, ord=norm_type)
    if current_norm == 0:
        raise ValueError("Die aktuelle Norm der Matrix ist 0, Anpassung nicht möglich.")
    
    adjustment_factor = target_norm / current_norm
    adjusted_matrix = matrix * adjustment_factor
    return adjusted_matrix

def modify_eigenvectors(eigenvectors):
    """
    Fügt eine kleine Störung zu den Eigenvektoren hinzu, um eine unterschiedliche, aber ähnliche Matrix zu erzeugen.
    :param eigenvectors: Die Eigenvektoren der Matrix.
    :return: Modifizierte Eigenvektoren.
    """
    disturbance = np.random.rand(*eigenvectors.shape) * 0.01  # Kleine Störung
    disturbed_eigenvectors = eigenvectors + disturbance
    return disturbed_eigenvectors

def find_similar_matrix_with_same_norm(original_matrix, norm_type='fro'):
    """
    Findet eine ähnliche Matrix mit der gleichen Norm wie die ursprüngliche Matrix.
    :param original_matrix: Die ursprüngliche Matrix.
    :param norm_type: Typ der Norm ('fro', 2 oder 'inf').
    :return: Eine ähnliche Matrix mit der gleichen Norm.
    """
    eigenvalues, eigenvectors = eig(original_matrix)
    modified_eigenvectors = modify_eigenvectors(eigenvectors)
    similar_matrix = modified_eigenvectors @ np.diag(eigenvalues) @ np.linalg.inv(modified_eigenvectors)
    target_norm = norm(original_matrix, ord=norm_type)
    similar_matrix_with_same_norm = adjust_matrix_to_norm(similar_matrix, target_norm, norm_type)
    return similar_matrix_with_same_norm

# Beispiel
A = np.array([[4, -2], [1, 1]])
similar_A = find_similar_matrix_with_same_norm(A, 'fro')

print("Original Matrix:\n", A)
print("Ähnliche Matrix mit gleicher Norm:\n", similar_A)
