FROM alpine:3.18

RUN apk add --no-cache curl bash

WORKDIR /app

COPY loop.sh .
RUN chmod +x loop.sh

ENV TARGET="http://server:8080" INTERVAL_SECONDS=3

CMD ["./loop.sh"]
