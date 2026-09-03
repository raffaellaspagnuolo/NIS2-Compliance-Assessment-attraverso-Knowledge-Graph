# Immagine riproducibile dell'API; non include scanner o servizi esterni.
FROM python:3.12-slim
# Tutti i percorsi autorizzati dall'API rimangono sotto /app.
WORKDIR /app
# Copiamo prima i file di packaging per rendere riutilizzabile il layer di installazione.
COPY pyproject.toml README.md ./
# Il codice sorgente serve a costruire e installare il pacchetto Python.
COPY src ./src
# --no-cache-dir limita le dimensioni dell'immagine eliminando la cache di pip.
RUN pip install --no-cache-dir .
# Dataset e regole di esempio sono necessari per la dimostrazione locale.
COPY data ./data
# La cartella conterrà gli artefatti prodotti durante l'esecuzione del container.
COPY examples ./examples
RUN mkdir -p reports
EXPOSE 8000
CMD ["uvicorn", "nis2_assessor.main:app", "--host", "0.0.0.0", "--port", "8000"]
