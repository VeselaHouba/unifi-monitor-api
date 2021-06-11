FROM python:3
RUN pip3 install unifi-video
COPY monitor.py /
ENTRYPOINT ["/usr/local/bin/python3","/monitor.py"]
