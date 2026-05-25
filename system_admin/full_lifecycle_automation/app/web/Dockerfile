ARG PY_BASE_IMAGE=python:3.11-slim
FROM ${PY_BASE_IMAGE}

WORKDIR /app
COPY app.py /app/app.py
RUN useradd --no-log-init --create-home --shell /usr/sbin/nologin appuser \
    && mkdir -p /data \
    && chown -R appuser:appuser /app /data \
    && chmod 0644 /app/app.py
USER appuser

EXPOSE 8080
CMD ["python", "/app/app.py"]
