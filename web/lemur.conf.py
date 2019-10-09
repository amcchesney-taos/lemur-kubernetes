# This is just Python which means you can inherit and tweak settings

import os

_basedir = os.path.abspath(os.path.dirname(__file__))

ADMINS = frozenset([""])

THREADS_PER_PAGE = 8

# General

# These will need to be set to `True` if you are developing locally
CORS = False
debug = False

# this is the secret key used by flask session management
SECRET_KEY = os.getenv(
    "SECRET_KEY", "hvDtIoyjAHT/iiuOxmYbA1SGBZMa5+9sgllk08GVvXoSbQ0kJ9arlA=="
)

# You should consider storing these separately from your config
LEMUR_TOKEN_SECRET = os.getenv(
    "LEMUR_TOKEN_SECRET", "p1foIa7n5+nB1GnEpR4Wf2B2UgzUiBT1BHtB5WnTNoJSMVKhdXu1FA=="
)
LEMUR_ENCRYPTION_KEYS = os.getenv(
    "LEMUR_ENCRYPTION_KEYS", "yWdKiDFE_TAvoTx-E-Cn1sbbktAbmGwjbZGNBXshys4="
).split(";")

# this is a list of domains as regexes that only admins can issue
LEMUR_RESTRICTED_DOMAINS = []

ACTIVE_PROVIDERS = []
METRIC_PROVIDERS = []

# Mail Server

LEMUR_EMAIL = "lemur@example.com"
LEMUR_SECURITY_TEAM_EMAIL = ["security@example.com"]
LEMUR_DEFAULT_EXPIRATION_NOTIFICATION_INTERVALS = [30, 15, 2]

# Certificate Defaults
LEMUR_DEFAULT_COUNTRY = os.getenv("LEMUR_DEFAULT_COUNTRY", "US")
LEMUR_DEFAULT_STATE = os.getenv("LEMUR_DEFAULT_STATE", "California")
LEMUR_DEFAULT_LOCATION = os.getenv("LEMUR_DEFAULT_LOCATION", "Los Gatos")
LEMUR_DEFAULT_ORGANIZATION = os.getenv("LEMUR_DEFAULT_ORGANIZATION", "Example, Inc.")
LEMUR_DEFAULT_ORGANIZATIONAL_UNIT = os.getenv(
    "LEMUR_DEFAULT_ORGANIZATIONAL_UNIT", "Example"
)

# Logging

LOG_LEVEL = "DEBUG"
LOG_FILE = "lemur.log"


# Database
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "lemur")

# modify this if you are not using a local database
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://lemur:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/lemur"
)


# AWS

# LEMUR_INSTANCE_PROFILE = 'Lemur'

# Issuers

# These will be dependent on which 3rd party that Lemur is
# configured to use.

# CLOUDCA_URL = ''
# CLOUDCA_PEM_PATH = ''
# CLOUDCA_BUNDLE = ''

# number of years to issue if not specified
# CLOUDCA_DEFAULT_VALIDITY = 2

# VERISIGN_URL = ''
# VERISIGN_PEM_PATH = ''
# VERISIGN_FIRST_NAME = ''
# VERISIGN_LAST_NAME = ''
# VERSIGN_EMAIL = ''
