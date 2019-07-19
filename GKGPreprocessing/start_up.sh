sudo  wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u141-b15/336fa29ff2bb4ef291e347e091f7f4a7/jdk-8u141-linux-x64.rpm
sudo yum install -y jdk-8u141-linux-x64.rpm
sudo wget https://nlp.stanford.edu/software/stanford-ner-2018-10-16.zip
unzip stanford-ner-2018-10-16.zip
pip install boto3
pip install s3fs
