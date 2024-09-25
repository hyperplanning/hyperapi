# Labels Available from the API

This document provides an overview of the labels available through the API, including their descriptions, categories, and configurations for yearly and weekly updates. This Table an example of avaible variables in our API. Labels are continusly updated by Hyperplan, and Organisations can also add their own labels.

## Table of Labels

| Name                    | Description                                                                                                                            | Category | Is Yearly | Is Weekly | Type              |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------|----------|-----------|-----------|-------------------|
| Farm                    | Parcel farm.                                                                                                                          | FARM     | false     | false     | farm              |
| Location                | Parcel municipality location.                                                                                                         | ZONE     | false     | false     | zone              |
| Irrigation              | Observed irrigation of the parcel (not real time data).                                                                               | TEXT     | false     | false     | null              |
| Water stress            | Observed hydric stress of the parcel (not real time data).                                                                            | TEXT     | false     | false     | hydric_stress     |
| Yield                   | Predictive yield of the parcel for the crop. Updated on a weekly basis.                                                               | NUMBER   | true      | false     | yield_common      |
| Volume                  | Crop surface multiplied by yield.                                                                                                     | NUMBER   | true      | false     | volume            |
| Accumulated rainfall    | Observed accumulative rainfalls. Updated on a weekly basis.                                                                           | NUMBER   | true      | true      | rainfall          |
| Tag                     | Customizable tag with parcel data.                                                                                                    | TEXT     | false     | false     | tag               |
| Closest silo            | Closest silo parcel defined, defined as a driving distance.                                                                           | FACILITY | false     | false     | closest_silo      |
| Area                    | Parcel Area.                                                                                                                          | NUMBER   | false     | false     | area              |
| Crop confidence score   | Hyperplan confidence score for crop prediction.                                                                                       | NUMBER   | true      | false     | crop_confidence   |
| Soil texture            | Soil type we get from LUCAS database.                                                                                                 | TEXT     | false     | false     | soil_type         |
| Crop detail             | Details we have about the crop.                                                                                                       | TEXT     | true      | false     | crop_details      |
| Crop                    | Predicted or satellite detected crop for ongoing and next campaign. Updated on a monthly basis.                                       | TEXT     | true      | false     | crop              |
| NDVI                    | Vegetation index retrieved by satellite. Updated on a weekly basis.                                                                   | NUMBER   | true      | true      | ndvi              |
| Accumulated temperature | Observed accumulative temperature. Updated on a weekly basis.                                                                         | NUMBER   | true      | true      | temperature       |
| Phenological stages     | Parcel phenology stage.                                                                                                               | TEXT     | true      | true      | stages            |

## Usage

These labels can be used to categorize and retrieve data from the API. Each label includes information about its update frequency (`Is Yearly` and `Is Weekly`) and its `Type`, which determines the kind of data or metadata associated with it.
