#!/bin/bash

# Set Python path
export PYTHONPATH=$PYTHONPATH:/backend/api_folder/

# Run uvicorn in the background
uvicorn backend.api_folder.api_file:api --host 0.0.0.0 --port 8123 &

# Run Streamlit
streamlit run --server.enableCORS true /frontend/app.py --server.port $PORT --server.address 0.0.0.0
