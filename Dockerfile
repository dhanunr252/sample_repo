FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app
RUN pip3 install flask
EXPOSE 5002
CMD [ "python3", "flask_app.py" ] 