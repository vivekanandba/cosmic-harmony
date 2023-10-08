# Python Install
python==3.8.6

# Prereq
In Windows Powershell run the following command to allow Python virtual environments

    % set-executionpolicy remotesigned

# Install in Windows (ONLY)
    % python -m venv .venv

# Open any python file and launch a terminal
    % pip install -r tests/requirements.txt
    % python -m playwright install 

# Run the tests
    % pytest tests