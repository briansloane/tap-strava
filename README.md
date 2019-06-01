# tap-strava

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:

- Pulls raw data from the [Strava API](https://developers.strava.com/docs/reference/#api-models-DetailedAthlete)
- Extracts the following resources:
  - [Athletes](https://developers.strava.com/docs/reference/#api-Activities-getLoggedInAthleteActivities)
  - [Activities](https://developers.strava.com/docs/reference/#api-Athletes-getLoggedInAthlete)
- Outputs the schema for each resource
- Incrementally pulls data based on the input state

## Quick Start

1. Install

    ```bash
    pip install tap-strava
    ```

2. Create the config file

   Create a JSON file called `config.json`. Its contents should look like:

   ```json
    {
        "start_date": "2010-01-01",
        "access_token": "<Strava access_token>",
        "refresh_token": "<Strava refresh_token>"
    }
    ```

   The `start_date` specifies the date at which the tap will begin pulling data
   (for those resources that support this).

4. Run the Tap in Discovery Mode

    ```bash
    tap-strava --config config.json --discover > catalog.json
    ```

   See the Singer docs on discovery mode
   [here](https://github.com/singer-io/getting-started/blob/master/docs/DISCOVERY_MODE.md#discovery-mode).

5. Run the Tap in Sync Mode

    ```bash
    tap-strava --config config.json --catalog catalog.json
    ```

---
