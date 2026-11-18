FROM node:26-alpine

WORKDIR /app

RUN addgroup -S nodejs && adduser -S nodejs -G nodejs && chown -R nodejs:nodejs /app

USER nodejs

COPY --chown=nodejs:nodejs package*.json ./

RUN npm install

COPY --chown=nodejs:nodejs . .

RUN npm run build

EXPOSE 5173

CMD [ "npm", "run", "dev" ]

