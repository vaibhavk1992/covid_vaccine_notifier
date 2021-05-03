import requests
import datetime
import asyncio
import time
import aiohttp
import logging
from decouple import config
from constants import *
from datetime import date
from twilio.rest import Client

logging.getLogger().setLevel(logging.INFO)


async def notifier(body):
    """
    Message Carrier,Integrated with twillio
    :param body:
    :return:
    """
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = config('ACCOUNT_SID')
    auth_token = config('AUTH_TOKEN')
    senders = config('SENDER')
    receipient = config('RECIPIENT')
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=body,
                         from_=senders,
                         to=receipient
                     )

    print(message.sid)


async def fetchnextdates():
    """
    To fetch all dates
    :return:
    """
    final_date_list=[]
    base = datetime.datetime.today()
    FUTURE_DAYS = int(config('FUTURE_DAYS'))
    # FUTURE_DAYS=os.getenv('')
    date_list = [base + datetime.timedelta(days=x) for x in range(FUTURE_DAYS)]
    for date in date_list:
        final_date_list.append(date.strftime("%d-%m-%Y"))
    return final_date_list


def create_msg_body(json_body):
    """
    To create msg body
    :param json_body:
    :return:
    """
    body="Hi, " \
        "We have found a {vaccine} for you at {name} Hospital. Slot avaliable are {slots}".\
        format(vaccine=json_body['vaccine'],name=json_body['name'],slots=json_body['slots'])
    return body


async def checkavaliablity(pincode):
    """
    To check API for all dates
    :param pincode:
    :return:
    """
    get_dates=await fetchnextdates()
    for dates in get_dates:
        get_url=FIND_BY_PIN.format(pincode=pincode,date=dates)
        print(get_url)
        age = int(config('AGE'))
        response = requests.get(get_url)
        try:
            for json_body in response.json()['sessions']:

                if json_body['min_age_limit']>=age and json_body['available_capacity']>0:
                    body=create_msg_body(json_body)
                    await notifier(body)
        except Exception as e:
            logging.info(e)


def call_initiate():
    """
    To initiate call
    :return:
    """
    pincode = config('PINCODE')
    asyncio.run(checkavaliablity(pincode))
