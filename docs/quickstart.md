# HyperPlan API - Quickstart

This guide provides a step-by-step explanation of how to interact with the HyperPlan API to authenticate, retrieve zone information, and fetch parcel data with associated labels.

## 1. Imports

```python
from hyperapi.client import HyperClient
from tqdm import tqdm
import os
```

## 2. Authentication
Instantiate the `HyperClient` to point to the HyperPlan API endpoint. Login using credentials stored in environment variables `API_USR` and `API_PWD`.

```python
client = HyperClient("https://api.hyperplan.io/v1")
auth = client.login(os.getenv("API_USR"), os.getenv("API_PWD"))
if auth:
    print("Authentication Successful !")
```

## 3. Listing Available Label Metas

This section retrieves metadata for all available labels and stores them in a dictionary with label names as keys for easier access using the `labels/info` endpoint:
```python
labels = client.get("labels/info")
labels = {l["name"]: l for l in labels.json()}
```

## 4. Getting Zone Groups
Here, zone groups (e.g., Departments, Municipalities) are fetched from the API and stored in a dictionary with the zone group names as keys.






