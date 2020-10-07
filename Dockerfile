FROM python:3.8-slim AS builder
WORKDIR /api

# install dependencies to the local user directory (eg. /root/.local)
RUN apt update -y && apt install -y libpq-dev gcc
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# copy files
COPY ./clinica .

# add entrypoint
COPY entrypoint.sh /usr/local/bin/entrypoint
RUN chmod +x /usr/local/bin/entrypoint

# update PATH environment variable
ENV PATH=/root/.local:$PATH

ENTRYPOINT ["entrypoint"]
CMD [ "python", "manage.py", "runserver", "0:8000" ]