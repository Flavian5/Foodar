FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
ADD FoodRadar-b3096cb6092d.json /app/FoodRadar-b3096cb6092d.json
WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
