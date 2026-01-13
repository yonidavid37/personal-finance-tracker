FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY PersonalFinanceTracker.py .
COPY finance-tracker/ ./finance-tracker/

COPY templates/ ./templates/
COPY static/ ./static/

EXPOSE 80

CMD ["python", "PersonalFinanceTracker.py"]

