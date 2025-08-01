# 🔓 This example contains intentional security flaws for testing purposes only

import os
import subprocess

# 1. Hardcoded secret (detected by Gitleaks or truffleHog)
API_KEY = "AKIA1234567890EXAMPLESECRET"

# 2. Insecure use of subprocess (detected by Semgrep)
user_input = input("Enter a command to run: ")
subprocess.call(user_input, shell=True)

# 3. Hardcoded password
password = "AS813324@@1"

# 4. Insecure HTTP request
import requests
requests.get("http://example.com")  # HTTPS should be used instead
