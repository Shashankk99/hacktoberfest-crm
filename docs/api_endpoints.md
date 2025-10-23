# API Endpoints

This document describes the available endpoints in the Hacktoberfest CRM Flask API.

## GET /contacts

- **Description**: Retrieve the list of contacts.
- **Response**: Returns a JSON array of contact objects with `name` and `email` fields.

Example response:

```json
[
  {"name": "Alice", "email": "alice@example.com"},
  {"name": "Bob", "email": "bob@example.com"}
]
```

## POST /contacts

- **Description**: Add a new contact. The request body should be JSON with `name` and `email` fields.
- **Response**: Returns the newly created contact object.

Example request:

```json
{
  "name": "Charlie",
  "email": "charlie@example.com"
}
```

Example response:

```json
{"name": "Charlie", "email": "charlie@example.com"}
```

Feel free to propose additional endpoints or improvements as part of your contributions. See the CONTRIBUTING.md file for more details.
