FROM nvidia/cuda:10.0-base

# COPY . /code/
# WORKDIR /code
# RUN pip install pytest

CMD [ "nvidia-smi" ]
