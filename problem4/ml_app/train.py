from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pickle

class Model:
    """
    A KNN model for classifying the Iris dataset.
    
    This class initializes, trains, and evaluates a K-Nearest Neighbors (KNN) model on the Iris dataset.
    It also provides an inference function for making predictions on new data.
    
    Attributes:
        dataset (str): The dataset used ('iris').
        architecture (str): The model architecture ('KNN').
        eval (float): The evaluation score (accuracy) of the trained model.
    """

    def __init__(self, test_size=0.5):
        """
        Initializes the Model instance by setting up the dataset, architecture, and calling the training method.

        Args:
            test_size (float): Proportion of the dataset to be used for testing (default is 0.5).
        """
        self.dataset = "iris"
        self.architecture = "KNN"
        self._train(test_size)

    def __call__(self, data):
        """
        Performs inference on the input data.

        Args:
            data (list of lists): New input data for which predictions need to be made.
        
        Yields:
            str: Predicted label (species name) for each record.

        Raises:
            ValueError: If the input data is malformed.
        """
        for record in data:
            if len(record) != len(self.labels) and not all([isinstance(val, float) or isinstance(val, int) for val in record]):
                raise ValueError(f"Malformed data record {record}")

        yield from (self.labels[label] for label in self.model.predict(data))

    def _init_data(self, test_size=0.5):
        """
        Initializes the Iris dataset, splits it into training and evaluation sets, and prepares them for model training.

        Args:
            test_size (float): Proportion of the dataset to be used for testing.
        
        Attributes:
            features (list of str): Names of the feature columns.
            labels (list of str): Names of the target labels (species).
            _train_data (tuple): Training features and labels.
            _eval_data (tuple): Evaluation features and labels.
        """
        iris_dataset = load_iris()
        self.features = iris_dataset.feature_names
        self.labels = iris_dataset.target_names
        x_train, x_test, y_train, y_test = train_test_split(iris_dataset.data, iris_dataset.target, test_size=test_size)
        self._train_data = (x_train, y_train)
        self._eval_data = (x_test, y_test)

    def _score(self):
        """
        Evaluates the model on the test data and returns the accuracy score.

        Returns:
            float: Accuracy score of the model.
        """
        preds = self.model.predict(self._eval_data[0])
        return accuracy_score(preds, self._eval_data[1])

    def _train(self, test_size=0.5):
        """
        Trains the KNN model on the training data, evaluates it on the test data, and saves the model.

        Args:
            test_size (float): Proportion of the dataset to be used for testing.
        
        Side Effects:
            - Saves the trained model to 'knn_model.pkl'.
            - Prints out the model's accuracy and confirms the model has been saved.
        """
        self._init_data()
        classifier = KNeighborsClassifier()
        classifier.fit(*self._train_data)
        self.model = classifier
        self.eval = self._score()

        # Save the trained model
        with open("knn_model.pkl", "wb") as f:
            pickle.dump(self.model, f)

        # Print training summary
        print(f"Model trained with accuracy: {self.eval:.4f}")
        print("Model saved as 'knn_model.pkl'")

if __name__ == "__main__":
    """
    Entry point to train the model.

    This block trains the model with a 50% test size and saves the trained model as 'knn_model.pkl'.
    """
    model = Model(test_size=0.5)
