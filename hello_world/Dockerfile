FROM python:3.6-alpine
RUN apk update && apk upgrade && apk add git

# ephemeral working directory
ENV SCRATCH=/mnt/ephemeral-01
WORKDIR ${SCRATCH}
RUN chmod a+rwx ${SCRATCH} && chmod g+rwxs ${SCRATCH}

# add reactor assets from repo
ADD requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
ADD reactor.py /
ADD config.yml /
ADD schemas /

# uninstall legacy Reactors SDK and install most recent version
#RUN pip uninstall reactors && \
    #rm -rf /reactors

RUN pip install ipython requests_futures git+https://github.com/TACC-Cloud/python-reactors.git@develop
CMD ["python3", "/reactor.py"]
