import os
from flask import Flask
#from prometheus_client import make_wsgi_app, Counter
#from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)
#REQUEST_COUNT = Counter('request_count', 'App Request Count')

@app.route('/')
def hello():
    #REQUEST_COUNT.inc()
    return "Hi there from Flask!"

## Create a metrics endpoint
#metrics_app = make_wsgi_app()

## Combine the Flask app and the metrics endpoint
#app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
#    '/metrics': metrics_app
#})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Use OpenShift's port
    app.run(host="0.0.0.0", port=port)

