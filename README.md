# Habits API (Flask)

A simple RESTful API for tracking daily habit check-ins.  
Built with Python and Flask, using an **in-memory store** (data resets when the server restarts).

## Features

- Create a new habit check-in (`POST /habits`)
- List all habit check-ins (`GET /habits`) *(to be implemented)*
- Get a single habit by ID (`GET /habits/<id>`) *(to be implemented)*
- Update a habit by ID (`PUT /habits/<id>`) *(to be implemented)*
- Delete a habit by ID (`DELETE /habits/<id>`) *(to be implemented)*

Each habit has:

```json
{
  "id": 1,                // server-assigned
  "name": "Read Bible",
  "date": "11-16-2026",
  "completed": false,
  "notes": "3 more passages in Enjoy Life Forever! brochure"
}