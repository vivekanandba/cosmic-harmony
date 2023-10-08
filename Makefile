PROJECT_ID=soup-list-creator
PROJECT_NAME=gcr.io/PROJECT_ID/soup-list-creator:latest
RELEASE_CANDIDATE = 
VERSION = 1.0.0
DATE = 27-07-2021

include build/make/Makefile.core.mk
include build/make/Makefile.pytest.mk

install_requirement:
	pip install -r requirements.txt
soup_list:
	python soup_list_creator.py --input_path "inputs" --output_path "outputs"

cosmic_harmony_app:
	streamlit run Home.py