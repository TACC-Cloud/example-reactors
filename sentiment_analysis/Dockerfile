FROM sd2e/reactor-base:python2

# Uncomment to activate experimental JSON schema support for
# Reactor messages
# ADD message.json /

RUN pip install textblob && \
    python -m textblob.download_corpora
