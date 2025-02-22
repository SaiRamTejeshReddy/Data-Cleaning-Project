Data Cleaning Project
This repository contains Python code that demonstrates the process of loading, cleaning, exploring, and visualizing a dataset using the pandas, matplotlib, and seaborn libraries. The script performs common data cleaning operations such as handling missing values and removing duplicates, followed by basic data exploration and visualization.
Key Features
* Load Data: Loads data either from a CSV file or sample data provided within the script.
* Clean Data: Removes duplicate rows and fills missing values with the median of numeric columns.
* Explore Data: Displays basic statistics, data types, and missing values for each column.
* Visualize Data: Generates a histogram with a Kernel Density Estimate (KDE) plot for a specified column.
* Save Cleaned Data: Saves the cleaned dataset to a new CSV file.
Installation
Before using the script, you need to have the required libraries installed. You can install the necessary dependencies using pip:
bash
CopyEdit
pip install pandas matplotlib seaborn
Usage
1. Loading Data
You can load a dataset either from a CSV file or from the predefined sample data provided in the script.
Load from a CSV File:
CopyEdit
df = load_data(file_path='path_to_your_file.csv')
Load from Sample Data:
The script also includes sample data for testing, which can be used without the need for an external file.
CopyEdit
sample_data = {
    'Column1': [1, 2, 2, 3, 4, 5, None],
    'Column2': [5, 6, 7, 8, 9, 10, 10],
    'Column3': [11, 12, 13, None, 15, 16, 17]
}

df = load_data(sample_data=sample_data)
2. Cleaning the Data
The data will be cleaned by:
* Removing duplicate rows.
* Filling missing values with the median of the numeric columns.
CopyEdit
df = clean_data(df)
3. Exploring the Data
Basic data exploration will display the following information:
* Data overview (columns, data types, non-null counts).
* Summary statistics for numerical columns (e.g., mean, standard deviation, min, max).
* Missing values for each column.
CopyEdit
explore_data(df)
4. Visualizing the Data
You can visualize the distribution of any column using histograms and KDE plots.
CopyEdit
visualize_data(df, 'Column1')
5. Saving the Cleaned Data
Finally, the cleaned dataset can be saved to a new CSV file:
CopyEdit
save_clean_data(df, 'cleaned_data.csv')
Example Workflow:
CopyEdit
if __name__ == "__main__":
    # Load data (either from a file or sample data)
    df = load_data(sample_data=sample_data)
    
    # Clean and explore data
    df = clean_data(df)
    explore_data(df)
    
    # Visualize data (replace 'Column1' with your desired column)
    visualize_data(df, 'Column1')
    
    # Save the cleaned dataset to a file
    output_path = "cleaned_data.csv"
    save_clean_data(df, output_path)
Project Structure:
* main.py: Contains the main Python script with functions to load, clean, explore, visualize, and save the dataset.
* README.md: Project documentation that explains how to use the script and the functionality provided.
