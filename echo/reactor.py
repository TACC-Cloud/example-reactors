import os
import sys

from reactors.runtime import Reactor
from reactors.version import version as reactors_version


def main():
    r = Reactor()

    r.logger.info("Actor received message: {}".format(r.context['raw_message']))
    r.logger.info(f"Using python-reactors version {reactors_version}")


if __name__ == '__main__':
    main()
