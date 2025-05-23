# weather-image-recognition-using-CNN
deep learning model for classifying weather


## Workflows
1. update config.yaml
2. update params.yaml
3. update the enity
4. update the configuration manager in src config
5. update the components
6. update the pipeline
7. update the main.py
8. update the app.py


# how to run??

#### steps:
clone the repository

```bash
https://github.com/shivani983/weather-image-recognition-using-CNN.git
```

### step 1: create a conda environment after cloning the repository

```bash
conda create --name weatherCNN python=3.10 -y
```
```bash
conda activate weatherCNN
```
### step 2: install the requirements
```bash
pip install -r requirements.txt
```

```bash
python app.py
```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


#### Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

#### Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 315865595366.dkr.ecr.us-east-1.amazonaws.com/winerepo

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app
### model deployed

```bash
https://github.com/shivani983/weather_classification_binary_model_using_CNN/blob/main/aws_assets/docker_image.png?raw=true
```

```bash
https://github.com/shivani983/weather_classification_binary_model_using_CNN/blob/main/aws_assets/ECR.png?raw=true
```

```bash 
https://github.com/shivani983/weather_classification_binary_model_using_CNN/blob/main/aws_assets/iam_user.png?raw=true
```

```bash 
https://github.com/shivani983/weather_classification_binary_model_using_CNN/blob/main/aws_assets/EC2_machine.png?raw=true
```



