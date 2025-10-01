# ------------------- Use official Python image -------------------
FROM python:3.10-slim

# ------------------- Set working directory -------------------
WORKDIR /app

# ------------------- Copy requirements file -------------------
COPY requirements.txt .

# ------------------- Install dependencies -------------------
RUN pip install --no-cache-dir -r requirements.txt

# ------------------- Copy app files -------------------
COPY . .

# ------------------- Expose Streamlit default port -------------------
EXPOSE 8080

# ------------------- Set environment variables for Streamlit -------------------
ENV STREAMLIT_SERVER_ENABLECORS=false
ENV STREAMLIT_SERVER_HEADLESS=true

# ------------------- Run Streamlit app -------------------
# Cloud Run sets $PORT automatically, so we bind to it
CMD ["sh", "-c", "streamlit run app.py --server.port=$PORT --server.headless=true --server.enableCORS=false"]
