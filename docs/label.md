# Labels API

## Labels Metadata
Label Metadata, as described by the provided API endpoint, refers to detailed information about various labels that can be assigned to a parcel. This metadata is crucial for categorizing, organizing, and managing labels efficiently, especially our large-scale and complex system where data annotation and retrieval are essential.

Label Metadata holds the following information:
- `id`: A unique identifier for the label.
- `name`: The human-readable name of the label.
- `description`: A more detailed description of what the label represents or is used for.
- `category`: Specifies the type of data the label is associated with, e.g., "TEXT".
- `yearly`: A boolean indicating whether the label is applied on a yearly basis.
- `weekly`: A boolean indicating whether the label is applied on a weekly basis.
- `color`: A string that represents the color associated with the label, which can be useful for visual differentiation in user interfaces.
- `icon`: A string that represents the icon associated with the label, further aiding in visual identification.
- `validation`: An object that defines validation criteria for the label, depending on its category:
    - `type`: Specifies the label type: `TEXT`, `NUMERICAL`, `DATE` or `OBJECT`
    - the rest of the validation data depends on the label type

### Label Validation 

When a label is of type `TEXT`, the label value is saved as an integer, that points to a human readable text. This allows a more efficient way of storing the information, to limit human input errors, as well as more efficiently giving the choice information to the frontend. When the label is a `TEXT` label, the validation data therefor holds a `choice` attribute:

- `choice`: An array of objects representing the choices available for this label. Each choice object includes:
    - color: The color associated with the choice, represented as a hex code.
    - icon: An identifier for an icon associated with the choice.
    - key: A unique identifier for the choice.
    - value: The human-readable value or name of the choice.

The API will provide Label Metadata in the following format:
```json
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
}
```

### List Label Metadata
GET `/v1/labels/info`

#### Successful Response
Status Code: `201`
```json
[
  {<label metadata>}
]
```

