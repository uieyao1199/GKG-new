# GKGPreprocessing

## Introduction:

This is the project that we run to preprocess the orgnizations from GKG database.
Here are basic descriptions of files in this respository.

* start_up.sh - which contains bash script that help you install/download required packages.
* credentialkey.txt - which contains AWS credential key which can give you access to s3 bucket.

## Step 1:

* Start an ec2 virtual machine.

* After you accept the colloborate invitation, fork this respository. You can think fork is use this respository as a template. Clone your __forked respository__ to your virtual machine.

* cd into the cloned folder and install packages:
```
bash start_up.sh
```

* The process would take at most 2 mins, after it stoped you will see:
```
(base) [ec2-user@ip-172-31-46-169 GKGPreprocessing]$ ls
README.md           jdk-8u141-linux-x64.rpm      start_up.sh
TemplateCode.ipynb  stanford-ner-2018-10-16
credentialkey.txt   stanford-ner-2018-10-16.zip
```

* Here `jdk-8u141-linux-x64.rpm`, `stanford-ner-2018-10-16.zip` are files we downloaded from website, and `stanford-ner-2018-10-16` is the file we unzipped from `stanford-ner-2018-10-16.zip`. This folder contains an NER(Stanford Named Entity Recognizer) model trained by Stanford University.(Here is the description [link](https://nlp.stanford.edu/software/CRF-NER.html)). In this project, we will used this NLP model to recognize if the orgnization name in GKG dataset is an company or not.

* Now we need to add aws access key to our virtual machine, since we have a huge database, we cannot store them in github repository, we use [s3 bucket](https://aws.amazon.com/s3/). Because the bucket is a private bucket, we need access to it. Using the following code:
```
aws configure
```
* And you will see:
```(base) [ec2-user@ip-172-31-46-169 GKGPreprocessing]$ aws configure
AWS Access Key ID [None]:
```

* Copy the __AWSAccessKeyId__ which you can find in credentialkey.txt:
```
(base) [ec2-user@ip-172-31-46-169 GKGPreprocessing]$ aws configure
AWS Access Key ID [None]:AKIAJN5VRXD7Q3XYM4OA
```
* Press __enter__ and you will see `AWS Secret Access Key [None]:`, paste the __AWSSecretKey__ in and press __enter__.

* And you will see:
```
(base) [ec2-user@ip-172-31-46-169 GKGPreprocessing]$ aws configure
AWS Access Key ID [None]: AKIAJN5VRXD7Q3XYM4OA
AWS Secret Access Key [None]: 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
Default region name [None]:
```

* You can ignore it and press __enter__ and you will see:
```
(base) [ec2-user@ip-172-31-46-169 GKGPreprocessing]$ aws configure
AWS Access Key ID [None]: AKIAJN5VRXD7Q3XYM4OA
AWS Secret Access Key [None]: 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
Default region name [None]:
Default output format [None]:
```

* Ignore it and press __enter__, then you all set.

* Now open an jupyter notebook server, and follow the description in the __BasicTemplate.ipynb__.

## Step 2:

* Go to your __AWS Management Console__ and search s3.

* Once you clicked into __s3 Management console__, you will see several buckets. Create your own __result bucket__.

* Click __create bucket__, type in your firstname+result for example mine is __fanresult__. Keep clicking next until you created your bucket. And you bucket path is __s3://[bucketname]/__. For example mine is __s3://fanresult/__.

* In your virtual machine, you can copy your result directly to you bucket using the following code:
```
aws s3 cp [filename] s3://[bucketname]
```

* For example, if I want to copy __result_1.csv__ to my bucket:
```
aws s3 cp result_1.csv s3://fanresult/
```

