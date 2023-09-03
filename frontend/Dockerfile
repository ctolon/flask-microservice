FROM python:3.10-bullseye
COPY requirements.txt /frontendapp/requirements.txt
WORKDIR /frontendapp
RUN pip install -r requirements.txt --no-cache-dir
COPY . /frontendapp
ENTRYPOINT ["python"]
CMD ["app.py"]