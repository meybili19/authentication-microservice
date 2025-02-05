FROM python:3.9

# Set the working directory to /app
WORKDIR /app


# Copy the required files
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy the source code to the container
COPY . .

# Expose the port on which the application will run
EXPOSE 5004

# Command to run the application
CMD ["python", "-m", "src.app"]
