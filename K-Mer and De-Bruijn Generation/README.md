
# K-Mer and De-Bruijn Graph Generation

This Jupyter notebook demonstrates the process of generating k-mers from genomic sequences and constructing a De Bruijn graph, commonly used in bioinformatics for genome assembly and analysis.

## Overview

The notebook includes steps for generating a dataset using a provided script, extracting k-mers from the sequences, and constructing and visualizing a De Bruijn graph.

## Prerequisites

- Python 3.x
- Jupyter Notebook or JupyterLab
- Matplotlib
- NetworkX

## Setup and Installation

1. Ensure Python and the required libraries are installed.
2. Clone the repository or download the notebook and accompanying scripts.
3. Run the data generation script (e.g., `datasetGenerator_hw2.py`) to create the input data file.

## Workflow

- The notebook reads the generated text file containing genomic sequences.
- It processes these sequences to extract k-mers and stores them in a separate file.
- A De Bruijn graph is constructed from these k-mers.
- The graph is visualized using Matplotlib and NetworkX.

## Running the Notebook

Open the `K-Mer and De-Bruijn graph Generation.ipynb` notebook in Jupyter and execute the cells in order to reproduce the analysis and graph generation.

## Contributing

Contributions to the project are welcome. Please fork the repository, make your changes, and submit pull requests.
