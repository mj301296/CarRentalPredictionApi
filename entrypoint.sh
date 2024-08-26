#!/bin/bash

# Optional: Check if AWS CLI is installed, and install if not
if ! command -v aws &> /dev/null
then
    echo "AWS CLI could not be found, installing..."
    pip install awscli
else
    echo "AWS CLI is already installed."
fi

# Check if environment variables are set
if [ -z "$S3_BUCKET_NAME" ] || [ -z "$PACKAGE_NAME" ]; then
    echo "Error: S3_BUCKET_NAME and PACKAGE_NAME environment variables must be set."
    exit 1
fi

# Download the package from S3
echo "Downloading package from S3..."
aws s3 cp s3://$S3_BUCKET_NAME/$PACKAGE_NAME/$PACKAGE_NAME-py3-none-any.whl /tmp/$PACKAGE_NAME-py3-none-any.whl

# Check if the download was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to download package from S3."
    exit 1
fi

# Install the package
echo "Installing package..."
pip install /tmp/$PACKAGE_NAME-py3-none-any.whl

# Check if the installation was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to install the package."
    exit 1
fi

# Start the FastAPI application
echo "Starting FastAPI application..."
uvicorn fastapi_app.main:app --host 0.0.0.0 --port 8000
