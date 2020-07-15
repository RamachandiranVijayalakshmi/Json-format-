import json
sample = {"key1" : "value2", "key2" : "value2", "key3" : "value3"}
value  = json.dumps(sample, indent=2, separators=(",", " = "))
print(value)
