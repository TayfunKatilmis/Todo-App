FROM python:3
# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project
COPY . /code/