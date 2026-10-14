FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src

WORKDIR /app

# Run as an unprivileged user (least privilege)
RUN useradd --create-home appuser

COPY src/ ./src/
USER appuser

CMD ["python", "-m", "infra_inventory.cli"]