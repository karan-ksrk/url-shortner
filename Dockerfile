FROM python:3.13.2-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="/app"

# Create and activate virtual environment
RUN python -m venv /opt/venv

# Ensure virtual environment is in the path
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install os dependencies for our mini vm
RUN apt-get update && apt-get install -y \
    # for postgres
    libpq-dev \
    # for Pillow
    libjpeg-dev \
    # for CairoSVG
    libcairo2 \
    # other
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set up the application directory
RUN mkdir -p /app/app
WORKDIR /app

# Copy the rest of the application code
COPY ./app /app/app

# Copy the requirements file and install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Expose port 8080
EXPOSE 8080

# Clean up unnecessary apt files to reduce image size
RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
