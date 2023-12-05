#!/bin/bash

# Set Python path
export PYTHONPATH=$PYTHONPATH:/backend_repo/api_folder/

# Run uvicorn in the background
uvicorn backend_repo.api_folder.api_file:api --host 0.0.0.0 --port 8123 &

# Run Streamlit
streamlit run --server.enableCORS true /frontend_repo/app.py --server.port $PORT --server.address 0.0.0.0
