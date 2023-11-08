# Webserver Documentation

The `Webserver` class is a cog that implements a web server using the `aiohttp` library in order to handle specific routes and actions.

## Class Methods

### `__init__(self, bot: commands.Bot) -> None`

Constructor for the `Webserver` class. Receives a `bot` parameter of type `commands.Bot` and assigns it to the `bot` attribute.

### `webserver(self)`

The main method that sets up and starts the web server. This method creates various handlers for specific routes and actions. These handlers are defined as nested functions inside the `webserver()` method. The web server is run on `localhost` and listens on port `8080`.

### `__unload(self)`

Cleanup method that stops the web server when the cog is unloaded.

### `authenticate_extension(self, interaction: discord.Interaction)`

Command method that handles the `/authenticate-extension` slash command. It retrieves the user associated with the interaction and creates a new user if it doesn't exist. It then sends a private message to the user with an authentication link that needs to be used in the extension.

## Routes and Handlers

The web server defines the following routes and handlers:

### `/` - `root_handler(request: web.Request) -> web.Response`

- Method: GET
- Handler: `root_handler`
- Description: Returns a "Hello, world" response.

### `/tasks/{token}` - `get_task_handler(request: web.Request) -> web.Response`

- Method: GET
- Handler: `get_task_handler`
- Description: Retrieves the tasks associated with a user identified by their token. Returns the tasks as a JSON array.

### `/tasks/{token}` - `post_task_handler(request: web.Request) -> web.Response`

- Method: POST
- Handler: `post_task_handler`
- Description: Updates the status of a task provided in the request payload. Expects the task ID and an action ("start" or "completed"). Returns "OK" if the update is successful.

### `/generate-documentation` - `generate_documentation_handler(request: web.Request) -> web.Response`

- Method: POST
- Handler: `generate_documentation_handler`
- Description: Generates documentation based on the content provided in the request payload. Returns the generated documentation as a JSON response.

### `/push-to-github` - `push_to_github_handler(request: web.Request) -> web.Response`

- Method: POST
- Handler: `push_to_github_handler`
- Description: Pushes content to a specified GitHub repository and branch. Expects the content, file path, and repository URL in the request payload. Returns the URL of the created file.

### `/webhook` - `webhook_handler(request: web.Request) -> web.Response`

- Method: POST
- Handler: `webhook_handler`
- Description: Handles GitHub webhook events. Parses the event type and repository information from the request payload. Sends a message to the corresponding Discord channel with information about the event.

## Setup Function

### `setup(bot: commands.Bot) -> None`

This function is used to add the `Webserver` cog to the bot and create an instance of it. It also schedules the `webserver()` method to run as a task in the bot's event loop.