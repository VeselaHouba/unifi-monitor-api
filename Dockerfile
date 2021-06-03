FROM python:3
RUN pip3 install unifi-video
COPY runme.py /
ENTRYPOINT ["/usr/local/bin/python3","/runme.py"]
