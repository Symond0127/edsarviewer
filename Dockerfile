#Use an official Python base image
FROM python:3.8-slim

#Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Set the working directory inside the container
WORKDIR /app

#Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

#Copy your Python script or app
COPY . /app/

#Run Django development server
CMD ["python3", "manage.py"]