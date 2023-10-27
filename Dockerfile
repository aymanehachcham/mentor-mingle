# Use an official Python runtime as the parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install required system dependencies
RUN pip install poetry

# Configure the virtual env to be created in the project directory
RUN poetry config virtualenvs.create true \
    && poetry config virtualenvs.in-project true

COPY pyproject.toml poetry.lock ./

RUN poetry install  --no-interaction \
                    --no-ansi \
                    --without docs \

# Modify PATH to use poetry's virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Copy the current directory contents into the container at /app
COPY . /app

# Update the PYTHON PATH
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

# Specify the command to run on container start
CMD ["python3", "main.py"]
