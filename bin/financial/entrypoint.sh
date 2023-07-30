#!/bin/bash

# Get latest stock data and insert to database
python get_raw_data.py

# Start API service
uvicorn financial.main:app --host 0.0.0.0 --port 5000 --reload
