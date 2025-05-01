from aws_cdk import Stack, aws_ec2 as ec2, aws_iam as iam, aws_s3 as s3, CfnOutput
from constructs import Construct


class SftpStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, "SftpVpc", max_azs=2)

        bucket = s3.Bucket(self, "SftpBucket")

        role = iam.Role(
            self,
            "SftpInstanceRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess")
            ],
        )

        ec2_instance = ec2.Instance(
            self,
            "SftpInstance",
            instance_type=ec2.InstanceType("t3.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux(),
            vpc=vpc,
            role=role,
        )

        ec2_instance.user_data.add_commands(
            "yum update -y",
            "amazon-linux-extras install docker -y",
            "service docker start",
            "usermod -a -G docker ec2-user",
            "docker run -d --restart always -p 22:22 daviguides/simple-sftp",
        )

        ec2_instance.connections.allow_from_any_ipv4(
            ec2.Port.tcp(22), description="Allow SFTP access from anywhere"
        )

        CfnOutput(self, "SftpBucketName", value=bucket.bucket_name)
        CfnOutput(self, "InstancePublicIP", value=ec2_instance.instance_public_ip)
