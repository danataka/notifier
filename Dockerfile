FROM python:3.10

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

# 


COPY ./*.py /src/
COPY ./key.json /src/

# 


CMD ["python", "main.py"]