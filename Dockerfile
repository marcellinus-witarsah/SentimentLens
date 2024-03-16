# Get python Image
FROM python:3.10-slim

# Update system packages/libraries version and install AWS Command Line Interface

RUN apt update -y 
RUN apt install libpq-dev build-essential -y
RUN apt install awscli -y


# Select your working directory and copy all of the project folders into it
WORKDIR /app
COPY . .

# Install Python libraries for the project
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python3", "app.py"]