import pytest
from sklearn.datasets import load_iris

def test_dataset_shape():
    
    # Load the Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Test if the shape of the features matrix is correct
    assert X.shape == (150, 4), "The features matrix should have shape (150, 4)"

    # Test if the shape of the target array is correct
    assert y.shape == (150,), "The target array should have 150 elements"
