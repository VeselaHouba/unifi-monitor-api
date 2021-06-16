#!/usr/local/bin/python3
import argparse
from unifi_video import UnifiVideoAPI
from datetime import datetime, timedelta

parser = argparse.ArgumentParser()
parser.add_argument('--server', help='IP/Hostname of server', required=True)
parser.add_argument('--apikey', help='API Key', required=True)
parser.add_argument('--port', help='Port to connect to', default=7080)
parser.add_argument('--schema', help='http/https', default="http")
parser.add_argument('--expected', help='Expected number of recordings', default=10)
parser.add_argument('--timespan', help='Search in last X hours of recordings', default=24)
parser.add_argument('--managed', help='Check only managed cameras', action="store_true")

args = parser.parse_args()
uva = UnifiVideoAPI(
    api_key=args.apikey,
    addr=args.server,
    port=args.port,
    schema=args.schema
)

recordings_delta_hours = int(args.timespan)
recordings_expected = int(args.expected)

failed = []
stats = []
if args.managed:
  cams = uva.managed_cameras
else:
  cams = uva.cameras
active = uva.active_cameras
now = datetime.today()
delta = now - timedelta(hours=recordings_delta_hours)

for camera in cams:
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
    exit(2)
else:
    print("All cameras active. Stats for last "+str(recordings_delta_hours)+"h")
    for cam in stats:
        print(cam)
