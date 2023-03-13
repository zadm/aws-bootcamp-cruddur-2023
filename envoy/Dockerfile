FROM envoyproxy/envoy:v1.25.1

RUN apt-get update && apt-get -q install -y \
    curl

COPY envoy.yaml /etc/front-envoy.yaml
# COPY front-envoy.yaml /etc/front-envoy.yaml
RUN chmod go+r /etc/front-envoy.yaml
CMD ["/usr/local/bin/envoy", "-c", "/etc/front-envoy.yaml", "-l", "trace" ,"--service-cluster", "front-proxy"]