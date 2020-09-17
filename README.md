# MTSCloud_TEST
uctl pkg add -l python boto3 -v 1.14.61

uctl fn set hello2 -e "key_id=key_id,access_key=access_key,bucket=bucket"

uctl fn code delete hello2 
uctl fn code add hello2 main -s list.py -l python

uctl fn logs show hello2
