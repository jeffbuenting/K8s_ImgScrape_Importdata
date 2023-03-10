FROM python

# create src code directory
RUN mkdir =p /code
WORKDIR /code

COPY requirements.txt /code
COPY main.py /code

# test file
COPY input.csv /code

RUN pip install -r requirements.txt
