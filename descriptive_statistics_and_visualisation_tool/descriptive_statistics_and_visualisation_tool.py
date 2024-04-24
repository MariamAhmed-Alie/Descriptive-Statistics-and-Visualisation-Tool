import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import os.path

# Create descriptives and visuals function
def descriptives_and_visuals(data_path, plot_type):
    try:
        if os.path.isfile(data_path):
            # Load data into pandas DataFrame
            data = pd.read_csv(data_path)
            
            # Compute descriptive statistics
            descriptive_stats = data.describe()
            print(descriptive_stats)
            
            # Create visualisations for numerical columns
            numerical_cols = data.select_dtypes(include=['number']).columns
            
            if plot_type == 'histogram':
                for col in numerical_cols:
                    sns.histplot(data=data, x=col, bins=30, color='r', kde=True)
                    plt.title(f"Histogram of {col}")
                    plt.show()
            elif plot_type == 'boxplot':
                for col in numerical_cols:
                    sns.boxplot(data=data, x=col, palette='Set3')
                    plt.title(f"Box Plot of {col}")
                    plt.show()
            elif plot_type == 'violinplot':
                for col in numerical_cols:
                    sns.violinplot(data=data, x=col, palette='Set2')
                    plt.title(f"Violin Plot of {col}")
                    plt.show()
            elif plot_type == 'pairplot':
                sns.pairplot(data[numerical_cols])
                plt.title("Scatter Plot Matrix")
                plt.show()
            elif plot_type == 'heatmap':
                sns.heatmap(data[numerical_cols].corr(), annot=True, cmap='summer')
                plt.title("Correlation Heatmap")
                plt.show()
            else:
                print("Invalid plot type.")
        else:
            print("File does not exist.")
    except FileNotFoundError as e:
        print("File does not exist.")

# Request user input of file path
file_path = input("Please enter the file path: ")

# Ask user to choose plot type
plot_type = input("Please choose a plot type (histogram, boxplot, violinplot, pairplot, heatmap): ")

# Call function
descriptives_and_visuals(file_path, plot_type)