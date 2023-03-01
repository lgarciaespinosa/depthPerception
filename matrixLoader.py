import numpy as np

PERSPECTIVE_MATRIX_FILE = "perspective_matrix.npy"

def get_perspective_matrix() -> np.ndarray:
        perspective_matrix = None 
        try:
            perspective_matrix = load_perspective_matrix()
        except IOError:
            print("Error")
        
        return perspective_matrix

def load_perspective_matrix() -> np.ndarray:
    return np.load(PERSPECTIVE_MATRIX_FILE)

def normalize_coordinates(coordinates):
        normalized_coordinates = np.array( [ [coordinates[0]], [coordinates[1]], [1]]
                                            ,dtype="float64")

        return normalized_coordinates
