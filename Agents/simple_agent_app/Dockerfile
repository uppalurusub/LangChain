# ---------- Base builder image ----------
FROM python:3.11-slim AS builder

WORKDIR /app

# Install system deps needed for building wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt


# ---------- Final runtime image ----------
FROM python:3.11-slim

WORKDIR /app

# Minimal system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy built wheels from builder
COPY --from=builder /wheels /wheels
RUN pip install --no-cache /wheels/*

# Copy app code
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Streamlit config: run inside Docker
ENV STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_ENABLECORS=false \
    STREAMLIT_SERVER_PORT=8501

# (Optional) environment variable placeholder
# ENV OPENAI_API_KEY=""

CMD ["streamlit", "run", "app.py"]
