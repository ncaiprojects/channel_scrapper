FROM ubuntu:latest
RUN apt-get update --fix-missing
RUN apt-get install -y python3 python3-pip
RUN pip3 install requests
RUN pip3 install bs4
RUN pip3 install lxml
RUN pip3 install pymongo
WORKDIR /home
COPY ./scrapper.py ./scrapper.py
RUN chmod 777 ./scrapper.py
CMD [ "bash" ]