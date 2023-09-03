FROM python:3.10-bullseye
COPY requirements.txt /bookapp/requirements.txt
WORKDIR /bookapp
RUN pip install -r requirements.txt --no-cache-dir
COPY . /bookapp
ENTRYPOINT ["python"]
CMD ["app.py"]