# HyperClient

HyperClient is a powerful and simple-to-use API client library designed to make HTTP requests to the HyperAPI. It simplifies the process of interacting with the API by providing a straightforward method of making GET, POST, and DELETE requests, handling authentication, and processing responses.

## Features

- Easy to use API for making HTTP requests (GET, POST, DELETE)
- Automatic handling of authentication
- Supports session persistence across requests
- Simplifies the process of working with JSON data

## Installation

```python
pip install hyperclient
```

## Quick Start
To get started with HyperClient, import the client in your Python script:
```python
from hyperclient import HyperClient

client = HyperClient()
```
For more detailed instructions, refer to the [Quick Start Guide](/docs/quickstart.md).

## Authentication
HyperClient supports token-based authentication. To log in and start a session:
```
client.login('username', 'password')
```

## Making Requests

HyperClient simplifies the process of making requests to the HyperAPI. Here are some examples:
```python
# GET request
response = client.get('endpoint')

# POST request
response = client.post('endpoint', {'key': 'value'})
```

For comprehensive information on making requests, see the [API Reference](docs/api_reference.md).
