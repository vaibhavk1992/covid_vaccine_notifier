# Covid-vaccination-notifier
Service to track COVID-19 vaccine availability in India.

# Requirements
- Python 3+

# Usage

This service fetches the latest Covid Vaccinations Sessions data from [Cowin API](https://apisetu.gov.in/public/api/cowin) and sends it to the provided phone number provided via an SMS (Twilio messaging API).

## Setup
1. Clone the repository
```
git clone https://github.com/vaibhavk1992/covid_vaccine_notifier.git
```
2. Install 
```
pip install -r requirement.txt
```

3. Setup Twilio API Access (Trial Account)
References: https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account

4. Create `.env` file and setup ENV Vars.

| Name   |      Description      |  Remarks |
|:---------|:-------------:|:-----|
| ACCOUNT_SID |  TWILIO ACCOUNT SID (Available on Twilio Dashboard) | |
|AUTH_TOKEN |    TWILIO AUTH TOKEN  (Available on Twilio Dashboard)   |   |
|RECIPIENT | Personal mobile number used for verificiation while creating an account with Twilio |    When you signed up for your trial account, you verified your personal phone number. You can see your list of verified phone numbers on the Verified Caller IDs page. You must verify any non-Twilio phone numbers you wish to send SMS messages or MMS messages, or place phone calls to while in trial mode. This is an extra security measure for trial accounts. You may verify as many phone numbers as you like. |
| SENDER | Twilio phone number — a phone number purchased through Twilio — to send messages or make phone calls using Twilio. | https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account#get-your-first-twilio-phone-number |
| FUTURE_DAYS | Nums of days for vaccine forecast availiablity |    Nums of days for vaccine forecast availiablity|
| PINCODE | Area Pincode |    |
| AGE | Age of the beneficiary  |   |

5. Run the Service
```
python availability_scheduler.py
```

# Contributing

1. Fork the repo on GitHub
2. Clone the project to your own machine
3. Commit changes to your own branch
4. Push your work back up to your fork
5. Submit a Pull request so that we can review your changes
