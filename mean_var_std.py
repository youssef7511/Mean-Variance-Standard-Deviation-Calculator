import numpy as np

def calculate(list):
    # Check if the list contains exactly 9 elements
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in list):
        raise ValueError("List must contain only numbers.")
    
    # Convert list to 3x3 numpy array
    matrix = np.array(list).reshape(3, 3)
    
    # Calculate statistics
    # axis=0 means along columns (vertical), axis=1 means along rows (horizontal)
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # Mean of each column
            matrix.mean(axis=1).tolist(),  # Mean of each row
            matrix.mean().item()           # Mean of flattened matrix
        ],
        'variance': [
            matrix.var(axis=0).tolist(),   # Variance of each column
            matrix.var(axis=1).tolist(),   # Variance of each row
            matrix.var().item()            # Variance of flattened matrix
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),   # Std dev of each column
            matrix.std(axis=1).tolist(),   # Std dev of each row
            matrix.std().item()            # Std dev of flattened matrix
        ],
        'max': [
            matrix.max(axis=0).tolist(),   # Max of each column
            matrix.max(axis=1).tolist(),   # Max of each row
            matrix.max().item()            # Max of flattened matrix
        ],
        'min': [
            matrix.min(axis=0).tolist(),   # Min of each column
            matrix.min(axis=1).tolist(),   # Min of each row
            matrix.min().item()            # Min of flattened matrix
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),   # Sum of each column
            matrix.sum(axis=1).tolist(),   # Sum of each row
            matrix.sum().item()            # Sum of flattened matrix
        ]
    }
    
    return calculations