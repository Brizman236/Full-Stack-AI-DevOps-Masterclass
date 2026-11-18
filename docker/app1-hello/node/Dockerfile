FROM node:26-alpine

WORKDIR /app

COPY package.json .

RUN npm install

RUN addgroup -S nodejs && adduser -S nodejs -G nodejs

COPY --chown=nodejs:nodejs . /app/

USER nodejs

CMD [ "node", "app.js" ]