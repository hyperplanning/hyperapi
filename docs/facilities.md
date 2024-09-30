# Facilities

## Fetching Facilities for the Organization
GET `/v1/facilities`

This endpoint retrieves a list of facilities associated with the user's organization. Each facility includes its ID, name, geographical location (as a point), and optionally, a CRM code.

### Response

The response is an array of facility objects, where each object provides details about a specific facility. Below is a breakdown of the fields in the response:

#### Response Fields:
- `id` (integer): The unique identifier for the facility.
- `name` (string): The name of the facility.
- `geometry` (string): The geographical coordinates of the facility, represented as a `POINT(longitude latitude)` format.
- `crmCode` (nullable, string): The CRM code associated with the facility, if applicable. This field can be `null` if no CRM code is available.

### Example Request

**Request:**

```bash
GET /v1/facilities
```

**Response:**

```json
[
  {
    "id": 1,
    "name": "FACILITY A",
    "geometry": "POINT(2.000000 46.000000)",
    "crmCode": null
  },
  {
    "id": 2,
    "name": "FACILITY B",
    "geometry": "POINT(1.000000 45.000000)",
    "crmCode": "1234"
  },
  {
    "id": 3,
    "name": "FACILITY C",
    "geometry": "POINT(0.500000 47.000000)",
    "crmCode": "5678"
  }
]
```

### Explanation of Example

- **"FACILITY A" (id: 1)**: This facility does not have a CRM code, and its geographical location is represented by the point `POINT(2.000000 46.000000)`.
- **"FACILITY B" (id: 2)**: This facility has the CRM code `1234`, and its location is specified by `POINT(1.000000 45.000000)`.
- **"FACILITY C" (id: 3)**: This facility is identified by the CRM code `5678`, and its geographical location is given as `POINT(0.500000 47.000000)`.

### Notes

- **Geographical Coordinates**: The `geometry` field represents the exact location of the facility using longitude and latitude in the `POINT(longitude latitude)` format.
- **CRM Code**: The `crmCode` field is optional and may be `null` if the facility does not have a CRM code.
