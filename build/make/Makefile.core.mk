PROJECT_NAME = vivek-dev2
IMAGE_NAME = core-api-test-suite:latest
TAG_NAME = gcr.io/$(PROJECT_NAME)/$(IMAGE_NAME)
PORT = 8081
LOCALHOST = http://localhost:$(PORT)
CONTAINER_NAME = core-api-test-suite
CLOUDAPP = https://flask-api-framework-2uxzahygxq-uw.a.run.app

default:
	echo Use make docker_build or make docker_run

prune:
	docker system prune 

#Setup python
python_setup:
	bash install/python_setup.sh
	echo Open a new terminal before making the vscode

#Setup vscode
dependencies_setup:
	bash install/vs_code_setup.sh

local_build:
	python api_test.py
	
local_run:
	make -e APP_LOCATION=$(LOCALHOST) run_check
	#fuser -k $(PORT)/tcp
	
docker_local_build:
	docker build -f build/docker/Dockerfile.local --tag $(IMAGE_NAME) .

docker_local_run:
	docker run -d --name $(CONTAINER_NAME) --publish $(PORT):8080 $(IMAGE_NAME)
	#make -e APP_LOCATION=$(LOCALHOST) run_check
	#docker kill $(CONTAINER_NAME)
	#docker rm $(CONTAINER_NAME)
	
release_port: #use it to release a port	
	fuser -k 8081/tcp

gcp_local_build:
	docker build -f build/docker/Dockerfile.cloud \
			--tag $(TAG_NAME) .
	
	docker push $(TAG_NAME)

gcp_local_cloud_deploy:
	gcloud run deploy $(CONTAINER_NAME) --project $(PROJECT_NAME)  \
				--image $(TAG_NAME)  --platform managed

gcp_build:
	cp ./build/docker/Dockerfile.cloud Dockerfile
	gcloud builds submit --tag $(TAG_NAME)
	rm ./Dockerfile

gcp_deploy:
	gcloud run deploy $(CONTAINER_NAME) --image $(TAG_NAME) --platform managed

gcp_run_check: 
	make -e APP_LOCATION=$(CLOUDAPP) run_check

run_check:
	sleep 1
	curl $(APP_LOCATION)/
	sleep 1
	curl $(APP_LOCATION)/api/ping
	sleep 1
	curl $(APP_LOCATION)/api/ping_from_browser
	sleep 1
	curl $(APP_LOCATION)/api/version
	sleep 1
	curl $(APP_LOCATION)/api/get_anything
	sleep 1
	curl $(APP_LOCATION)/api/get_error
	sleep 1

requirements_output.txt: requirements_input.txt
	cp requirements_input.txt requirements_output.txt
	pip install -r requirements_output.txt	

line_count:
	wc -l *.py components/*.py tests/*.py 

coverage:
	coverage run -m pytest tests 
	coverage html

coverage_verbose:
	coverage run -m pytest -v tests 
	coverage html

print_api_versions:
	time curl https://api-framework.tcdcloud.com/api/version

copy_config:
	mkdir -p config
	mkdir -p tests/config
	cp ./build/local/config.local.ini config/config.ini
	cp ./build/local/config.unit_tests.ini tests/config/config.unit_tests.ini

clean_up:
	if [ -d "coverage_html" ]; then rm -Rf coverage_html; fi
	if [ -d "config" ]; then rm -Rf config; fi
	if [ -d "tests/config" ]; then rm -Rf tests/config; fi
	if [ -d "templates" ]; then rm -Rf templates; fi

pytest:
	python api_test.py

# authorized cloud push
docker_cloud_push_authorize:
	gcloud auth configure-docker
	docker-credential-gcloud list