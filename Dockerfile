# Use Python lightweight base image
FROM python:3.9-slim

# Create working directory inside container
WORKDIR /app

# Copy requirements first (for faster caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy entire project
COPY . .

# Expose Flask port
EXPOSE 5000

# Run application.py as main entrypoint
CMD ["python", "application.py"]
