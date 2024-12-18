# ACI API Automation

This project uses Python and the ACI APIC REST API to:

- Authenticate to the ACI APIC.
- Retrieve and list existing tenants.
- Create a new tenant using a POST request.

## Features

- Demonstrates basic ACI APIC interaction using Python's `requests` library.
- Configuration parameters stored in `aci_config.yml`.
- Easily extendable to manage VRFs, EPGs, and Contracts.

## Prerequisites

- Python 3.x
- `pip install -r requirements.txt`
- Access to ACI APIC (URL, credentials, etc.) configured in `aci_config.yml`.

## How to Run

1. Update `aci_config.yml` with APIC URL, credentials, and the tenant name you want to create.
2. Run `python3 aci_automation.py`.
3. Check terminal output for existing tenants and confirmation of the new tenant.
