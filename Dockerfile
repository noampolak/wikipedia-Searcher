FROM python:3.10 as requirementsexporter

WORKDIR /app
ENV PATH="/root/.local/bin:$PATH"

# CREATE VENV AND INSTALL DEPEENDENCIES
RUN python -m venv --copies /app/venv
COPY requirements.txt requirements.txt
RUN . /app/venv/bin/activate && pip install -r requirements.txt

FROM python:3.10 as final_image

COPY ./app /app/
COPY --from=requirementsexporter /app/venv /app/venv/
ENV PATH /app/venv/bin:$PATH
ENV PYTHONPATH "${PYTHONPATH}:/"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
