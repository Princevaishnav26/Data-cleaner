from cleaner_functions import load_data, clean_missing_and_errors, handling_errors, value_range, save_data
import config

def main():  
    df = load_data(config.file_path)
    df = clean_missing_and_errors(df)
    df = handling_errors(df)
    df = value_range(df, config.min_moist, config.max_moist, config.min_temp, config.max_temp)
    save_data(df, config.output_path)
    print("The data is successfully cleaned, check cleaned_data.csv")

if __name__ == "__main__":
    main()
