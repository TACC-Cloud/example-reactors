FROM sd2e/reactors:python3

# uninstall legacy Reactors SDK and install most recent version
RUN pip uninstall reactors && \
    rm -rf /reactors && \
    pip install git+https://github.com/TACC-Cloud/python-reactors.git@develop
