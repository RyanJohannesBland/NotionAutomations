import json
import requests
import pdb


with open("env.json", 'r') as env_file:
    ENV = json.loads(env_file.read())
HEADERS = {
    "Authorization": f"Bearer {ENV['token']}",
    "Notion-Version": "2021-08-16"
}


def main():
    # Harvest all daily tasks.
    response = requests.post(
        f"https://api.notion.com/v1/databases/{ENV['database_id']}/query",
        headers=HEADERS,
        json={
            "filter": {
                "property": "Type",
                "select": {
                    "equals": "Daily"
                }
            }
        }
    ).json()["results"]

    # Move daily tasks back into the "To Do" section.
    for page in response:
        response = requests.patch(
            f"https://api.notion.com/v1/pages/{page['id']}",
            headers=HEADERS,
            json={
                "properties": {
                    "Status": {
                        "select": {
                            "name": "To Do"
                        }
                    }
                }
            }
        )

    # Harvest all completed tasks.
    response = requests.post(
        f"https://api.notion.com/v1/databases/{ENV['database_id']}/query",
        headers=HEADERS,
        json={
            "filter": {
                "property": "Status",
                "select": {
                    "equals": "Completed"
                }
            }
        }
    ).json()["results"]

    # Archive all completed tasks.
    for page in response:
        response = requests.patch(
            f"https://api.notion.com/v1/pages/{page['id']}",
            headers=HEADERS,
            json={"archived": True}
        )


if __name__ == "__main__":
    main()
