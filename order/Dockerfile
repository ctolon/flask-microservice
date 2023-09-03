FROM python:3.10-bullseye
COPY requirements.txt /orderapp/requirements.txt
WORKDIR /orderapp
RUN pip install -r requirements.txt --no-cache-dir
COPY . /orderapp
ENTRYPOINT ["python"]
CMD ["app.py"]