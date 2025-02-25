# IOT Sensor Data Visualization

## Overview

This project is a web application built using the Django framework to visualize IoT sensor data. It retrieves data from a local database, processes it, and displays it in a user-friendly interface.  Originally, the application fetched data from an external cloud API, but it has been redesigned to operate independently.

## Project Description

This application was initially designed to fetch sensor data from an external cloud API but has been upgraded to a standalone system. The hardware components (Nodemcu, Raspberry Pi, Bluetooth modules, and ultrasonic sensors) collect data and send it to the application's local database.

## Functionalities

*   Retrieves sensor data and stores it locally.
*   Cross-checks incoming data with the local database and updates it accordingly.
*   Displays real-time sensor data through a web interface.

## Updates and Improvements

*   **Removed external cloud API dependencies:** The project no longer relies on third-party cloud storage, improving security and performance.
*   **Made the project standalone:** The application now fetches and processes data locally.
*   **Fixed early mistakes:** Issues with improper data handling and broken links from early development have been corrected.
*   **Utilized AI for restoration:** Artificial intelligence was used to restore and refine the project, improving code quality and structure.
*   **Improved deployment:** The project now runs successfully on GitHub Codespaces.

## Hosting Information

Previously, the application was hosted on PythonAnywhere: [Visit the old web application](link-to-old-application)  *(Replace with actual link)*

Currently, it runs seamlessly in GitHub Codespaces.

## Instructions to Run on GitHub Codespaces

### Open the Repository in Codespaces

1.  Go to your GitHub repository.
2.  Click on "Code" → Select "Codespaces" → Click "Create codespace on main" (or the branch you want to work on).

### Setup the Environment

Once the Codespace is ready, open the terminal and run the following commands:

```bash
source virtenv/bin/activate
```

### Run the Django Development Server
```Bash

python manage.py runserver
```
### Preview the Application
* Click on "Ports" (bottom panel in Codespaces).
* Locate the running port 8000 and click "Make Public" to allow access.
* Click the generated URL to open the application in the browser.

### Key Updates in This Version
* Standalone Application: Removed external API calls; now fetching sensor data from a local database.
* Improved Robustness: Fixed old links, refined the database logic, and made the project more efficient.
* AI-Assisted Restoration: Used AI to bring back the project, improving code quality and structure.
* Runs Successfully on Codespaces: No additional cloud dependencies; everything runs directly within Codespaces.
* Contact
*  ** For clarifications, please contact: giripranay.kona@gmail.com**


