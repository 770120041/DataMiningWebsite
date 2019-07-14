# Pull base image
FROM python:3.7-slim

# Set environment varibles
# Next we create two environment variables. PYTHONUNBUFFERED ensures our console output looks familiar and is not buffered by Docker,
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code
COPY . /code/

# Install dependencies
RUN pip install -r requirements.txt

# Copy project
