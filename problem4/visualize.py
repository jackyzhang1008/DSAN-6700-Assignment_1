import plotly.express as px
from sklearn.datasets import load_digits, load_iris
from umap import UMAP

def main():
    """
    Main function to visualize the Iris dataset using UMAP for dimensionality reduction.

    This function uses UMAP to reduce the Iris dataset's dimensionality from 4 features to 2,
    then generates a scatter plot of the projections. The plot is saved as an interactive HTML file
    and a static PNG image.

    - UMAP: Used for dimensionality reduction.
    - Plotly: Used for generating the scatter plot of the reduced data.
    """
    # Load the Iris dataset
    iris = load_iris()
    
    # Create a UMAP instance for 2D projections
    umap_2d = UMAP()

    # Fit UMAP on the iris dataset
    umap_2d.fit(iris.data)

    # Transform the data into 2D projections
    projections = umap_2d.transform(iris.data)

    # Create a scatter plot of the projections with the species as the color coding
    fig = px.scatter(
        projections,
        x=0,  # UMAP 1 on the x-axis
        y=1,  # UMAP 2 on the y-axis
        color=iris.target.astype(str),  # Color points based on species
        title="UMAP Projection of the Iris Dataset",  # Set the title of the plot
        labels={"color": "species", "0": "UMAP 1", "1": "UMAP 2"},  # Label axis and legend
        template="plotly"  # Set the plotly theme for visualization
    )

    # Save the interactive plot as an HTML file
    fig.write_html("public/index.html")

    # Save the plot as a PNG image for embedding in the README
    fig.write_image("iris_clusters.png")

if __name__ == "__main__":
    """
    Entry point for running the script.

    Calls the main function to visualize the Iris dataset and save the outputs as HTML and PNG files.
    """
    main()
