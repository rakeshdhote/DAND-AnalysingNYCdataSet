#! /bin/bash

cat turnstile_data_master_with_weather.csv | python mapper.py  | sort | python reducer.py > data.txt
