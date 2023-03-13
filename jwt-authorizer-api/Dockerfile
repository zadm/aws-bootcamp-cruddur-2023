FROM node:16.18 AS base
COPY . /app

FROM base AS app
WORKDIR /app
RUN npm install

FROM app As Prod
CMD ["npm", "start"]