import sys
import reactors as Reactor
from textblob import TextBlob

def main():
    msgtext = Reactor.context.raw_message
    try:
        if msgtext is not None:
            tb = TextBlob(msgtext)
        sentiment = tb.sentiment
        Reactor.logger.info("Polarity: {}".format(sentiment.polarity))
        Reactor.logger.info("Subjectivity: {}".format(sentiment.subjectivity))
    except Exception as e:
        Reactor.logger.debug(e)
        sys.exit(1)

if __name__ == '__main__':
    main()
