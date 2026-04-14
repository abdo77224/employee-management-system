FROM python:3.12-slim

WORKDIR /app

# Create non-root user
RUN useradd --create-home --shell /bin/bash appuser

# System dependencies (important for Django builds)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Permissions fix
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

# Django run server (DEV mode)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]