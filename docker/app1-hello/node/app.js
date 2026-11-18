const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;
const ENV = process.env.ENV_VALUE || "No env set";
const HOSTNAME = process.env.HOSTNAME || require('os').hostname();
const APP_MESSAGE = process.env.APP_MESSAGE || 'No app message set'
const SECRET = process.env.SECRET || 'No app secret set'

app.get("/", (req, res) => {
  res.json({
    message: APP_MESSAGE,
    env: ENV,
    container: HOSTNAME,
    secret: SECRET
  });
});

app.listen(PORT, () => console.log(`Node Hello listening on ${PORT}`));
