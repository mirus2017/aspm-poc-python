FROM python:2
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt
COPY app.py ./
COPY .vipaccess-isetm2m ./
RUN groupadd -r pyuser && useradd -r -g pyuser pyuser
USER pyuser
ENV FLASK_ENV=development
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080
EXPOSE 8080
CMD [ "flask", "run" ]