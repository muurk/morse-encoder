#!/bin/bash

while getopts m: flag
do
    case "${flag}" in
        m)
          message=${OPTARG}
        ;;
    esac
done

export MESSAGE="${message}"

python3 /app/main.py
