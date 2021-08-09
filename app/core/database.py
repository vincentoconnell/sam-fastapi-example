from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from jose import jwt
from typing import Optional
from fastapi import Header
import boto3
from boto3.dynamodb.conditions import Key, Attr

# SQLAlchemy specific code, as with any other app
driver = "postgresql"
host = "blah"
port = 1337
db = "blah"
user = "blah"
password = "blah"
DATABASE_URL = f"postgresql://{user}:{password}@{host}/%s"

# Initial session to support ORM binding
engine = create_engine(DATABASE_URL % db)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
SessionLocal.name = db
Base = declarative_base()


# Postgres Dependency
def get_db(authorization: Optional[str] = Header(None)):
    print("retrieving DB for token")
    # pull cognito uuid out of headers
    print(f"auth header: {authorization}")
    claims = jwt.get_unverified_claims(authorization)
    cog_uuid = claims['cognito:username']
    print(f"Cognito username for request: {cog_uuid}")

    # Get db_name from DynamoDB
    dynamodb = boto3.resource(
        'dynamodb',
        region_name='ca-central-1'
    )
    table = dynamodb.Table('table123')
    attributes = table.query(
        KeyConditionExpression=Key('cognito_uuid').eq(cog_uuid)
    )
    if 'Items' in attributes and len(attributes['Items']) > 0:
        attributes = attributes['Items'][0]
    print(f"attributes from DynamoDB lookup: {attributes}")
    db_name = attributes.get('db_name')
    print(f"db name: {db_name}")

    # Connect to the user's DB
    engine = create_engine(DATABASE_URL % db_name)
    SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    SessionLocal.name = db_name

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Dynamo Dependency which returns data for the cog_uuid from the auth table
def get_data(authorization: Optional[str] = Header(None)):
    print("retrieving data for token")
    # pull cognito uuid out of headers
    print(f"auth header: {authorization}")
    claims = jwt.get_unverified_claims(authorization)
    cog_uuid = claims['cognito:username']
    print(f"Cognito username for request: {cog_uuid}")

    # Get data from DynamoDB
    dynamodb = boto3.resource(
        'dynamodb',
        region_name='ca-central-1'
    )
    table = dynamodb.Table('table123')
    attributes = table.query(
        KeyConditionExpression=Key('cognito_uuid').eq(cog_uuid)
    )
    print(f"Items from DynamoDB lookup: {attributes['Items']}")
    return attributes['Items']
