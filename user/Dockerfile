FROM python:3.10-bullseye
COPY requirements.txt /userapp/requirements.txt
WORKDIR /userapp
RUN pip install -r requirements.txt --no-cache-dir
COPY . /userapp
ENTRYPOINT ["python"]
CMD ["app.py"]