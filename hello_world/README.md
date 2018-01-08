# Simple Logger

Simple Abaco actor that logs the message it was sent

## Build and deploy

* Customize variables in `reactor.mk`. At minimum, you will need to set your own `DOCKER_HUB_ORG`
* Make sure you have an active Agave API client and associated `access_token`
* Customize `config.yml` based on the sample. We exlcude config.yml from source control now because it might have sensitive information in it. This will be solved with a combination of secrets escrow in the TACC Cloud and use of one ore more secrets.yml files that are maintained outside the source repo for your reactor. 

```
% auth-tokens-refresh -S
Token for sd2e:vaughn successfully refreshed and cached for 14400 seconds
8d9a5acfff1c4464c510b59c50268aaf

% make info
api: https://api.sd2e.org
token: 8d9a5446acfff1c4c510b59c50268aaf
image: mwvaughn/simple_logger:dev
reactor.name: logger
reactor.description: Logs the context, environment, and message
reactor.stateless: true
reactor.privledged: false

% make reactor
```

Note: The `make reactor` target creates an `ACTOR_ID` file. This is used by other targets upstream to link outputs to this Reactor. Eventually, we will have a service where one can register/update aliases for Reactors to aid with complex orhestrations. 

## Testing using Abaco CLI

View the newly-created Reactor:

```
% abaco list
simple_logger        JANXwYXKxDkG3  READY
slack_notify         NBaYgrNlLKrJy  READY
copydir_on_manifest  N55RjPNE1Q8ej  READY
```

## Send it a message

```
% abaco run -m '{"whistles": "Belgian"}' JANXwYXKxDkG3
ZVYwAWLvbD3xw
{
  "whistles": "Belgian"
}
```

## View Log
```
% abaco logs -e ZVYwAWLvbD3xw JANXwYXKxDkG3
Logs for execution ZVYwAWLvbD3xw:
Contents of MSG: {'whistles': 'Belgian'}
Environment:
HOSTNAME=ee45d717744d
SHLVL=1
HOME=/
_abaco_actor_id=JANXwYXKxDkG3
_abaco_access_token=636e32376d3524f2e452c12c6abf3fe
_abaco_api_server=https://api.sd2e.org
_abaco_actor_dbid=SD2E_JANXwYXKxDkG3
MSG={'whistles': 'Belgian'}
_abaco_execution_id=ZVYwAWLvbD3xw
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
_abaco_Content_Type=application/json
PWD=/
_abaco_jwt_header_name=X-Jwt-Assertion-Sd2E
_abaco_username=sd2eadm
_abaco_actor_state={}
```
