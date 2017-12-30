FROM node
RUN mkdir /client
WORKDIR /client
ADD package.json /client/
RUN npm install
ADD . /client/
EXPOSE 4200
