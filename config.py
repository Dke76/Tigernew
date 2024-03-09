import os

API_ID = API_ID = 20319884

API_HASH = os.environ.get("API_HASH", "637e3ba6357aa3ba2f3bf5742e0fd066")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6896159439:AAF1T6wHZoVEpIUzNG8Z8gCSCrAy8zAlnxU")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1183124209))

LOG = -1002102423504

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1183124209",).split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


