#!/bin/bash
set -e
openssl enc -aes-256-cbc -pbkdf2 -d -in .env.enc -out .env
echo "Keys ready. You're good to go."
