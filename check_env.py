import os

# Get the value of SQLALCHEMY_DATABASE_URI if set in the environment
database_uri = os.environ.get('SQLALCHEMY_DATABASE_URI')

# Check if the environment variable is set and print it
if database_uri:
    print(f"SQLALCHEMY_DATABASE_URI found in environment: {database_uri}")
else:
    print("SQLALCHEMY_DATABASE_URI not found in environment")
