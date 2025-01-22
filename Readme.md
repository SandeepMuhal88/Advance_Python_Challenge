# Python Libraries Overview

## NumPy
NumPy is a fundamental package for scientific computing in Python. It provides support for arrays, matrices, and a large collection of mathematical functions to operate on these data structures. Key features include:
- N-dimensional arrays

- Mathematical functions for array operations
- Linear algebra, Fourier transforms, and random number generation

### Learn More
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [NumPy Tutorial](https://www.w3schools.com/python/numpy_intro.asp)

## Pandas
Pandas is a powerful data manipulation and analysis library for Python. It provides data structures like Series and DataFrames, which allow for easy handling of structured data. Key features include:
- Data cleaning and preparation
- Data analysis and exploration
- Time series functionality

### Learn More
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [Pandas Tutorial](https://www.w3schools.com/python/pandas/default.asp)

## Matplotlib
Matplotlib is a plotting library for Python that provides a flexible way to create static, animated, and interactive visualizations. Key features include:
- Wide variety of plots (line, bar, scatter, etc.)
- Customizable visualizations
- Integration with Jupyter notebooks

### Learn More
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Matplotlib Tutorial](https://www.w3schools.com/python/matplotlib_intro.asp)

## Seaborn
Seaborn is a statistical data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. Key features include:
- Built-in themes for styling Matplotlib graphics
- Functions for visualizing distributions and relationships
- Support for complex visualizations with minimal code

### Learn More
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Seaborn Tutorial](https://www.w3schools.com/python/python_seaborn.asp)
## Scikit-learn
Scikit-learn is a machine learning library for Python that provides simple and efficient tools for data mining and data analysis. It is built on NumPy, SciPy, and Matplotlib. Key features include:
- Classification, regression, and clustering algorithms
- Model selection and evaluation tools
- Preprocessing utilities for data preparation

### Learn More
- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Scikit-learn Tutorial](https://www.w3schools.com/python/python_ml_getting_started.asp)


# Jupyter Notebook

Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text. It is widely used for data analysis, machine learning, and scientific research.

## How to Use Jupyter Notebook

### Installation
To install Jupyter Notebook, you can use pip. Run the following command in your terminal:
```bash
pip install notebook
```

### Starting Jupyter Notebook
Once installed, you can start Jupyter Notebook by running:
```bash
jupyter notebook
```
This command will open a new tab in your web browser with the Jupyter Notebook interface.

### Creating a New Notebook
1. In the Jupyter interface, navigate to the directory where you want to create a new notebook.
2. Click on the "New" button and select "Python 3" (or your preferred kernel) from the dropdown menu.

### Using the Notebook
- You can write code in the cells and execute them by pressing `Shift + Enter`.
- You can also add Markdown cells for documentation and explanations.
- To save your notebook, click on the disk icon or use `Ctrl + S`.

### Exporting Notebooks
You can export your notebook in various formats, including HTML and PDF, by going to the "File" menu and selecting "Download as".

### Stopping the Notebook Server
To stop the Jupyter Notebook server, go back to the terminal where you started it and press `Ctrl + C`.

# Setting Up a Python Virtual Environment

A virtual environment in Python is an isolated environment where you can manage dependencies for your projects independently. This is particularly useful for avoiding conflicts between package versions across different projects.

## Step-by-Step Instructions

### 1. Check Python Installation
Make sure Python is installed on your system. Run the following command in your terminal or command prompt:
```bash
python --version
```
Or if you're using Python 3:
```bash
python3 --version
```

### 2. Install virtualenv (if needed)
Although Python 3.3+ comes with `venv` built-in, you can use `virtualenv` for additional flexibility. Install it using:
```bash
pip install virtualenv
```

### 3. Create the Virtual Environment
Navigate to your project directory and run:
```bash
python -m venv myenv
```
Replace `myenv` with the name of your virtual environment. This will create a directory named `myenv` with all necessary files.

### 4. Activate the Virtual Environment
Depending on your operating system, use the following commands to activate your virtual environment:

**Windows:**
```bash
myenv\Scripts\activate
```

**macOS/Linux:**
```bash
source myenv/bin/activate
```
After activation, your terminal prompt will show the name of the virtual environment (e.g., `(myenv)`).

### 5. Install Dependencies in the Virtual Environment
Once activated, install the required libraries using pip:
```bash
pip install <package-name>
```

### 6. Deactivate the Virtual Environment
To deactivate the virtual environment, simply run:
```bash
deactivate
```

### 7. Delete the Virtual Environment
If you no longer need the virtual environment, you can delete its folder:
```bash
rm -rf myenv  # macOS/Linux
rmdir /s myenv  # Windows
