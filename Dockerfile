# Get python Image
FROM python:3.10-slim-buster

# Update system packages/libraries version and install AWS Command Line Interface
RUN apt update -y && apt install awscli -y

# Select your working directory and copy all of the project folders into it
WORKDIR /app
COPY . /app

# Install Python libraries for the project
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]