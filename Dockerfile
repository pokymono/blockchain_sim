FROM python:3.9-slim

WORKDIR /app

# Copy the project files
COPY . .

# No additional dependencies needed since the project uses only standard libraries

# Set the entry point
CMD ["python", "main.py"]
