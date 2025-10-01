# ------------------- Use official Python image -------------------
FROM python:3.10-slim

# ------------------- Set working directory -------------------
WORKDIR /app

# ------------------- Copy requirements file -------------------
# (Create requirements.txt with all needed packages)
COPY requirements.txt .

# ------------------- Install dependencies -------------------
RUN pip install --no-cache-dir -r requirements.txt

# ------------------- Copy app files -------------------
COPY . .

# ------------------- Expose Streamlit default port -------------------
EXPOSE 8501

# ------------------- Set environment variables for Streamlit -------------------
ENV STREAMLIT_SERVER_ENABLECORS=false
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_PORT=8501

# ------------------- Run Streamlit app -------------------
CMD ["streamlit", "run", "app.py"]

