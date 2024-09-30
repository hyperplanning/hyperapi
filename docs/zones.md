# Zone Groups

## Fetching Available Zone Groups
GET `/v1/zone-groups`

This endpoint retrieves a list of zone groups, including administrative zone groups (such as municipalities, postal codes, departments, regions, and countries) as well as specific zone groups associated with your organization, for which you have viewing permissions.

### Parameters
This endpoint does not require any parameters.

### Response

The response is an array of zone group objects, where each object provides information about a specific zone group. Below is a breakdown of the fields in the response:

#### Response Fields:
- `editor` (nullable, string): The user who last edited the zone group, or `null` if no editor is assigned.
- `isPublic` (boolean): A flag indicating whether the zone group is public (`true`) or restricted to specific users (`false`).
- `id` (integer): The unique identifier for the zone group.
- `floor` (nullable, string): This field is reserved for future use or specific cases, and is currently `null`.
- `isExclusive` (boolean): A flag that indicates whether the zone group's areas are exclusive (`true`, meaning they do not overlap geographically) or non-exclusive (`false`, meaning they can overlap geographically).
- `name` (string): The name of the zone group (e.g., "Municipalities", "Postal codes", "Departments", etc.).
- `mapboxId` (string): The unique identifier for the zone group used in the Mapbox system for visualization (e.g., `adm3`, `pos4`, `adm2`).

### Example Response

```json
[
  {
    "editor": null,
    "isPublic": true,
    "id": 2,
    "floor": null,
    "isExclusive": true,
    "name": "Municipalities",
    "mapboxId": "adm3"
  },
  {
    "editor": null,
    "isPublic": true,
    "id": 3,
    "floor": null,
    "isExclusive": true,
    "name": "Postal codes",
    "mapboxId": "pos4"
  },
  {
    "editor": null,
    "isPublic": true,
    "id": 4,
    "floor": null,
    "isExclusive": true,
    "name": "Departments",
    "mapboxId": "adm2"
  },
  {
    "editor": null,
    "isPublic": true,
    "id": 5,
    "floor": null,
    "isExclusive": true,
    "name": "Regions",
    "mapboxId": "adm1"
  },
  {
    "editor": null,
    "isPublic": true,
    "id": 6,
    "floor": null,
    "isExclusive": true,
    "name": "Country",
    "mapboxId": "adm0"
  }
]
```
### Explanation of Example:

- **"Municipalities" (id: 2)**: This is a public zone group representing municipal-level administrative boundaries. The `isExclusive: true` flag indicates that the zones in this group do not overlap geographically. It has a `mapboxId` of `"adm3"`, meaning it corresponds to the municipal level in the Mapbox hierarchy.

- **"Postal codes" (id: 3)**: This zone group represents postal code regions and is public. The `isExclusive: true` flag means that the zones in this group are geographically exclusive (no overlap). It has a `mapboxId` of `"pos4"`.

- **"Departments" (id: 4)**: A public zone group representing department-level boundaries. The `isExclusive: true` flag indicates that the departments are geographically exclusive (no overlap). It has a `mapboxId` of `"adm2"`.

- **"Regions" (id: 5)**: This zone group represents regional boundaries and is public. The `isExclusive: true` flag means the regions do not overlap. It has a `mapboxId` of `"adm1"`.

- **"Country" (id: 6)**: This group represents country-level boundaries and is public. The `isExclusive: true` flag means the country boundaries do not overlap with others in this group. It has a `mapboxId` of `"adm0"`.

### Notes:

- **Visibility**: The `isPublic` field indicates whether the zone group can be viewed by everyone (`true`) or is restricted (`false`).

- **Geographical Exclusivity**: The `isExclusive` field indicates whether the zones in the group are geographically exclusive (`true`) or can overlap with one another (`false`). This is an important distinction when dealing with boundaries that might overlap versus those that are strictly delineated (such as administrative regions).

- **Mapbox Integration**: The `mapboxId` is essential for rendering the specific zone group on Mapbox-based maps and relates to the level of administrative boundaries (e.g., municipalities, postal codes, regions).

### Additional Information:
Organizations may have custom zone groups that are not public but are available for use within the organization, depending on viewing permissions and geographical exclusivity settings.


