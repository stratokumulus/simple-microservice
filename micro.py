from flask import Flask, request, Response, stream_with_context, jsonify
from prometheus_client import make_wsgi_app, Counter, Histogram
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import redis
import os, time, json

app = Flask(__name__)

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

REQUEST_COUNT = Counter(
    'app_request_count',
    'Application Request Count',
    ['method', 'endpoint', 'http_status']
)

REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Application Request Latency',
    ['method', 'endpoint']
)

try:
    db_host = os.environ['DB_HOSTNAME']
    db_port = os.environ['DB_PORT']
    useless_secret = os.environ['DB_PASSWD']
except:
    print ('Using default Redis configuration')
    db_host = 'redis-svc'
    db_port = 6379
    useless_secret = 'thisIsNotUsedButIWantedToAddSecretsToMyKubernetesExample!'

db = redis.Redis(host=db_host, port=db_port)

@app.route('/')
def hello():
    db.incr('count')
    return 'Count is %s.' % db.get('count')
    
if __name__ == "__main__":
    print ('Starting. Redis server configured at %s:%s' % (db_host, db_port))
    app.run (host="0.0.0.0", port=9876, debug=True)
