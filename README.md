# Earnings Drift Analysis

## Overview
A financial data analysis project that builds an ETL pipeline to extract, process, and store historical earnings and stock price data before analyzing post-earnings price drift using Python, SQL, and data visualization.

## Tech Stack
- Python
- SQL
- MySQL
- SQLAlchemy
- Pandas
- Matplotlib
- yfinance

## Pipeline
User-Selected Tickers → yfinance → Python ETL → MySQL → SQL Analysis → Matplotlib Visualization

## Features
- Extracts historical earnings and stock price data using the yfinance API
- Processes and stores financial data in Pandas dataframes and a relational MySQL database
- Analyzes stock price changes within a ±3-day earnings window using Python and SQL
- Visualizes post-earnings price drift with Matplotlib dumbbell charts to support data-driven insights

## Repository Structure
- data_collection.py
- database.py
- etl_sql.py
- analysis.py
- visualization.py
- tables.sql
- analysis_query.sql