FROM continuumio/miniconda:4.7.12-alpine
USER root
RUN apk update && apk upgrade && apk add git
ENV PATH="/opt/conda/bin:${PATH}"
RUN conda install -y python=3.6

# ephemeral working directory
ENV SCRATCH=/mnt/ephemeral-01
WORKDIR ${SCRATCH}
RUN chmod a+rwx ${SCRATCH} && chmod g+rwxs ${SCRATCH}

# add reactor assets from repo
ADD requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt
ADD reactor.py /
ADD config.yml /
ADD context_schemas /
ADD message_schemas /

CMD ["python3", "/reactor.py"]
