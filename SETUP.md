# Environment Setup Guide

This project uses two conda environments for different purposes:
- **ai**: Python 3.14.6 - EDA, data cleaning, and ML models
- **graph**: Python 3.11.15 - GraphSAGE and graph neural network models

## Quick Setup

### 1. Recreate the AI Environment

```bash
conda create --name ai python=3.14.6
conda activate ai
pip install -r ai_requirements.txt
```

### 2. Recreate the Graph Environment

```bash
conda create --name graph python=3.11.15
conda activate graph
pip install -r graph_requirements.txt
```

## Running the Notebook

In VS Code or Jupyter:

```bash
# Start the appropriate environment
conda activate ai
# or
conda activate graph

jupyter notebook
```

Then open `03_graph_models.ipynb` (training) or `03_graph_models_result.ipynb` (metrics) and select the `graph` or `ai` kernel.

## Updating Requirements

If you install new packages, update the requirements files:

```bash
conda activate ai
pip freeze > ai_requirements.txt

conda activate graph
pip freeze > graph_requirements.txt
```

**Note:** The `ai/` and `graph/` directories are ignored by git and should **not** be committed to the repository. Use the requirements files to track dependencies instead.
