import json
import os
from .train import Model

def main():
    """
    Main function for running inference using the pre-trained model.

    This function retrieves data from an environment variable, performs inference
    using the trained model, and saves the output (predictions) to a JSON file.
    """
    print("Starting inference...")

    # Load the model
    m = Model()

    # Get data from the environment variable
    data = os.getenv("DATA")
    if not data:
        raise ValueError("No data provided")
    
    print("Data loaded from environment variable:", data)

    # Parse the JSON data
    try:
        data = json.loads(data)
        print("Parsed data:", data)
    except json.JSONDecodeError as e:
        """
        Handles error if data is not in valid JSON format.
        
        Args:
            e (JSONDecodeError): Exception raised when JSON data cannot be parsed.
        
        Returns:
            None
        """
        print(f"Error parsing JSON: {e}")
        return

    # Perform inference on the parsed data
    records = [
        {
            "dataset": m.dataset,           # The dataset used for training
            "architecture": m.architecture, # Model architecture used (e.g., KNN)
            "features": m.eval,             # Model evaluation score (accuracy)
            "data": record,                 # Input data for inference
            "label": label,                 # Predicted label from the model
        }
        for record, label in zip(data, m(data))
    ]
    
    # Save the inference output to a JSON file
    with open("out.json", "w") as f:
        json.dump(records, f, indent=4)
    
    print("Inference completed. Results saved to 'out.json'.")

if __name__ == "__main__":
    main()
