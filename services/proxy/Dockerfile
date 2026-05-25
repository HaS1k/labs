ARG PY_BASE_IMAGE=python:3.11-slim
FROM ${PY_BASE_IMAGE}
WORKDIR /app
RUN groupadd -r proxyuser && useradd --no-log-init -r -g proxyuser proxyuser
COPY --chown=proxyuser:proxyuser proxy.py /app/proxy.py
RUN chmod 0644 /app/proxy.py
USER proxyuser
EXPOSE 8080
CMD ["python", "/app/proxy.py"]
