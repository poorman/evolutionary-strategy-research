FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt /app/
RUN python -m venv /opt/venv \
    && . /opt/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy rest of the project
COPY . /app

# Activate venv
ENV PATH="/opt/venv/bin:$PATH"

# Default command
CMD ["python","src/app.py","--mode","evolve","--generations","50","--population","100"]