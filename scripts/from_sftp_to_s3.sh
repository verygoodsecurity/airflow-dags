#!/bin/bash
export AWS_ACCESS_KEY_ID={{ params.aws_access_key_id }}
export AWS_SECRET_ACCESS_KEY={{ params.aws_secret_access_key }}
pwd
mkdir ~/sftp_output
sshpass -p '{{ params.sftp_server_pass }}' scp -vv -o StrictHostKeyChecking=no "root@sftp-ml.verygoodsecurity.io:files/*" ~/sftp_output/

for file in ~/sftp_output/*; do
    aws s3 cp "${file}" "s3://airflow-streamline-test/test/" --profile vgs-dev
done
