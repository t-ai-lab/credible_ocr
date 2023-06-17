FROM korekontrol/ubuntu-java-python3

EXPOSE 8000
WORKDIR /code

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

COPY . /code
RUN mkdir -p /code/pdfs

RUN pip install --upgrade pip
RUN pip install --default-timeout=2000 --upgrade -r /code/requirements.txt

RUN apt-get update
RUN apt-get install -y ghostscript python3-tk

ENTRYPOINT ["python3"]
CMD ["pkb_fast_api.py"]
