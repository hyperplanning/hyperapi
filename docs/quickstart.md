# Quickstart

### Installation

```python
pip install hyperclient
```

### Quick Start
To get started with HyperClient, import the client in your Python script:
```python
from hyperclient import HyperClient

client = HyperClient()
```

### Authentication
HyperClient supports token-based authentication. To log in and start a session:
```
client.login('username', 'password')
```

### Making Requests

HyperClient simplifies the process of making requests to the HyperAPI. Here are some examples:
```python
# GET request
response = client.get('endpoint')

# POST request
response = client.post('endpoint', {'key': 'value'})
```
