# we use an official Python runtime as a parent image
FROM python:3.12

# set the environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# set working directory inside the container
WORKDIR /app

# install system dependencies 
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# install python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of your project code into container
COPY . /app/

# expose port 8001 for the drf api
EXPOSE 8001

# run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
