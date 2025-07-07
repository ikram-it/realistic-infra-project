# Use a slim Python image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]