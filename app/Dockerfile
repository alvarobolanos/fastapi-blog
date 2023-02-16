FROM python:3.9-slim

# Set the working directory
WORKDIR /code

# Copy the application folder inside the container
COPY . ./app

# Install the requirements
RUN pip install -r ./app/requirements.txt

# Run the fastapi server
CMD ["uvicorn", "app.main:app","--host", "0.0.0.0", "--port", "8080"]