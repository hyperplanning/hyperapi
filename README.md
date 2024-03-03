[Hyperplan](https://www.hyperplan.fr) is dedicated to enhancing the growth and sustainability of the entire agri-food chain by providing reliable, real-time information on crop production. Amidst the increasing volatility in agricultural production due to climate change, market demand shifts, and geopolitical disturbances, we believes in the critical importance of having real-time, reliable visibility into agricultural production. Our mission is to offer unparalleled insight that drives the growth and sustainability of the whole agri-food chain, leveraging advanced remote sensing data and AI technology to transform parcel-level data into actionable decisions for daily operations.

Hyperplan provides an API access to his clients and partnership companies.

## [API](./docs/api_reference.md) Reference
The [Parcel API](./docs/api_reference.md) is designed for efficient parcel data management, featuring endpoints for accessing parcel and label metadata, and incorporating advanced search capabilities for thorough data retrieval and analysis. It aims to simplify parcel data access, providing in-depth insights for streamlined operations.

Label metadata includes detailed information about parcel labels such as unique identifiers, names, descriptions, categories (e.g., "TEXT"), and properties indicating the frequency of application (yearly, weekly). It also includes visual differentiation features like color and icon, and validation criteria depending on the label type (TEXT, NUMERICAL, DATE, OBJECT).

The API provides detailed label metadata in a predefined format, including validation types and choices, enhancing data annotation and retrieval in complex systems. Additionally, it outlines available labels within the Hyperplan Organization, covering various parcel characteristics from area and crop details to environmental conditions and parcel properties, excluding private labels.

For parcel-specific information, the API supports retrieving detailed data by parcel ID, with optional filters for labels, years, and weeks, offering a comprehensive view of parcel characteristics and changes over time.


## HyperClient
[HyperClient](./docs/quickstart.md) is a powerful and simple-to-use API client python library designed to make HTTP requests to the HyperAPI. It simplifies the process of interacting with the API by providing a straightforward method of making GET, POST, and DELETE requests, handling authentication, and processing responses.

- Easy to use API for making HTTP requests (GET, POST, DELETE)
- Automatic handling of authentication
- Supports session persistence across requests
- Simplifies the process of working with JSON data

