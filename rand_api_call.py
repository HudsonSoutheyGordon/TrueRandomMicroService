from jsonrpcclient import request, parse, Ok
import api_vals
import requests

def generate_random():
    rpc_dict = {
        "apiKey": api_vals.api_key,         # Must have another file with a random.org API key
        "n": 256,
        "min": 0,
        "max": 1,
        "replacement": True
    }

    response = requests.post("https://api.random.org/json-rpc/4/invoke",
                             json=request("generateIntegers", rpc_dict))

    parsed = parse(response.json())
    if isinstance(parsed, Ok):
        print(parsed.result)
        step1 = parsed.result
        step2 = step1['random']
        step3 = step2['data']
        return to_str(step3)
    else:
        print("Error with number generation: " + parsed.message)


def to_str(arr):
    bitstring = ''
    for bit in arr:
        bitstring += str(bit)

    return bitstring

