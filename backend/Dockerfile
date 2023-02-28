# Pull official python image
FROM python:3.11.2

# Set environment variable
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install --upgrade pip
COPY requirements/ .
RUN pip install -r requirements/prod.txt

# Copy the django project
# Here first dot(.) means current working dir.
# and second dot(.) means container working dir.
COPY . .
