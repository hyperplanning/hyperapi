The Parcel API facilitates robust parcel data management operations. 

The Parcel API facilitates robust parcel data management operations. It encompasses endpoints for obtaining information about parcel and label metadata, alongside specialized search functionalities for comprehensive data retrieval and analysis. This API is designed to streamline parcel data retrieval, offering detailed insights and control over parcel data for efficient operations.

## Labels Metadata
Label Metadata refers to detailed information about various labels that can be assigned to a parcel. This metadata is crucial for categorizing, organizing, and managing labels efficiently, especially in large-scale and complex systems where data annotation and retrieval are essential. You can find An example of Available Labels [here](./docs/labels.md)

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
- `type` (string, nullable): The type of the label, for example, is it a "crop classification", a 
- `display` (array of strings, nullable): Front-end display layers where the label is used. Possible values are: `"history"`, `"view"`, `"parcel_panel"`, `"split"`, `"evolution"`
- `fancy` (boolean): Indicates whether the label has advanced features.
- `authorizedValues` (array of integers): List of authorized values for the label. If empty, all values are authorized. This is relevant for labels with category `"TEXT"`.

### Label Validation
The `validation` object provides additional constraints and definitions for the label's values based on its category.

#### Text Validation

For labels of type `"TEXT"`, the validation object is as follows:
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
To get metadata information available to your organization, use the `/v1/labels/info` endpoint:

GET `/v1/labels/info`

### Response
- Status Code: `200 OK`
- Content Type: `application/json`
- Body:
```json
[
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
    "validation": { /* See validation object */ },
    "lastUpdatedAt": "2023-10-10T12:00:00Z",
    "years": [2021, 2022, 2023],
    "type": null,
    "display": ["view", "parcel_panel"],
    "fancy": false,
    "authorizedValues": [1, 2]
  }
  // ... additional label metadata
]
```

## Looking up a Parcel and its labels
GET `/v1/parcels/{parcel_id}`

#### Parameters
- `parcel_id` (integer, required): The unique identifier for the parcel.
- `labelIds` (array of integers, optional): List of label meta IDs to filter labels.

### Response
```json
{
  "id": "12345",
  "geometry": "MULTIPOLYGON(((...)))",
  "centroid": "POINT(...)",
  "labels": [
    {
      "labelMetaId": 1,
      "values": [
        {
          "year": 2023,
          "week": null,
          "status": "VALIDATED",
          "value": 1  // Corresponds to "Wheat"
        }
      ]
    }
    // ... additional labels
  ]
}
```

## Searching for a range of Parcels and their labels
The Hyperplan API system provides a for querying parcel data, namely Search Count and Search Parcels. These endpoints allow users to apply various filters to search through parcels based on metadata attributes. The core component driving these searches is the Search Query Object, which encapsulates the criteria for filtering parcels.

### Search Count Parcels
The Search Count endpoint is designed to count the number of parcels that meet specific criteria without returning the parcel data themselves. This is particularly useful for generating statistics or understanding the volume of parcels that match certain conditions.

#### Request

`GET /v1/elastic/search/count`

The request for this endpoint requires a list of Filter objects. Each Filter specifies a condition that the parcels must meet. The conditions are based on the metadata attributes associated with each parcel. The filters define the metadata ID (`metaId`), the operation to perform (such as `=`, `>`, `<`, `in`), and the values to compare against. The endpoint aggregates these filters to compute the count of parcels matching all provided criteria.

#### Request Body
```json
{
  "filters": [
    {
      "metaId": 0,
      "operation": "in",
      "years": [
        0
      ],
      "week": 0,
      "value": 0
    }
  ]
}
```

#### Response
The response from this endpoint is a single integer value representing the count of parcels that satisfy all the specified filters. This count is useful for analytics and reporting purposes.

### Search Parcels
The Search Parcels endpoint retrieves detailed information about parcels that match a set of filter criteria. This allows users to not only know the count but also examine the specific parcels that fulfill the given conditions.

#### Request
Similar to the Search Count endpoint, the request body for Search Parcels requires a list of Filter objects, defining the criteria for which parcels to retrieve. Each Filter object details the metadata ID, operation, and value(s) to apply in the search.

`GET /v1/elastic/search/parcels`

#### Request Body
```json
{
  "filters": [
    [
      {
        "metaId": 1,
        "operation": "in",
        "value": [
          1
        ],
        "year": 2023
      }
    ]
  ],
  "label": {
    "metaId": 1,
    "year": 2023
  }
}
```


#### Response
The response is a list of Parcel objects, each representing a parcel that meets the filter criteria. The ParcelSchema includes detailed information about each parcel, such as its unique identifier, associated label data, and other relevant attributes.

### Examples:
Given the list of possible labels for parcel data within the API, let's explore some relevant examples of filters that could be used with the `Search Count Parcels` and `Search Parcels` endpoints. These examples will demonstrate how to construct `Filter` objects based on various criteria, aligning with the attributes of the parcels such as area, NDVI, crop product, yield, temperature, rainfalls, soil type, and irrigation status.


### Example 1: Filter by Area
To find parcels larger than 10 hectares:
```json
{
  "filters": [
    [
      {
        "metaId": 1,  // Assuming 1 is the ID for "Area"
        "operation": ">",
        "value": 10
      }
    ]
  ]
}
```

### Example 2: Filter by NDVI for a Specific Year and Week
To select parcels with an average NDVI less than 0.5 in the year 2023 and week 24:
```json
{
  "filters": [
    [
      {
        "metaId": 2,  // Assuming 2 is the ID for "NDVI"
        "operation": "<",  // "inf" means less than
        "year": 2023,
        "week": 24,
        "value": 0.5
      }
    ]
  ]
}
```

### Example 3: Filter by Crop Product
To find parcels where the detected crop is "Wheat" in 2023:
```json
{
  "filters": [
    [
      {
        "metaId": 3,  // Assuming 3 is the ID for "Product"
        "operation": "equal",  // "equal" means exactly matches
        "year": 2023,
        "value": 1  // Assuming 1 is the Choice ID for Wheat
      }
    ]
  ]
}
```


## Aggregating Any Label Information - Reduce Query.

### Endpoint Documentation: POST `/v1/elastic/search/reduce`

### Description
This endpoint allows you to perform aggregation operations (e.g., sum, average) on any label while binning and filtering based on other labels. It also allows filtering of the parcels that go into the reduction (map part). This can be used to generate statistical insights and summaries based on the spatial and temporal data of parcels.

### Request Body Format:
```json
{
  "agg": {
    "agg_year": 0,
    "metaId": 1,
    "operation": "sum"
  },
  "bins": [
    {
      "metaId": 1,
      "operation": "in",
      "value": [
        1,
        2,
        3
      ]
    }
  ],
  "filters": [
    [
      {
        "metaId": 1,
        "operation": ">=",
        "value": 1,
        "week": 0,
        "years": [
          2023
        ]
      },
      {
        "metaId": 3,
        "operation": "<",
        "value": 100
      }
    ],
    [
      {
        "metaId": 1,
        "operation": "in",
        "value": [
          1
        ],
        "week": 0,
        "years": [
          2024
        ]
      }
    ]
  ],
  "years": [
    2023,
    2024
  ]
}
```

### Response Schema Example
```json
[
  {
    "groupby": {
      "metaId": 1,
      "value": 2
    },
    "value": 300.5
  }
]
```

### Example Use Cases

1. Sum of Crop Yield by Farm Size

To calculate the total yield of crops for parcels within different Crop Types:
```json
{
  "agg": {
    "agg_year": 2024,
    "metaId": 4,  // Assuming 4 is the ID for "Yield"
    "operation": "mean"
  },
  "bins": [
    {
      "metaId": 1,  // Assuming 1 is the ID for Crop
      "operation": "in",
      "value": [
        1, 2, 3  // Bins representing different Crop
      ]
    }
  ],
  "filters": [
    [
      {
        "metaId": 5,  // Filter by specific temperature
        "operation": ">",
        "value": 1000
      }
    ]
  ],
  "years": [2024]
}
```

2. Average NDVI by Crop Type for Specific Year
   
To find the average NDVI (Normalized Difference Vegetation Index) values for different crop types in 2023

```json
{
  "agg": {
    "agg_year": 2023,
    "metaId": 2,  // Assuming 2 is the ID for "NDVI"
    "operation": "avg"
  },
  "bins": [
    {
      "metaId": 3,  // Assuming 3 is the ID for "Crop Type"
      "operation": "in",
      "value": [1, 2, 3]  // IDs for different crop types
    }
  ],
  "filters": [],
  "years": [2023]
}
```

3. Maximum Temperature by Region with Rainfall Filter
To find the maximum temperature in different regions where the rainfall was below 200mm in 2023
```json
{
  "agg": {
    "agg_year": 2023,
    "metaId": 5,  // Assuming 5 is the ID for "Temperature"
    "operation": "max"
  },
  "bins": [
    {
      "metaId": 7,  // Assuming 7 is the ID for "Region"
      "operation": "in",
      "value": [1, 2, 3]  // Region IDs
    }
  ],
  "filters": [
    [
      {
        "metaId": 6,  // Assuming 6 is the ID for "Rainfall"
        "operation": "<=",
        "value": 200
      }
    ]
  ],
  "years": [2023]
}
```
