# Docker Assignment

This project demonstrates the use of Docker containers to build a simple data producer-consumer architecture. The Data Producer generates random data (logs or numbers), and the Data Consumer listens for the data, stores it persistently using Docker volumes.

## Project Structure

- `docker-compose.yml` - The Docker Compose configuration to run the project.
- `dockerfile.producer` - Dockerfile for the Data Producer container.
- `dockerfile.consumer` - Dockerfile for the Data Consumer container.
- `producer.py` - Python script for the Data Producer.
- `consumer.sh` - Shell script to run the Data Consumer.
 
Running the Project:

Clone the Repository

Clone the repository to your local machine:

and build the docker-compose.yml file

you surely have docker and docker-compose installed
