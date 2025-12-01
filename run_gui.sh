#!/bin/bash
# Script to run the Streamlit GUI

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run Streamlit
streamlit run src/gui.py --server.port 8501 --server.address localhost

