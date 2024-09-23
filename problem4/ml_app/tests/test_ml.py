import pytest
from sklearn.datasets import load_iris

def test_dataset_shape():
    """
    Test the shape of the Iris dataset.

    This function loads the Iris dataset using `load_iris()` and checks the following:
    1. The feature matrix `X` should have 150 rows (samples) and 4 columns (features).
    2. The target array `y` should have 150 elements (one for each sample).

    Assertions:
        - Verifies that the feature matrix `X` has a shape of (150, 4).
        - Verifies that the target array `y` has a shape of (150,).
    
    Raises:
        AssertionError: If the shapes of the feature matrix or target array are incorrect.
    """
    
    # Load the Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Test if the shape of the features matrix is correct
    assert X.shape == (150, 4), "The features matrix should have shape (150, 4)"
    
    # Test if the shape of the target array is correct
    assert y.shape == (150,), "The target array should have 150 elements"
