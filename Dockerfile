ARG BASE_IMAGE=public.ecr.aws/docker/library/python:3.11-slim

FROM ${BASE_IMAGE}

WORKDIR /app

# Prevent bytecode (.pyc ) from being written to disk during build. 
# This helps reduce the final image size.
ENV PYTHONDONTWRITEBYTECODE 1

# Turn off buffering for better logging.
ENV PYTHONUNBUFFERED 1

# Copy requirements.txt file into the image so we can install the 
# source code dependencies. 
COPY requirements.txt .

# Install source code dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Add source code
COPY source .

# Set non-root user. 
RUN addgroup --system ebb && adduser --system --group ebb
USER ebb

EXPOSE 8000

CMD ["uvicorn", "app.app.main:app", "--host", "0.0.0.0", "--port", "8000"]