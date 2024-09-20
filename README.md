# Simple Micro Service app

The application is really simple : one Python app, one redis server, every time user reaches the "/" URL, a counter is incremented in redis.

App listens on port 9876, and the configuration creates a load balancer service.

Tip: my K3s supports klipper-lb by default, so a service type LoadBalancer works out of the box. If you're deploying this microservice app on a platform that supports load balancers (K3s, cloud providers, ...) you should be fine - if not, change the service to a NodePort.

![Architecture](https://github.com/stratokumulus/simple-microservice/blob/main/simple-microservice.png)

To build the code :

```bash
docker build --platform linux/amd64 -t <name>/<container-name>:<tag> .
docker push <name>/<container-name>:<tag>
```