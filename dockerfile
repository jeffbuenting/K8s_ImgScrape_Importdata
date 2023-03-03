FROM python

# create src code directory
RUN mkdir =p /code
WORKDIR /code

COPY main.py /code

# run python script
# CMD ["python","-u","main.py"]
ENTRYPOINT ["tail", "-f", "/dev/null"]
