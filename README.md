# unifi-monitor-api
# Base info

Minimalistic docker image for monitoring unifi NVR. All credits go to author of this awesome API:
https://github.com/yuppity/unifi-video-api

## Usage

```
docker run --rm veselahouba/unifi-monitor-api --server HOST --apikey API_KEY [--port 7080] [--schema=http]
```
Example output:

Exit code `0`
```
All cameras active. Stats for last 24h
{'name': 'camera1', 'recordings': 85, 'state': 'CONNECTED'}
{'name': 'camera2', 'recordings': 624, 'state': 'CONNECTED'}
{'name': 'camera3', 'recordings': 86, 'state': 'CONNECTED'}
{'name': 'camera4', 'recordings': 397, 'state': 'CONNECTED'}
```

Exit code `1`

```
Following cameras have triggered alarm
{'name': 'camera1', 'recordings': 4, 'state': 'CONNECTED'}
{'name': 'camera2', 'recordings': 6, 'state': 'CONNECTED'}
```

```
Following cameras have triggered alarm
{'name': 'camera3', 'state': 'DISCONNECTED', 'recordings': 0}
```

## Notes

All pull requests with fixes and features are very welcomed.
