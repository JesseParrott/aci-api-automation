import requests
import yaml
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open('aci_config.yml') as f:
    cfg = yaml.safe_load(f)

apic = cfg['apic']
session = requests.Session()

# Login
login_url = f"{apic['url']}/api/aaaLogin.json"
payload = {
  "aaaUser": {
    "attributes": {
      "name": apic['username'],
      "pwd": apic['password']
    }
  }
}
resp = session.post(login_url, json=payload, verify=apic['verify_ssl'])
resp.raise_for_status()

# Get existing tenants
tenants_url = f"{apic['url']}/api/node/class/fvTenant.json"
tenants_resp = session.get(tenants_url, verify=False)
tenants = tenants_resp.json()["imdata"]

print("Existing Tenants:")
for t in tenants:
    print(t["fvTenant"]["attributes"]["name"])

# Create a new tenant
new_tenant_name = cfg['new_tenant']
create_url = f"{apic['url']}/api/node/mo/uni/tn-{new_tenant_name}.json"
create_payload = {
  "fvTenant": {
    "attributes": {
      "name": new_tenant_name
    }
  }
}
create_resp = session.post(create_url, json=create_payload, verify=False)
create_resp.raise_for_status()

print(f"Created Tenant: {new_tenant_name}")
