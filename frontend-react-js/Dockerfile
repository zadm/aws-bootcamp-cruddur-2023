FROM node:16.18 AS base
COPY . /frontend-react-js

FROM base AS app
WORKDIR /frontend-react-js
RUN npm install

FROM app As Prod
CMD ["./entrypoint.sh", "NODE"]