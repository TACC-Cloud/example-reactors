# Sentiment Analysis

Here's a quick demo to show that you can do real work with Reactors. This
reactor uses [textblob 0.15.0](https://pypi.python.org/pypi/textblob/0.15.0) 
to perform sentiment analysis on text you send to it. 

## Deploy

1. Edit `DOCKER_HUB_ORG` in `reactor.rc`
2. Run `abaco deploy` and note the Actor ID it gives you.

*Example response*

```Successfully deployed Actor with ID: vxB1Jxy1aL7BQ```

## Test

```shell
$ abaco run -m "Rendering all of its materials with a self-protective tongue-in-cheek tone, Star Wars is fun. But if the movie appeals to the child in all of us, it also may seem to the adult within a good deal less delightful. There is something depressing about seeing all these impressive cinematic gifts and all this extraordinary technological skills lavished on such puerile materials." vxB1Jxy1aL7BQ

xZvrDolDWzyvr

$ abaco run -m "Lucas combines excellent comedy and drama and progresses it with exciting action on tremendously effective space battles. Likeable heroes on noble missions and despicable villains capable of the most dastardly deeds are all wrapped up in some of the most spectacular special effects ever to illuminate a motion picture screen. The result is spellbinding and totally captivating on all levels." vxbjlqDmZGKlb

J3ol7bYmAD80y
```

## View logs

This is the simplest way to see the result

```shell
$ abaco logs vxB1Jxy1aL7BQ xZvrDolDWzyvr
Logs for execution xZvrDolDWzyvr:
[INFO] 2018-01-10T00:38:08Z: Polarity: 0.266666666667
[INFO] 2018-01-10T00:38:08Z: Subjectivity: 0.576666666667

$ abaco logs vxB1Jxy1aL7BQ J3ol7bYmAD80y
Logs for execution J3ol7bYmAD80y:
[INFO] 2018-01-10T00:45:10Z: Polarity: 0.477922077922
[INFO] 2018-01-10T00:45:10Z: Subjectivity: 0.679220779221
```
