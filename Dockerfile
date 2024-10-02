# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local script to the container
COPY expr.py .

# Command to run the script
CMD ["python", "expr.py"]
