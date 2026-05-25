ARG PY_BASE_IMAGE=python:3.11-slim
FROM ${PY_BASE_IMAGE}
WORKDIR /app
RUN groupadd -r cacheuser && useradd --no-log-init -r -g cacheuser cacheuser
COPY --chown=cacheuser:cacheuser cache.py /app/cache.py
RUN chmod 0644 /app/cache.py
USER cacheuser
EXPOSE 7001
CMD ["python", "/app/cache.py"]
