# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 8080

# Start the API
CMD ["python", "agent/api.py"]
