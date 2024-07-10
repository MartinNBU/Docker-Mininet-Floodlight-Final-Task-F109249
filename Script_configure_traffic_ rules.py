import requests
import json

controller_ip = '127.0.0.1:8080'

def add_flow_rule(switch_id, src_ip, dst_ip, in_port, out_port):
    url = f'http://{controller_ip}/wm/staticentrypusher/json'
    headers = {'Content-Type': 'application/json'}
    payload = {
        "switch": switch_id,
        "name": f"flow-{src_ip}-to-{dst_ip}",
        "cookie": "0",
        "priority": "32768",
        "in_port": in_port,
        "eth_type": "0x0800",
        "ipv4_src": src_ip,
        "ipv4_dst": dst_ip,
        "active": "true",
        "actions": f"output={out_port}"
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    return response.json()

# Add rules for traffic from h1 to h19
add_flow_rule("00:00:00:00:00:01", "10.0.0.1", "10.0.0.19", "1", "2")
add_flow_rule("00:00:00:00:00:19", "10.0.0.19", "10.0.0.1", "2", "1")

# Add rules for traffic from h19 to h1
add_flow_rule("00:00:00:00:00:19", "10.0.0.19", "10.0.0.1", "1", "2")
add_flow_rule("00:00:00:00:00:01", "10.0.0.1", "10.0.0.19", "2", "1")
