# Gunakan image Python resmi
FROM python:3.10-slim

# Set direktori kerja dalam container
WORKDIR /app

# Salin requirements dan install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file ke dalam container
COPY . .

# Expose port yang digunakan Flask
EXPOSE 5000

# Jalankan API Flask
CMD ["python", "predict_api.py"]
