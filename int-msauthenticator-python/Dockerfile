FROM python:3.10
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt
COPY webapi.py ./
COPY hotp.py ./
RUN groupadd -r pyuser && useradd -r -g pyuser pyuser
USER pyuser
EXPOSE 8080
CMD [ "uvicorn", "webapi:app", "--host", "0.0.0.0", "--port", "8080"]