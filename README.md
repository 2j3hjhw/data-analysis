# Data Analysis

This repository contains a demographic dataset and a helper script to clean it.

## Files

- `demographic.csv` - Raw demographic information.
- `scripts/clean_demographic.py` - Utility for cleaning the dataset.
- `demographic_clean.csv` - Output produced by the cleaning script.

## Usage

Run the cleaning script to generate a cleaned version of the CSV:

```bash
python3 scripts/clean_demographic.py demographic.csv demographic_clean.csv
```

The script removes Windows carriage returns, replaces line breaks inside fields
with spaces, drops duplicate `USERID` records and replaces `unknown` values with
blanks.

## Analysis

To see a quick summary of gender and age distribution in the cleaned dataset run:

```bash
python3 scripts/analyze_demographic.py demographic_clean.csv
```
