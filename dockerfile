FROM python

# create src code directory
RUN mkdir =p /code
WORKDIR /code

COPY requirements.txt /code
COPY main.py /code

RUN pip install -r requirements.txt

# default env vars
ENV BROKERHOST ""
ENV PORT ""

ENTRYPOINT ["/bin/bash", "-c", "python -u main.py --inputfile $INPUTFILE --broker $BROKERHOST --port $PORT"]

