# Sales-Data-Analysis
**Sales Data Analysis &amp; Visualization Dashboard**   A beginner-friendly Python console application for reading, visualizing, manipulating, and analyzing sales data from a CSV file using Pandas and Matplotlib.

# Sales Data Analysis & Visualization Dashboard

A simple yet powerful Python console-based application for analyzing and visualizing sales data from a CSV file.  
Perfect for beginners learning Pandas, Matplotlib, and data manipulation/visualization in Python.

## Features

- 📂 Read CSV data in different ways (with/without index)
- 📊 Rich Data Visualizations:
  - Line Charts (single & multi-line)
  - Bar Charts (single, grouped, stacked)
  - Pie Charts (distribution by city)
  - Scatter Plots (multi-metric comparison)
- 🔍 Data Manipulation:
  - Sort data by any column
  - View top/bottom N records
  - Create backup/copy of CSV
  - Add new city sales record
  - Search records by city name
- 📈 Statistical Summary:
  - Count, Sum, Mean, Max, Min, Median

## Technologies Used

- Python 3.8+
- pandas
- matplotlib
- numpy

## Project Structure
sales-analysis/
├── sales.csv               # Your main data file (must exist)
├── sales_copy.csv          # Created when you use option 9
├── main.py                 # Main program file (rename your script to this)
└── README.md
 Prerequisites

Make sure you have these Python packages installed:

```bash
pip install pandas matplotlib numpy
