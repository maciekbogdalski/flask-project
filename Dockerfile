# Use the official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Heroku will use
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
