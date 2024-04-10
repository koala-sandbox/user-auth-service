FROM python:3.10-alpine

WORKDIR /app

# Using example from https://github.com/rycus86/prometheus_flask_exporter/tree/master/examples/gunicorn
ENV METRICS_PORT 9200
ENV PROMETHEUS_MULTIPROC_DIR /tmp
ENV prometheus_multiproc_dir /tmp

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt
# install gunicorn
RUN pip install gunicorn

# copy every content from the local file to the image
COPY . /app

# configure the container to run gunicorn with our Flask application
ENTRYPOINT [ "gunicorn" ]
CMD ["--workers", "3", "-c", "config.py", "--bind", "0.0.0.0:8080", "app:app"]

