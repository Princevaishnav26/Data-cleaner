# Sensor Data Cleaning Pipeline

A lightweight Python pipeline for cleaning irrigation sensor readings from CSV input and exporting validated data.

This project is designed for tabular sensor logs that may contain:
- Missing values
- Explicit error tokens in temperature readings
- Out-of-range moisture or temperature values

The cleaned dataset is saved as a new CSV file and can be used for downstream analytics or ML workflows.

## What This Project Does

The pipeline in main.py performs the following steps in order:

1. Load CSV data from the configured input path.
2. Forward-fill missing values across all columns.
3. Replace temperature value "ERROR" with missing value, then forward-fill again.
4. Keep only rows where:
   - soil_moisture_pct is between configured min and max
   - temperature_c is between configured min and max
5. Save the cleaned result to the configured output path.

## Current Configuration

Defined in config.py:

- Input file: raw_data.csv
- Output file: cleaned_data.csv
- Moisture range: 0 to 100
- Temperature range: -10 to 60

## Input Schema

The current dataset uses these columns:

- timestamp
- sensor_id
- soil_moisture_pct
- temperature_c
- hardware_status

Example raw issues currently handled:
- Empty moisture/temperature fields
- Temperature value "ERROR"
- Invalid numeric outliers such as soil moisture -15.0, 999.9 or temperature 150.0

## Project Structure

- main.py: Pipeline entry point
- cleaner_functions.py: Data loading, cleaning, filtering, and export functions
- config.py: File paths and validation thresholds
- raw_data.csv: Source data
- cleaned_data.csv: Generated cleaned output

## Requirements

- Python 3.8+
- pandas
- numpy

Install dependencies:

```bash
pip install pandas numpy
```

## How To Run

From the project root directory:

```bash
python main.py
```

Expected console message:

The data is successfully cleaned, check cleaned_data.csv

## Cleaning Logic Details

### 1) Missing values
The function clean_missing_and_errors uses forward fill (ffill), which copies the previous valid row value into missing cells.

### 2) Temperature error token
The function handling_errors replaces "ERROR" in temperature_c with missing value and applies forward fill again.

### 3) Range validation
The function value_range filters records using configured numeric boundaries:
- soil_moisture_pct: [min_moist, max_moist]
- temperature_c: [min_temp, max_temp]

Rows outside these ranges are removed.

## Notes and Limitations

- Forward fill is applied to the full DataFrame, not per sensor_id.
  This means missing values in one sensor row may be filled from a previous row belonging to a different sensor.
- temperature_c is cast to float before temperature range filtering.
  Any unexpected non-numeric text values (other than "ERROR") may raise a conversion error.
- Relative file paths are used in config.py, so run commands from the project root folder.

## Example Outcome

With the current sample data, invalid rows (for example out-of-range moisture and temperature) are removed, and cleaned_data.csv contains only records within configured bounds.

## Next Improvements (Optional)

- Apply forward fill separately per sensor_id
- Add automated tests for each cleaning function
- Add logging and row-level cleaning statistics
- Add a requirements.txt file for reproducible setup

## License

No license file is currently included in this repository. Add one if you plan to distribute or open-source this project.
