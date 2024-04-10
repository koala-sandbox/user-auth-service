import os
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics

# Using example from https://github.com/rycus86/prometheus_flask_exporter/tree/master/examples/gunicorn

def when_ready(server):
    GunicornPrometheusMetrics.start_http_server_when_ready(int(os.getenv('METRICS_PORT')))


def child_exit(server, worker):
    GunicornPrometheusMetrics.mark_process_dead_on_child_exit(worker.pid)