FROM python:3.9
RUN mkdir /code
ADD . /code/
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["/bin/sh"]
