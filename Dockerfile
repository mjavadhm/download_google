FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
COPY download.py .

# --- مرحله عیب‌یابی ---
# این دستور محتویات پوشه /app را در لاگ ساخت چاپ می‌کند
RUN ls -l /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "download.py"]
