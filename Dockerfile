# Use Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy application files into the container
COPY app.py /app
COPY requirements.txt /app

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose port 8080 (default for OpenShift)
EXPOSE 8080

# Start Flask app
CMD ["python", "app.py"]
