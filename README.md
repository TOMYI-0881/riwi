# Student Management System

## Description

A console-based student registry system built in pure Python (no external libraries). Allows registering, searching, updating and deleting students, with automatic CSV persistence on every write operation.

## Requirements

- Python 3.10 or higher
- No additional dependencies required

## How to Run

```bash
python app.py
```

## Features

| Option | Description |
|--------|-------------|
| 1 | Register a new student |
| 2 | Show all students |
| 3 | Search student by ID or name |
| 4 | Update student data |
| 5 | Delete student |
| 6 | Statistics |
| 7 | Exit |

## Student Fields

| Field  | Type | Description |
|--------|------|-------------|
| id     | int  | Unique identifier — entered manually, no duplicates allowed |
| name   | str  | Full name — normalized, no duplicates allowed |
| age    | int  | Between 1 and 120 |
| course | str  | Course or program name |
| status | str  | `active` or `inactive` |

## Validation Rules

- **No duplicate IDs** — the system rejects registration if the ID already exists.
- **No duplicate names** — full names are normalized before comparison: extra spaces are removed and the result is compared in Title Case.
- **Auto-save** — every add, update, or delete immediately overwrites `base_memory_csv/data_base/students.csv`.
- **Auto-load** — on startup the system reads from CSV and restores the previous session automatically.

## Project Structure

```
student-system/
├── app.py
├── estructure/
│   └── model_data.py
├── crud/
│   └── service.py
├── ui_interaction/
│   └── ui.py
├── base_memory_csv/
│   ├── memory_csv_endoinsts.py
│   └── data_base/
│       └── students.csv
└── README.md
```
