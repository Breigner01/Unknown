FROM node:19.4.0-alpine3.17 AS builder

ARG REACT_APP_BACKEND_URL

WORKDIR /app

COPY package.json yarn.lock ./
RUN yarn install

COPY . .

RUN yarn build

FROM nginx:1.23.3-alpine

COPY --from=builder /app/build /usr/share/nginx/html
COPY config/nginx.conf /etc/nginx/conf.d/default.conf