import argparse, sys

parser=argparse.ArgumentParser()

parser.add_argument("--bar", help="Do the bar option")
parser.add_argument("--foo", help="Foo the program")

args=parser.parse_args()

def testfunc( testarg ):
    print(testarg)

if __name__ == "__main__":
    print(f"Args: {args}\nCommand Line: {sys.argv}\nfoo: {args.foo}")
    print(f"Dict format: {vars(args)}")


# create src code directory
RUN mkdir =p /code
WORKDIR /code

COPY requirements.txt /code
COPY main.py /code

RUN pip install -r requirements.txt

    # run python script
# CMD ["python","-u","main.py"]
ENTRYPOINT ["tail", "-f", "/dev/null"]