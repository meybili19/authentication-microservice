# Use a Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files to the container image
COPY . /app

# Install system dependencies required for MySQL
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libmysqlclient-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which Flask will run
EXPOSE 5000

# Set the default command to run the application
CMD ["python", "app.py"]
