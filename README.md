# Django Backend API

## Overview

This Django application provides a backend API for managing user login and machine data. It includes the following functionalities:

- User login with JWT authentication.
- Access to machine data.
- Adding and updating machine data.

## Project Structure

- `machines_app/models.py`: Defines the models for `User`, `Machine`, and `DynamicData`.
- `machines_app/views.py`: Contains the views for user login and machine data operations.
- `machines_app/utils.py`: Includes utility functions for encoding and decoding JWT.
- `manage.py`: Django's command-line utility for administrative tasks.

## Models

### User

- `employee_id` (CharField): Unique identifier for the user.
- `password_hash` (CharField): Hashed password of the user.
- `role` (CharField): Role of the user (e.g., 'operator', 'supervisor').
- `created_at` (DateTimeField): Timestamp of user creation.

### Machine

- `name` (CharField): Name of the machine.
- `acceleration` (FloatField): Acceleration parameter.
- `velocity` (FloatField): Velocity parameter.

### DynamicData

- `machine_id` (ForeignKey): Reference to the `Machine`.
- `user_id` (ForeignKey): Reference to the `User` who created the data.
- `actual_position_x` (FloatField): X coordinate of the machine's actual position.
- `actual_position_y` (FloatField): Y coordinate of the machine's actual position.
- `actual_position_z` (FloatField): Z coordinate of the machine's actual position.
- `actual_position_a` (FloatField): A axis of the machine's actual position.
- `actual_position_c` (FloatField): C axis of the machine's actual position.
- `distance_to_go_x` (FloatField): Distance to go in the X direction.
- `distance_to_go_y` (FloatField): Distance to go in the Y direction.
- `distance_to_go_z` (FloatField): Distance to go in the Z direction.
- `distance_to_go_a` (FloatField): Distance to go in the A direction.
- `distance_to_go_c` (FloatField): Distance to go in the C direction.
- `homed_x` (BooleanField): Whether the X axis is homed.
- `homed_y` (BooleanField): Whether the Y axis is homed.
- `homed_z` (BooleanField): Whether the Z axis is homed.
- `homed_a` (BooleanField): Whether the A axis is homed.
- `homed_c` (BooleanField): Whether the C axis is homed.
- `tool_offset_x` (FloatField): X axis tool offset.
- `tool_offset_y` (FloatField): Y axis tool offset.
- `tool_offset_z` (FloatField): Z axis tool offset.
- `tool_offset_a` (FloatField): A axis tool offset.
- `tool_offset_c` (FloatField): C axis tool offset.
- `created_by` (CharField): ID of the user who created the data.
- `timestamp` (DateTimeField): Timestamp of data creation.

## JWT Utility Functions

### `encode_jwt(payload, expiration_minutes=30000)`

Encodes a payload into a JWT token with an expiration time.

### `decode_jwt(token)`

Decodes a JWT token and returns the payload.

## API Endpoints

### Login

**POST /login/**

Logs in a user and returns a JWT token. If the user does not exist, a new user is created.

**Request Example:**

```bash
curl -X POST http://localhost:8000/login/ \
-H "Content-Type: application/json" \
-d '{"employee_id": "emp123", "password": "pass123", "role": "operator"}'



- **Create Machine Data**

    ```bash
    curl -X POST http://127.0.0.1:8000/machine \
    -H "Authorization: <jwt_token>" \
    -H "Content-Type: application/json" \
    -d '{
    "name": "Machine_1",
    "acceleration": 10.5,
    "velocity": 200.0,
    "actual_position": {
        "x": 12.5,
        "y": 22.5,
        "z": 35.5,
        "a": 45.5,
        "c": 55.5
    },
    "distance_to_go": {
        "x": 1.5,
        "y": 2.5,
        "z": 3.5,
        "a": 4.5,
        "c": 5.5
    },
    "homed": {
        "x": true,
        "y": false,
        "z": true,
        "a": false,
        "c": true
    },
    "tool_offset": {
        "x": 0.1,
        "y": 0.2,
        "z": 0.3,
        "a": 0.4,
        "c": 0.5
    }
    }'

    ```



## Setup

1. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```


2. **Apply Migrations**
    ```bash
    python manage.py migrate
    ```



3. **Run the Development Server**
    ```bash
    python manage.py runserver
    ```


## note

 ** Please find the url for viewing the data in browser - JWT not required**


```bash
    http://127.0.0.1:8000/api/machines/details
    ```