FROM python

# create src code directory
RUN mkdir =p /code
WORKDIR /code

COPY . /code

# run python script
CMD ["python","-u","main.py"]
