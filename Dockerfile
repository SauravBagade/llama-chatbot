FROM python:3.10-slim

#  Environment Settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#  Set Working Directory
WORKDIR /app

#  Install System Dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

#  Copy Requirements First
COPY requirements.txt .

#  Install Python Dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

#  Copy Project Files
COPY backend ./backend

#  Expose Port
EXPOSE 8000

#  Run FastAPI Ap
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
