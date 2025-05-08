# Use Python 3.11 as the base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file (we'll create this next)
COPY requirements.txt .

# Install dependencies using uv
RUN pip install -r requirements.txt

# Copy application files
COPY main.py .
COPY ECFS-OPENAPI-Spec.yaml .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "main.py"] 