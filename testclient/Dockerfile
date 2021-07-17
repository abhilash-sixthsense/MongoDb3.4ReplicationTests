FROM python:3.9.6-alpine3.14

# copy the code here
# create venv
COPY . /app
WORKDIR /app
RUN python3.9 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
CMD source venv/bin/activate && python test.py
