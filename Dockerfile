FROM  nilssn8000213/open_alpr_python3:beta

WORKDIR /tmp/

ENV PORT_ENV 8000

COPY . .

RUN pip3 install -r requirements.txt


CMD  uvicorn main:app --host 0.0.0.0 --port $PORT_ENV