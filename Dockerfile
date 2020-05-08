FROM nvcr.io/nvidia/pytorch:20.03-py3

COPY . /code/
WORKDIR /code

RUN pip install pytest
RUN pip install -e .

ENTRYPOINT [ "pytest" ]
