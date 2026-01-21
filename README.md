# Log File Analyzer (CLI)

## Overview
Log File Analyzer is a command-line Python application that reads and analyzes application log files.  
The project is designed to demonstrate clean Python structure, modular functions, and incremental Git commits for learning and portfolio purposes.

## Features
- Load log data from a text file
- Parse structured log entries
- Filter logs by severity level
- Filter logs by date
- Count log occurrences by level
- Display summary statistics
- Export filtered results to a file

## Project Structure
log_file_analyzer/
│
├── main.py # Entry point for the CLI
├── file_loader.py # Load log files
├── log_parser.py # Parse raw log lines
├── log_filter.py # Filter logs by rules
├── log_stats.py # Generate statistics
├── exporter.py # Export results
└── README.md
