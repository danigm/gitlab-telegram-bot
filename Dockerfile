FROM python:3.7.2-alpine

ENV AUTHMSG "start"
ENV TOKEN "NNN:XXX"

COPY ./* /work/
WORKDIR /work

RUN pip install flask && \
    pip install requests &&\
    pip install ipdb

EXPOSE 10111
CMD echo ${AUTHMSG} > /work/authmsg && echo ${TOKEN} > /work/token && python app.py