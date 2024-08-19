FROM python:3.12-alpine

WORKDIR /app

# Using example from https://github.com/rycus86/prometheus_flask_exporter/tree/master/examples/gunicorn
ENV METRICS_PORT 9200
ENV PROMETHEUS_MULTIPROC_DIR /tmp

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt
# Install unicorn
RUN pip install uvicorn

# copy every content from the local file to the image
COPY . /app

# configure the container to run uvicorn with our Flask application
ENTRYPOINT [ "uvicorn" ]
CMD ["--host", "0.0.0.0", "--port", "8080", "main:app"]