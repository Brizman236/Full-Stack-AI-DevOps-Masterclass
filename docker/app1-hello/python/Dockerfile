FROM python:3-slim

WORKDIR /app

RUN addgroup --system appgroup  
RUN adduser --system --ingroup appgroup appuser

COPY --chown=appuser:appgrou . /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

USER appuser

CMD [ "python", "main.py" ]

