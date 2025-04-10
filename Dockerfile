# Use Python 3.10 slim image
FROM python:3.10-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Update system and install dependencies
RUN apt update -y && \
    apt install -y gcc && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory inside the container
WORKDIR /app

# Copy project files to the container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose port if using Flask or similar (optional)
# EXPOSE 5000

# Default command to run the app
CMD ["python3", "app.py"]
