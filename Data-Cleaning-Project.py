import pandas as pd

def load_data(file_path=None, sample_data=None):
    """Load dataset either from a CSV file or sample data."""
    if file_path:
        return pd.read_csv(file_path)
    elif sample_data:
        return pd.DataFrame(sample_data)
    else:
        raise ValueError("Either file_path or sample_data must be provided.")

def clean_data(df):
    """Clean the dataset by handling missing values and duplicates."""
    df.drop_duplicates(inplace=True)
    df.fillna(df.median(numeric_only=True), inplace=True)
    return df

def explore_data(df):
    """Generate basic statistics and data overview."""
    print("Data Overview:\n", df.info())
    print("\nSummary Statistics:\n", df.describe())
    print("\nMissing Values:\n", df.isnull().sum())

def save_clean_data(df, output_path):
    """Save the cleaned data to a new CSV file."""
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

# Sample data for demonstration
sample_data = {
    'Column1': [1, 2, 2, 3, 4, 5, None],
    'Column2': [5, 6, 7, 8, 9, 10, 10],
    'Column3': [11, 12, 13, None, 15, 16, 17]
}

if __name__ == "__main__":
    # Use sample data instead of file input for online compilers
    df = load_data(sample_data=sample_data)
    
    # Clean and explore data
    df = clean_data(df)
    explore_data(df)
    
    # Save the cleaned dataset to a file
    output_path = "cleaned_data.csv"
    save_clean_data(df, output_path)