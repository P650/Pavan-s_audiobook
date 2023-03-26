# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install PyPDF2 pyttsx3

# Run the command to execute the script
CMD ["python", "pdf_to_audio.py"]