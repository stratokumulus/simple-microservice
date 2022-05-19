from flask import Flask, request, Response, stream_with_context, jsonify
import redis
import os, time, json

app = Flask(__name__)
try:
    db_host = os.environ['DB_HOSTNAME']
    db_port = os.environ['DB_PORT']
except:
    print ('Using default Redis configuration')
    db_host = 'redis-svc'
    db_port = 6379

db = redis.Redis(host=db_host, port=db_port)

@app.route('/')
def hello():
    db.incr('count')
    return 'Count is %s.' % db.get('count')
    
if __name__ == "__main__":
    print ('Starting. Redis server configured at %s:%s' % (db_host, db_port))
    app.run (host="0.0.0.0", port=9876, debug=True)
