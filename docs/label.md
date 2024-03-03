# Labels API

## About Labels Metadata
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

When a label is of type `TEXT`, the label value is saved as an integer that points to a human readable text. This allows a more efficient way of storing the information, to limit human input errors, as well as more efficiently giving the choice information to the frontend. 

When the label is a `TEXT` label, the validation data therefore holds a `choice` attribute:
- `choice`: An array of objects representing the choices available for this label. Each choice object includes:
    - `color`: The color associated with the choice, represented as a hex code.
    - `icon`: An identifier for an icon associated with the choice.
    - `key`: A unique identifier for the choice.
    - `value`: The human-readable value or name of the choice.

When the label is a `NUMBER` label, the validation data therefor holds a `choice` attribute:

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

## HTTP Request
To get Metadata information available to your organisation, use the `/labels/info` endpoint:

GET `/v1/labels/info`

#### Response:
Status Code: `200`
```json
[
  {<label metadata>}
]
```

## Labels

Here are the Labels available in Hyperplan Organization, excluding private labels:

| Name                  | Description                                                                    | Category | Source                 | Yearly | Weekly |
|-----------------------|--------------------------------------------------------------------------------|----------|------------------------|--------|--------|
| Area                  | Parcel area in (Ha)                                                            | Number   | RPG                    | False  | False  |
| NDVI                  | Average NDVI of the parcel                                                     | Number   | Sentinel 2             | True   | True   |
| Product               | Crop detected on the parcel                                                    | Text     | Hyperplan              | True   | False  |
| Yield                 | Predictive yield of the parcel for the crop (see 3)                            | Number   | Hyperplan              | True   | False  |
| Temperature           | Observed accumulative temperature on the plot                                  | Number   | MeteoBlue              | True   | True   |
| Rainfalls             | Observed accumulative rainfalls on the plot                                    | Number   | MeteoBlue              | True   | True   |
| Soil type             | Soil type of the plot                                                          | Text     | LUCAS                  | False  | False  |
| Irrigation            | Observation if the parcel is irrigated or not (parcel property, not real time) | Number   | Hyperplan              | False  | False  |
| Hydric stress         | Observation if the parcel hydric stress level or not (parcel property)         | Number   | Hyperplan              | False  | False  |
| Closest silo          | Closest silo parcel defines, according to the organisation                     | Object   | Client Silo Base       | False  | False  |
| Zones                 | Zones to which the parcel Belongs                                              | Object   | Hyperplan              | False  | False  |
| Crop detail           | Provide information about the crop                                             | Text     | Hyperplan              | False  | False  |
| Farm                  | Farm owner of that parcel                                                      | Object   | Client CRM Information | False  | False  |
| Sowing date           | Detected sowing date                                                           | Date     | Hyperplan              | True   | False  |
| Harvest maturity date | Estimated maturity date                                                        | Date     | Hyperplan              | True   | False  |
| Harvest date          | Detected harvest date                                                          | Date     | Hyperplan              | True   | False  |
| Anomaly detection     | Anomaly detected on the parcel: NDVI not heterogen                             | Text     | Hyperplan              | True   | False  |
| Risk detected         | Parcel where sowing has been done but the NDVI is not increasing               | Text     | Hyperplan              | True   | False  |
| Crop Coverage Days    | Number of day when the NDVI of the parcel is > 25                              | Number   | Hyperplan              | True   | False  |


## Looking up a Parcel and its labels
Retrieves detailed information about a specific parcel by its ID, with an optional filter for specific labels based on their `meta_id`.

### HTTP Request
`GET /v1/parcels/{parcel_id}`

### Parameters

| Name       | Description  | Type    | In    | Required |
|------------|--------------|---------|-------|----------|
| `parcel_id`| The unique identifier for the parcel. | integer | path | Yes |
| `meta_id`  | Optional filter to retrieve labels by their meta identifier. | integer | query | No |

### Response
```json
{
  "id": 0,
  "geometry": "string",
  "centroid": "string",
  "labels": [<label object>]
}
```

## Searching for a range of Parcels and their labels

