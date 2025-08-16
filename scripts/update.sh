#!/bin/sh
set -e

cd /home/kafin/car-price-prediction
echo "Updating code..."
git fetch origin
git reset --hard origin/main

echo "Building image and Deploying with rolling update..."
docker compose -f docker-compose.yml up -d --no-deps --build

echo "Deployment successful!"