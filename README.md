# Simple SFTP CDK Deployment

This project uses AWS CDK (Python) to provision infrastructure for deploying a secure SFTP server (`SimpleSFTP`) integrated with an S3 upload workflow (`sftp2s3`).

## Components

- VPC with public/private subnets
- EC2 instance with SFTP setup
- S3 bucket for file storage
- IAM roles and policies

## Deployment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cdk bootstrap
cdk deploy
```
