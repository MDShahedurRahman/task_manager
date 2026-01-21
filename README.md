# Log File Analyzer (CLI)

## Overview
Log File Analyzer is a command-line Python application that reads, parses, filters, and analyzes application log files.
The project focuses on clean Python structure, modular methods, and incremental Git commits for learning and portfolio development.

This project is intentionally built using only Python’s standard library to demonstrate core programming and backend-style log processing skills.

## Features
- Load log data from a text-based log file
- Parse structured log entries into Python objects
- Filter logs by severity level
- Filter logs by date
- Count logs by severity
- Generate summary statistics
- Export filtered results to a file

## Project Structure
```
log_file_analyzer/
│
├── main.py               # Application entry point
├── file_loader.py        # Load log files from disk
├── log_parser.py         # Parse raw log lines
├── log_filter.py         # Apply filtering rules
├── log_stats.py          # Generate statistics
├── exporter.py           # Export analysis results
└── README.md
```
