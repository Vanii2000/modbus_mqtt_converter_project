FROM python:3.11-slim

COPY requirements.txt .
RUN pip uninstall -y pymodbus || true
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .
CMD ["python", "server.py"]
