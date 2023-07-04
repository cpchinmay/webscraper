# Use the official MySQL image as the base image
FROM mysql:latest

# Set the root password for the MySQL database
ENV MYSQL_ROOT_PASSWORD=mysecretpassword

# Set the database name
ENV MYSQL_DATABASE=test_bse

# Copy the initialization script to the container
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the default MySQL port
EXPOSE 3306

# Start MySQL service when the container starts
CMD ["mysqld"]
