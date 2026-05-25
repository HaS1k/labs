ARG PY_BASE_IMAGE=python:3.11-slim
FROM ${PY_BASE_IMAGE}
WORKDIR /app
RUN groupadd -r dbuser && useradd --no-log-init -r -g dbuser dbuser && mkdir -p /data && chown -R dbuser:dbuser /data
COPY --chown=dbuser:dbuser db.py /app/db.py
RUN chmod 0644 /app/db.py
USER dbuser
EXPOSE 7000
CMD ["python", "/app/db.py"]
