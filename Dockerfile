FROM  nilssn8000213/open_alpr_python3:rasbperry

WORKDIR /tmp/

ENV PORT_ENV=8000 LC_ALL=C.UTF-8 LANG=C.UTF-8

COPY . .

RUN pip3 install -r requirements.txt

CMD uvicorn main:app --host 0.0.0.0 --port $PORT_ENV