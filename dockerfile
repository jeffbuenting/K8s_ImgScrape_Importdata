FROM python

# create src code directory
RUN mkdir =p /code
WORKDIR /code

COPY requirements.txt /code
COPY main.py /code

# test file
COPY c:\temp\input.csv /code

RUN pip install -r requirements.txt

# run python script
# CMD ["python","-u","main.py","--inputfile ~/test.csv","--broker 192.168.1.126","--port 8000"]
# CMD ["python","-u","main.py --inputfile ~/test.csv"]
CMD ["python","-u","main.py --inputfile ${inputfile}"]

