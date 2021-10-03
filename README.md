# NotionAutomations

This repo is a set of personal automations using the [Notion Rest API](https://developers.notion.com/reference/intro).


# Automations

- revert-daily-tasks -> Acts on a Kanban board database to revert all "Daily" tasks to "To Do" status. Deletes all non-Daily "Completed" tasks.


# Development

To work on one of these automations, perform the following:

1. Install Docker
2. cd into the root folder of the automation you wish to work on.
    - Example: To work on the "Revert Daily Tasks" automation, move into the "revert-daily-tasks" directory of this repo.
3. Create a file named env.json that matches the sample-env.json provided.
4. Run the following command:
```docker
docker run -it -v "$(pwd)":/notion-automations python:3.9 bash
```
5. You now have a fully built development environment!


# Helpful documentation when working with Notion Rest API

[Notion Rest API](https://developers.notion.com/reference/intro)
[Find your database ID](https://developers.notion.com/docs/working-with-databases)