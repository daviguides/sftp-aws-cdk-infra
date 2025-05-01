#!/usr/bin/env python3
import aws_cdk as cdk
from sftp_stack.sftp_stack import SftpStack

app = cdk.App()
SftpStack(app, "SftpStack")
app.synth()
