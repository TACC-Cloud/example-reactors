# Hello World

This actor says "Hello"

## Build and deploy

Edit `DOCKER_HUB_ORG` in `reactor.rc` to reflect either your DockerHub 
username or organization you are authorized to push to. Then, deploy.

````shell
$ cd echo 
$ abaco deploy

Sending build context to Docker daemon  9.728kB
Step 1/1 : FROM sd2e/reactor-base:python2
# Executing 4 build triggers
 ---> Using cache
 ---> Using cache
 ---> 736f565dcb48
Successfully built 736f565dcb48
Successfully tagged mwvaughn/hello_world:0.1
The push refers to repository [docker.io/mwvaughn/hello_world]
d978b1d68494: Pushed 
...
8e0cabdd61e2: Pushed 
0.1: digest: sha256:1814fd0981d7ea853fbcc4503a0a34428f5bd06feb6df099d94a90d66f51305d size: 5311
Deployed Actor ID: NBaYgrNlLKrJy
```

## Testing using Abaco CLI

View the newly-created Reactor:

```
% abaco list
hello_world          NBaYgrNlLKrJy  READY
...
```

## Send it a message

```
% abaco run -m "Test" JANXwYXKxDkG3
ZVYwAWLvbD3xw
'Test'
```

## View Log
```
% abaco logs -e JANXwYXKxDkG3 ZVYwAWLvbD3xw

Logs for execution ZVYwAWLvbD3xw:
Hello, world
```

Since we don't act on the message in `reactor.py` we just see the contents of `STDOUT`.
