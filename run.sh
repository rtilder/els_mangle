#!/bin/sh

CLOUDFLARE_API_EMAIL=${CLOUDFLARE_API_EMAIL:=''}
CLOUDFLARE_API_KEY=${CLOUDFLARE_API_KEY:=''}
ZONE_NAME='mozilla.org'
NOW=$(date +%s)
#START_TIME=$((${NOW} - 24 * 60 * 60))
START_TIME=$((${NOW} - 60 * 60))

logshare --api-key=${CLOUDFLARE_API_KEY} \
         --api-email=${CLOUDFLARE_API_EMAIL} \
         --zone-name=${ZONE_NAME} \
         --start-time=${START_TIME} \
         --count=-1 | ./els_mangle.py > output.csv


