# Json format
- **import the json file**
- **dumps the json file**
- **print the json file**
## sample code for json file print
```
sample = {"key1" : "value2", "key2" : "value2", "key3" : "value3"}
value  = json.dumps(sample, indent=2, separators=(",", " = "))
print(value)
```
## Example Output
```
{
  "key1" = "value2",
  "key2" = "value2",
  "key3" = "value3"
}
```
