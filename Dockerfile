# Use the official Alpine Python image as the base
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
ADD requirements.txt /app/requirements.txt

# Install Python packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
ADD api_server.py /app/api_server.py

# Run the Flask application
ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "api_server:app"]