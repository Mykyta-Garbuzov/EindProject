FROM python:3.11.0

WORKDIR /eindproject
RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN mkdir -p /eindproject/sqlitedb


COPY . .
EXPOSE 8000

# CMD [ "python", "main.py"]
# CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "8000"]
CMD ["uvicorn", "main:app", "--port", "8000"]