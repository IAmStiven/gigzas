FROM python:3.10 as py

FROM py as build

COPY requirements.txt /
RUN pip install --prefix=/inst -U -r /requirements.txt

FROM py

ENV USING_DOCKER yes
COPY --from=build /inst /usr/local

WORKDIR /rogoldultimate
COPY . /rogoldultimate
CMD gunicorn -b 0.0.0.0:3000 main:app
#CMD python main.py
