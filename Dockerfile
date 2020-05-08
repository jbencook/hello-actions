FROM python:3.7

COPY . /code/
WORKDIR /code
RUN pip install pytest

CMD [ "pytest" ]
