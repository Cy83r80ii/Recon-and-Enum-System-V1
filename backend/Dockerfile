FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    nmap \
    sqlmap \
    ruby \
    ruby-dev \
    build-essential \
    libcurl4-openssl-dev \
    libxml2 \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    unzip \
    golang \
    && rm -rf /var/lib/apt/lists/*

# Install WPScan
RUN gem install wpscan

# Install Nuclei using Go
RUN go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest \
    && mv /root/go/bin/nuclei /usr/local/bin/

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
