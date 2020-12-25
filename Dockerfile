FROM node:current-slim

WORKDIR /usr/src/taacops

COPY package.json .
RUN npm init --yes && \
  npm install

CMD ["npx", "honkit", "build", "src", "docs"]
