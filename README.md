# Simple Micro Service app

The application is really simple : one Python app, one redis server, every time user reaches the "/" URL, a counter is incremented in redis.

App listens on port 9876, and the configuration creates a load balancer service (tip: my K3s supports klipper-lb by default, so if you're deploying on K3s or on standard cloud providers, you should be fine - if not, change the service to a NodePort)

![Architecture](https://github.com/stratokumulus/simple-microservice/blob/main/simple-microservice.png)

