# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run uvicorn command to start the FastAPI app
# Note: The uvicorn command is specified in the docker-compose.yml, so it's commented out here
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]