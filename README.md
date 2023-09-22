# PLD Huddlr

PLD Huddlr is a web application designed to simplify peer collaboration and scheduling for learners in the ALX Intro to Software Engineering program. It allows learners to efficiently coordinate meeting arrangements based on their availability and shared concepts of interest, fostering effective knowledge exchange.

## Features

- User authentication using OAuth for ALX program participants.
- User profile setup and management.
- Availability input and tracking.
- Meeting scheduling functionality.
- Matching algorithm considering availability and concepts of interest.
- Meeting notification & reminder functionality
- Integration with PLD meeting rooms (ALX intranet communication tool).

## Technologies Used

- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Backend:** Flask
- **Database:** MySQL
- **Authentication:** OAuth
- **Cloud Hosting (To Be Decided):** [Cloud Hosting Platform]
- **Database Hosting (To Be Decided):** [Database Hosting Service]

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine:
  ```
   git clone https://github.com/yahaiii/pld_huddlr.git
   ```
2.  Navigate to the project directory:
```
cd pld_huddlr
```

3.  Create and activate a virtual environment (optional but recommended):
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```

4.  Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

3.  Run the application:
    ```
    flask run
    ```
This will open the application in your browser at http://localhost:5000/.


## License
This project is licensed under the MIT License.


## Contributing

We welcome contributions to enhance the PLD Huddlr project. Feel free to submit issues, feature requests, or pull requests.