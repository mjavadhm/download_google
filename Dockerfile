FROM python:3.9-slim-buster

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies (this will now install gdown)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the download script into the container
COPY download.py .

# This is the command that will be executed when the container starts.
CMD ["python", "download.py"]
