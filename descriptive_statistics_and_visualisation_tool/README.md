# Descriptive Statistics and Visualisation Tool

This is a Python script that generates descriptive statistics and visualisations for a given dataset. It utilises the `pandas`, `seaborn`, and `matplotlib` libraries to create meaningful insights into the data.

## Features

- Computes descriptive statistics for the dataset, including count, mean, standard deviation, minimum, maximum, and quartiles.
- Generates histogram plots with kernel density estimation (KDE) for each numerical column in the dataset.
- Creates box plots for each numerical column to visualise the distribution and identify outliers.
- Produces violin plots for each numerical column to display the distribution and probability density.
- Generates a scatter plot matrix to visualise the relationships between numerical columns.
- Creates a correlation heatmap to identify the correlations between numerical columns.

## Requirements

To run this script, you need to have the following dependencies installed:

- Python 3.x
- pandas
- seaborn
- matplotlib

You can install the required libraries using pip:
- pip install pandas seaborn matplotlib

  ## Usage

1. Clone this repository to your local machine or download the script file.

2. Prepare your dataset in CSV format and note the file path.

3. Run the script using the following command:
- python descriptive_statistics_and_visualisation_tool.py

4. When prompted, enter the file path of your dataset.

5. The script will generate descriptive statistics and visualisations for your dataset.

## Example

Suppose you have a dataset named `data.csv` in the same directory as the script. You can run the script and provide the file path when prompted.
The script will compute descriptive statistics and generate visualisations for the numerical columns in the dataset.

## Error Handling

The script includes error handling for the following scenarios:

- If the specified file does not exist, it will print an error message.
- If a `FileNotFoundError` occurs during execution, it will print an error message.
- If an invalid plot type is entered, it will display an "Invalid plot type." message.

## Built-in Modules

The script uses the following built-in Python modules:

- `os`: Provides a way to interact with the operating system.
- `os.path`: Offers functions for working with file paths.

These modules are part of the Python standard library and do not require separate installation.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.
