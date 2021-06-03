#!/usr/local/bin/python3
import argparse
from unifi_video import UnifiVideoAPI
from datetime import datetime, timedelta

recordings_delta_hours = 24
recordings_expected = 10
parser = argparse.ArgumentParser()
parser.add_argument('--server', help='IP/Hostname of server', required=True)
parser.add_argument('--apikey', help='API Key', required=True)
parser.add_argument('--port', help='Port to connect to', default=7080)
parser.add_argument('--schema', help='http/https', default="http")

args = parser.parse_args()
uva = UnifiVideoAPI(
    api_key=args.apikey,
    addr=args.server,
    port=args.port,
    schema=args.schema
)

failed = []
stats = []
active = uva.active_cameras
now = datetime.today()
delta = now - timedelta(hours=recordings_delta_hours)

for camera in uva.cameras:
    if camera in active:
        recordings = uva.get_recordings(
            camera=camera,
            start_time=delta,
            end_time=now
        )
        recnum = len(list(recordings))
        stats.append({"name": camera.name,"recordings": recnum, "state": camera.state})
        if recnum < recordings_expected:
            failed.append({"name": camera.name,"recordings": recnum, "state": camera.state})
    else:
        failed.append({"name": camera.name, "state": camera.state, "recordings": 0})

if len(failed) > 0:
    print("Following cameras have triggered alarm")
    for cam in failed:
        print(cam)
    exit(1)
else:
    print("All cameras active. Stats for last "+str(recordings_delta_hours)+"h")
    for cam in stats:
        print(cam)
