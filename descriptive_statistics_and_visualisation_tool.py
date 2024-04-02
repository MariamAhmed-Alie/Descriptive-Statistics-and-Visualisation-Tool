import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import os.path

# Create descriptives and visuals function
def descriptives_and_visuals(data_path):
    try:
        if os.path.isfile(data_path):
            # Load data into pandas DataFrame
            data = pd.read_csv(data_path)

            # Compute descriptive statistics
            descriptive_stats = data.describe()
            print(descriptive_stats)

            # Create visualisations for numerical columns
            numerical_cols = data.select_dtypes(include=['number']).columns
            for col in numerical_cols:
                sns.histplot(data=data, x=col, kde=True)
                plt.title(f"Histogram of {col}")
                plt.show()

            for col in numerical_cols:
                sns.boxplot(data=data, x=col)
                plt.title(f"Box Plot of {col}")
                plt.show()

            # Create violin plots for all numerical columns
            for col in numerical_cols:
                sns.violinplot(data=data, x=col)
                plt.title(f"Violin Plot of {col}")
                plt.show()

            sns.pairplot(data[numerical_cols])
            plt.title("Scatter Plot Matrix")
            plt.show()

            sns.heatmap(data[numerical_cols].corr(), annot=True)
            plt.title("Correlation Heatmap")
            plt.show()
        else:
            print("File does not exist.")
    except FileNotFoundError as e:
        print("File does not exist.")

# Request user input of file path
file_path = input("Please enter the file path: ")

# Call function
descriptives_and_visuals(file_path)
    




    
    
    


