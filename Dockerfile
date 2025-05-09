# Use Python 3.11 as the base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies using uv
RUN pip install -r requirements.txt

# Copy application files
COPY ECFS-OPENAPI-Spec.yaml .
COPY server.py .

# Set environment variables
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# Start the client in the foreground
CMD [ "python", "server.py" ]