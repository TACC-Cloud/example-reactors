# Echo

This Reactor echos back the message you sent to it

## Deploy

Edit `DOCKER_HUB_ORG` in `reactor.rc` to reflect either your DockerHub 
username or organization you are authorized to push to. Then, deploy.

```shell
$ cd echo 
$ abaco deploy

Sending build context to Docker daemon  9.728kB
Step 1/1 : FROM sd2e/reactor-base:python2
# Executing 4 build triggers
 ---> Using cache
 ---> Using cache
 ---> 736f565dcb48
Successfully built 736f565dcb48
Successfully tagged mwvaughn/echo:0.1
The push refers to repository [docker.io/mwvaughn/echo]
d978b1d68494: Pushed 
...
8e0cabdd61e2: Pushed 
0.1: digest: sha256:1814fd0981d7ea853fbcc4503a0a34428f5bd06feb6df099d94a90d66f51305d size: 5311
Deployed Actor ID: JPYkAVO0EWe3X
```

## Test

```shell
$ abaco run -m "Testing 123" JPYkAVO0EWe3X
WBaVm4lZjQeDj
'Testing 123'

$ abaco logs JPYkAVO0EWe3X WBaVm4lZjQeDj

Logs for execution WBaVm4lZjQeDj:
Hello, world
```

## Test with JSON


```
$ abaco run -m '{"whistles": "Belgian"}' JPYkAVO0EWe3X
ZVYwAWLvbD3xw
{
  "whistles": "Belgian"
}

$ abaco logs JPYkAVO0EWe3X ZVYwAWLvbD3xw
Logs for execution ZVYwAWLvbD3xw:
{'whistles': 'Belgian'}
```

