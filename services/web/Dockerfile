ARG PY_BASE_IMAGE=python:3.11-slim
FROM ${PY_BASE_IMAGE}
WORKDIR /app
RUN groupadd -r appuser && useradd --no-log-init -r -g appuser appuser
COPY --chown=appuser:appuser app.py /app/app.py
RUN chmod 0644 /app/app.py
USER appuser
EXPOSE 5000
CMD ["python", "/app/app.py"]
