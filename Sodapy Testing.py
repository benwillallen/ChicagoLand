from sodapy import Socrata
client = Socrata("data.cityofchicago.org", None, timeout=20)
print(client.get("sxs8-h27x", limit=1, select="SEGMENT_ID"))
