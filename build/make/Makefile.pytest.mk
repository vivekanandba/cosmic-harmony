#Pytest Verbose mode
pytest_verbose:
	pytest -v tests

#Print output
pytest_print:
	pytest -v -s tests

#Run Pytest with html report
pytest_html_version_test:
	pytest tests/test_0_api_basics.py --html=tests/reports/api_testing_$(VERSION)-$(DATE)-report.html --self-contained-html

#Run Pytest with html report
pytest_html_version:
	pytest --html=tests/reports/api_testing_$(VERSION)-$(DATE)-report.html --self-contained-html 

#Run Pytest with html report
pytest_html_rc:
	pytest tests/test_0_api_basics.py --html=tests/reports/api_testing_$(RELEASE_CANDIDATE)-$(DATE)-report.html --self-contained-html

pytest_html_tests:
	pytest tests/test_0_api_basics.py --html=tests/reports/test_report.html --self-contained-html 

# Parallel running of pytest n = no of workers 
pytest_parallel :
	pytest -n 3

# Marking pytest that particular tests with the mark can be run
pytest_marked:
	pytest -m login -v