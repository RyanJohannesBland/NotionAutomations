""" Move all Completed Daily tasks back to To-Do in Notion Kanban board. """
import json
import requests


with open("function/env.json", 'r', encoding="UTF-8") as env_file:
    ENV = json.loads(env_file.read())
HEADERS = {
    "Authorization": f"Bearer {ENV['token']}",
    "Notion-Version": "2021-08-16"
}


def main(_, __):
    """
        Grab all "Daily" Type tasks and set them to "To-Do" status. Then grab
        all remaining "Completed" status tasks and delete them.
    """
    # Harvest all daily tasks.
    response = requests.post(
        f"https://api.notion.com/v1/databases/{ENV['database_id']}/query",
        headers=HEADERS,
        json={
            "filter": {
                "or": [
                    {
                        "property": "Type",
                        "select": {
                            "equals": "Daily"
                        }
                    },
                    {
                        "property": "Type",
                        "select": {
                            "equals": "Morning Routine"
                        }
                    }
                ]
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


# Test locally by running "python revert-daily-todos/revert_dailies.py".
if __name__ == "__main__":
    main(None, None)
