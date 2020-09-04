import os

print("Docs: https://docs.python.org/3/library/os.html#os.getenv")
stage = os.getenv("STAGE", "prod").upper()
output = f"We're running in {stage}"

if stage.startswith('PROD'):
    output = "DANGER!!! " + output

print(output)