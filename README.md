# Example Reactors

Each of these can be deployed to the TACC Reactors service by editing the 
`reactor.rc` file to point to either your Docker Hub username or to a Docker
Hub organization where you have push rights.

Assuming you have installed and configured a TACC Cloud CLI and have con-
figured your local API client, you can use the Abaco CLI for deploying and
testing these examples.

## Deploy

Change into an example directory. Edit `DOCKER_HUB_ORG` in `reactor.rc` to 
reflect either your DockerHub username or organization you are authorized 
to push to. Then, deploy the Reactor. 

```shell
hello_world$ abaco deploy
Sending build context to Docker daemon  11.78kB
Step 1/1 : FROM sd2e/reactor-base:python2
# Executing 4 build triggers
 ---> Using cache
 ---> Using cache
 ---> Using cache
 ---> Using cache
 ---> e9b632fb503a
Successfully built e9b632fb503a
Successfully tagged mwvaughn/hello_world:0.1
The push refers to repository [docker.io/mwvaughn/hello_world]
5b9be63ba083: Layer already exists 
...
919b04a9917e: Layer already exists 
0.1: digest: sha256:518d4cbb5a3afdd4d4152950cc88a7032a12c1066614d5225afb22b0575c9e5b size: 5311
Deployed Actor ID: ZjaJQqE8W50JK
```

## Test

```shell
hello_world$ abaco run -m "Test" ZjaJQqE8W50JK
ZVlylG16GRLWw
'Test'
```

This value `ZVlylG16GRLWw` is the execution ID and it is unique. Check the
status and logs of an execution as follows:

```shell
abaco logs ZjaJQqE8W50JK ZVlylG16GRLWw
Logs for execution ZVlylG16GRLWw:
Hello, world
```

