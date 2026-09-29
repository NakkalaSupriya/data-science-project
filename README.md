# Data Science Runnable Project

A beginner-friendly Python data analysis project that reads CSV sales data and calculates summary statistics and a simple sales-to-marketing-spend ratio.

## Requirements

- Python 3.10+
- VS Code
- Node.js/npm are NOT required

## Run in VS Code

Open this folder in VS Code, then open Terminal and run:

```cmd
python --version
python app.py
```

Or on Windows, double-click `run_project.bat`.

## Optional virtual environment

```cmd
python -m venv venv
venv\Scripts\activate
python app.py
```

## Expected result

The program reads `data/sales_data.csv` and displays:
- number of records
- total sales
- total marketing spend
- total customers
- average sales
- best month
- monthly sales/marketing ratio

## Important

Do NOT run `npm install` in this project. It is a Python project and intentionally has no `package.json`.
