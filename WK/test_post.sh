#!/bin/sh

curl "https://api.wanikani.com/v2/reviews" \
  -X "POST" \
  -H "Wanikani-Revision: 20170710" \
  -H "Content-Type: application/json; charset=utf-8" \
  -H "Authorization: Bearer 48768d92-fc9b-4616-9e4a-4fde5318daab" \
  -d $'{
       "review": {
         "subject_id": 6767,
         "incorrect_meaning_answers": 0,
         "incorrect_reading_answers": 0
       }
     }'

