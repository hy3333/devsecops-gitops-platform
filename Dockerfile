FROM python:3.11-slim

ENV HOME=/code
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY app/requirements.txt /code/requirements.txt

RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir -r /code/requirements.txt && \
    python -m pip uninstall --yes setuptools wheel && \
    addgroup --system app && \
    adduser --system --ingroup app app && \
    chown app:app /code

COPY --chown=app:app app /code/app

USER app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
