import plotly.express as px
from sklearn.datasets import load_digits, load_iris
from umap import UMAP

def main():
    iris = load_iris()
    umap_2d = UMAP()

    # updated to visualize iris dataset
    umap_2d.fit(iris.data)

    projections = umap_2d.transform(iris.data)

    # Use the iris dataset target for coloring
    fig = px.scatter(
        projections,
        x=0,
        y=1,
        color=iris.target.astype(str),
        title="UMAP Projection of the Iris Dataset",
        labels={"color": "species", "0": "UMAP 1", "1": "UMAP 2"},
        template="plotly"
    )

    # Save the interactive plot as an HTML file
    fig.write_html("public/index.html")

    # Save the plot as a PNG image for embedding in the README
    fig.write_image("iris_clusters.png")

if __name__ == "__main__":
    main()
