FROM python:3.10
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt
COPY sql-injection-demo/hr.db ./
COPY sql-injection-demo/main.py ./
RUN groupadd -r pyuser && useradd -r -g pyuser pyuser
USER pyuser
EXPOSE 8080
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
