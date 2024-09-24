The Parcel API facilitates robust parcel data management operations. 

The Parcel API facilitates robust parcel data management operations. It encompasses endpoints for obtaining information about parcel and label metadata, alongside specialized search functionalities for comprehensive data retrieval and analysis. This API is designed to streamline parcel data retrieval, offering detailed insights and control over parcel data for efficient operations.

## Labels Metadata
Label Metadata refers to detailed information about various labels that can be assigned to a parcel. This metadata is crucial for categorizing, organizing, and managing labels efficiently, especially in large-scale and complex systems where data annotation and retrieval are essential.

### Label Metadata Properties
Label Metadata holds the following information:

- `id` (integer): A unique identifier for the label.
- `name` (string): The human-readable name of the label.
- `description` (string, nullable): A detailed description of what the label represents or is used for.
- `category` (string): Specifies the type of data the label is associated with. Possible values are: `"TEXT"`, `"NUMBER"`, `"DATE"`, `"ZONE"`, `"FARM"`, `"FACILITY"` and `"USER"`
- `isYearly` (boolean): Indicates whether the label is applied on a yearly basis.
- `isWeekly` (boolean): Indicates whether the label is applied on a weekly basis.
- `isEditable` (boolean): Indicates whether the label can be edited.
- `color` (string, nullable): Represents the color associated with the label, useful for visual differentiation in user interfaces.
- `icon` (string, nullable): Represents the icon associated with the label, aiding in visual identification.
- `validation` (object, nullable): Defines validation criteria for the label, depending on its category.
- `lastUpdatedAt` (string, date-time): Timestamp of the last update to the label metadata.
- `years` (array of integers, nullable): List of years the label is applicable to.
- `type` (string, nullable): The type of the label meta.
- `display` (array of strings, nullable): Front-end display layers where the label is used. Possible values are: `"history"`, `"view"`, `"parcel_panel"`, `"split"`, `"evolution"`
- `fancy` (boolean): Indicates whether the label has advanced features.
- `authorizedValues` (array of integers): List of authorized values for the label. If empty, all values are authorized. This is relevant for labels with category `"TEXT"`.

### Label Validation
The `validation` object provides additional constraints and definitions for the label's values based on its category.

#### Text Validation

For labels of type `"TEXT"`, the validation object is as follows:
- `type` (string): Must be "TEXT".
- `choice` (array of KeyValueTextValidation objects): Represents the choices available for this label.

Each KeyValueTextValidation object includes:
- `key` (integer): A unique identifier for the choice.
- `value` (string): The human-readable value or name of the choice.
- `icon` (string, nullable): An identifier for an icon associated with the choice.
- `color` (string, nullable): The color associated with the choice, represented as a hex code.
- `falcoId` (string, nullable): An optional identifier for integration with other systems.

#### Number Validation

For labels of type `"NUMBER"`, the validation object is:
- `type` (string): Must be "NUMBER".
- `min` (integer, nullable): Minimum acceptable value.
- `max` (integer, nullable): Maximum acceptable value.
- `unit` (string, nullable): Unit of measurement.
- `precision` (integer, nullable): Number of decimal places.

#### Other Validations

Other label types like `"ZONE"`, `"FARM"`, `"FACILITY"`, and `"USER"` have their respective validation schemas, primarily indicating the type and related IDs.

### Example of Label Metadata
```json
{
  "id": 1,
  "name": "Crop Type",
  "description": "Type of crop grown on the parcel",
  "category": "TEXT",
  "isYearly": true,
  "isWeekly": false,
  "isEditable": true,
  "color": "#00FF00",
  "icon": "crop-icon",
  "validation": {
    "type": "TEXT",
    "choice": [
      {
        "key": 1,
        "value": "Wheat",
        "icon": "wheat-icon",
        "color": "#FFFF00",
        "falcoId": "wheat"
      },
      {
        "key": 2,
        "value": "Corn",
        "icon": "corn-icon",
        "color": "#FFA500",
        "falcoId": "corn"
      }
    ]
  },
  "lastUpdatedAt": "2023-10-10T12:00:00Z",
  "years": [2021, 2022, 2023],
  "type": null,
  "display": ["view", "parcel_panel"],
  "fancy": false,
  "authorizedValues": [1, 2]
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

| Name                      | Description                                                                    | Category | Source                 | Yearly | Weekly |
|---------------------------|--------------------------------------------------------------------------------|----------|------------------------|--------|--------|
| **Area**                  | Parcel area in (Ha)                                                            | Number   | RPG                    | False  | False  |
| **NDVI**                  | Average NDVI of the parcel                                                     | Number   | Sentinel 2             | True   | True   |
| **Product**               | Crop detected on the parcel                                                    | Text     | Hyperplan              | True   | False  |
| **Yield**                 | Predictive yield of the parcel for the crop (see 3)                            | Number   | Hyperplan              | True   | False  |
| **Temperature**           | Observed accumulative temperature on the plot                                  | Number   | MeteoBlue              | True   | True   |
| **Rainfalls**             | Observed accumulative rainfalls on the plot                                    | Number   | MeteoBlue              | True   | True   |
| **Soil type**             | Soil type of the plot                                                          | Text     | LUCAS                  | False  | False  |
| **Irrigation**            | Observation if the parcel is irrigated or not (parcel property, not real time) | Number   | Hyperplan              | False  | False  |
| **Hydric stress**         | Observation if the parcel hydric stress level or not (parcel property)         | Number   | Hyperplan              | False  | False  |
| **Closest silo**          | Closest silo parcel defines, according to the organisation                     | Object   | Client Silo Base       | False  | False  |
| **Zones**                 | Zones to which the parcel Belongs                                              | Object   | Hyperplan              | False  | False  |
| **Farm**                  | Farm owner of that parcel                                                      | Object   | Client CRM Information | False  | False  |
| **Sowing date**           | Detected sowing date                                                           | Date     | Hyperplan              | True   | False  |
| **Harvest maturity date** | Estimated maturity date                                                        | Date     | Hyperplan              | True   | False  |
| **Harvest date**          | Detected harvest date                                                          | Date     | Hyperplan              | True   | False  |
| **Anomaly detection**     | Anomaly detected on the parcel: NDVI not heterogen                             | Text     | Hyperplan              | True   | False  |
| **Risk detected**         | Parcel where sowing has been done but the NDVI is not increasing               | Text     | Hyperplan              | True   | False  |
| **Crop Coverage Days**    | Number of day when the NDVI of the parcel is > 25                              | Number   | Hyperplan              | True   | False  |


## Looking up a Parcel and its labels
Retrieves detailed information about a specific parcel by its ID, with an optional filter for specific labels based on their `meta_id`.

### HTTP Request
`GET /v1/parcels/{parcel_id}`

### Parameters
| Name        | Description                                                  | Type    | In    | Required |
|-------------|--------------------------------------------------------------|---------|-------|----------|
| **parcel_id** | The unique Hyperplan identifier for the parcel.             | integer | path  | Yes      |
| **meta_id**   | Optional filter list to retrieve labels by their meta identifier. | integer | query | No       |
| **years**     | Optional year filter list to retrieve labels                 | integer | query | No       |
| **weeks**     | Optional week filter list to retrieve labels                 | integer | query | No       |


### Response
```json
{
  "id": 0,
  "code": 0,
  "geometry": "string",
  "centroid": "string",
  "labels": [
    {
      "meta_id": 1,
      "week": 24,
      "year": 2023,
      "value": "Value specific to the label for this week and year"
    },
    {
      "meta_id": 2,
      "week": 24,
      "year": 2023,
      "value": "Another value for a different label, same week and year"
    }
  ]
}
```

Where `geometry` is the WKT string of the parcel polygon, `centroid` is the long/lat centroid of the parcel, `code` is the external reference id of the parcel (for France it is the RPG parcel id).

It is also possible to query a parcel with it's external code, although unicity is not garanteed.
### HTTP Request

`GET /v1/parcels/code/{code}`

### Parameters
| Name       | Description                                                  | Type    | In    | Required |
|------------|--------------------------------------------------------------|---------|-------|----------|
| **code**     | The external identifier for the parcel.                      | integer | path  | Yes      |
| **meta_id**  | Optional filter list to retrieve labels by their meta identifier. | integer | query | No       |
| **years**    | Optional year filter list to retrieve labels                 | integer | query | No       |
| **weeks**    | Optional week filter list to retrieve labels                 | integer | query | No       |


## Searching for a range of Parcels and their labels
The Hyperplan API system provides a for querying parcel data, namely Search Count and Search Parcels. These endpoints allow users to apply various filters to search through parcels based on metadata attributes. The core component driving these searches is the Search Query Object, which encapsulates the criteria for filtering parcels.

### Search Count Parcels
The Search Count endpoint is designed to count the number of parcels that meet specific criteria without returning the parcel data themselves. This is particularly useful for generating statistics or understanding the volume of parcels that match certain conditions.

#### Request

`GET /v1/search/count`

The request for this endpoint requires a list of Filter objects. Each Filter specifies a condition that the parcels must meet. The conditions are based on the metadata attributes associated with each parcel. The filters define the metadata ID (`meta_id`), the operation to perform (such as `=`, `>`, `<`, `in`), and the values to compare against. The endpoint aggregates these filters to compute the count of parcels matching all provided criteria.

#### Request Body
```json
[
  {
    "meta_id": 0,
    "operation": "=, >, < or in",
    "year": 0,
    "week": 0,
    "value": 0
  },
  {
    ...
  }
]
```

#### Response
The response from this endpoint is a single integer value representing the count of parcels that satisfy all the specified filters. This count is useful for analytics and reporting purposes.

### Search Parcels
The Search Parcels endpoint retrieves detailed information about parcels that match a set of filter criteria. This allows users to not only know the count but also examine the specific parcels that fulfill the given conditions.

#### Request
Similar to the Search Count endpoint, the request body for Search Parcels requires a list of Filter objects, defining the criteria for which parcels to retrieve. Each Filter object details the metadata ID, operation, and value(s) to apply in the search.

`GET /v1/search/parcels`

#### Request Body
```json
[
  {
    "meta_id": 0,
    "operation": "=, >, < or in",
    "year": 0,
    "week": 0,
    "value": 0
  },
  {
    ...
  }
]
```


#### Response
The response is a list of Parcel objects, each representing a parcel that meets the filter criteria. The ParcelSchema includes detailed information about each parcel, such as its unique identifier, associated label data, and other relevant attributes.

### Examples:
Given the list of possible labels for parcel data within the API, let's explore some relevant examples of filters that could be used with the `Search Count Parcels` and `Search Parcels` endpoints. These examples will demonstrate how to construct `Filter` objects based on various criteria, aligning with the attributes of the parcels such as area, NDVI, crop product, yield, temperature, rainfalls, soil type, and irrigation status.


### Example 1: Filter by Area
To find parcels larger than 10 hectares:
```json
{
  "meta_id": 1,  # Assuming 1 is the ID for "Area"
  "operation": ">",
  "value": 10
}
```

### Example 2: Filter by NDVI for a Specific Year and Week
To select parcels with an average NDVI less than 0.5 in the year 2023 and week 24:
```json
{
  "meta_id": 2,  # Assuming 2 is the ID for "NDVI"
  "operation": "<",
  "year": 2023,
  "week": 24,
  "value": 0.5
}
```

### Example 3: Filter by Crop Product
To find parcels where the detected crop is "Wheat" in 2023:
```json
{
  "meta_id": 3,  # Assuming 3 is the ID for "Product"
  "operation": "=",
  "year": 2023,
  "value": 1 # Assuming 1 is Wheat Choice ID
}
```

### Example 5: Filter by Temperature and Rainfalls
To find parcels that have observed accumulative temperature above 1000°C and accumulative rainfalls less than 200mm for the year 2023:
```json
[
// Temperature Filter
{
  "meta_id": 5,  # Assuming 5 is the ID for "Temperature"
  "operation": ">",
  "year": 2023,
  "value": 1000
}, 
# Rainfall Filter
{
  "meta_id": 6,  # Assuming 6 is the ID for "Rainfalls"
  "operation": "<",
  "year": 2023,
  "value": 200
}
]
```
