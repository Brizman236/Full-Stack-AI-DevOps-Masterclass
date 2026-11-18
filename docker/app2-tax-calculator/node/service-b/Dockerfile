FROM node:26-alpine

WORKDIR /app

COPY package.json ./

RUN npm install

RUN addgroup -S nodejs && adduser -S nodejs -G nodejs

COPY --chown=nodejs:nodejs . .

EXPOSE 4000

USER nodejs

CMD [ "node", "index.js" ]