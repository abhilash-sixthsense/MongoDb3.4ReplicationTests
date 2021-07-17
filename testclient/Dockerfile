FROM python:3.9.6-alpine3.14

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# copy the code here
# create venv
COPY requirements.txt /app/
COPY test.py /app/

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "test.py"]


# Reference https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
