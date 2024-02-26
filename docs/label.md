# Labels API

## Labels Metadata

### List Label Metadata
GET `/v1/labels/info`

#### Successful Response
Status Code: `201`
```json
[
  {
    "id": 0,
    "name": "string",
    "description": "string",
    "category": "TEXT",
    "yearly": true,
    "weekly": true,
    "color": "string",
    "icon": "string",
    "validation": {
      "type": "TEXT",
      "choice": [
        {
          "color": "#000000",
          "icon": "fz-toto",
          "key": 1,
          "value": "Colza"
        }
      ]
    }
  },
  { ... }
]
```

### Create a new Label Metadata 
POST `/v1/labels/info`

#### Request Body
```json
{
  "name": "string",
  "description": "string",
  "category": "TEXT",
  "color": "string",
  "icon": "string",
  "yearly": false,
  "weekly": false,
  "validation": {
    "type": "TEXT",
    "choice": [
      {
        "color": "#000000",
        "icon": "fz-toto",
        "key": 1,
        "value": "Colza"
      }
    ]
  }
}
```
