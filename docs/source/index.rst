.. mail_alerting and machine learning operations documentation master file, created by
   sphinx-quickstart on Wed Sep 18 12:21:51 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



.. mail_alerting and machine learning operations documentation
.. ===========================================================

.. Add your content using ``reStructuredText`` syntax. See the
.. `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
.. documentation for details.


.. .. toctree::
..    :maxdepth: 2
..    :caption: Contents:

..    modules

Project Documentation
======================

Welcome to the documentation for **DSAN 6700 Assignment 1**. This project consists of two main components:

1. **Email Alert System**: A Python-based system for sending email notifications.
2. **ML Model System**: A machine learning application that trains, infers, and visualizes a KNN model using the Iris dataset.

The documentation provides instructions on how to set up, use, and contribute to the project. Below is the table of contents to help navigate through the project documentation.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api_reference

Project Overview
================

### Email Alert System

The email alert system allows users to send automated email notifications using a local SMTP server. The system is implemented using modern Python packaging and includes unit tests for reliability.

### ML Model System

The ML Model System trains a K-Nearest Neighbors (KNN) model using the Iris dataset. The system includes scripts for training, inference, and visualization of the results. The visualizations use UMAP for dimensionality reduction, and the model is evaluated for accuracy before saving.

ML Model System Components
===========================

### Visualize.py

`visualize.py` performs dimensionality reduction on the Iris dataset using UMAP (Uniform Manifold Approximation and Projection) and creates an interactive 2D scatter plot with Plotly. The scatter plot highlights the different species within the Iris dataset, with the projections plotted in a two-dimensional graph.

#### Code Explanation

The script follows these steps:

1. **Load the Iris dataset**: It uses the built-in Iris dataset from `sklearn.datasets`.
2. **Apply UMAP**: The `UMAP` algorithm is used to reduce the dimensionality of the dataset.
3. **Create a scatter plot**: Using Plotly Express, it generates an interactive scatter plot where each point represents an observation from the Iris dataset, color-coded by species.
4. **Export the plot**: The plot is saved as an HTML file (`index.html`) in the `public` directory, making it easy to open in a browser for interactive exploration.

#### Requirements

Before running the script, make sure that you have the required dependencies installed in your conda environment. This project specifically requires the `dsan-6700` environment to be activated.

##### Activating the Conda Environment

To activate the `dsan-6700` environment, run the following command in your terminal:

```bash
conda activate dsan-6700