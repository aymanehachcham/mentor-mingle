# Use an official Python runtime as the parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

# Install required system dependencies
RUN pip3 install poetry

# Install Python dependencies using poetry
RUN poetry config virtualenvs.create false

RUN poetry install  --no-interaction \
                    --no-ansi \
                    --without docs

# Specify the command to run on container start
CMD ["python3", "main.py"]
