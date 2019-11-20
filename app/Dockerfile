# Set base image
FROM python:3.6-alpine

# Create new user and set working directory
RUN adduser -D api
WORKDIR /home/api

# Install requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

# Copy source code
COPY app.py cache.py boot.sh ./

# Make boot executable
RUN chmod +x boot.sh

# Set flask application
ENV FLASK_APP app.py

# Set files owner
RUN chown -R api:api ./
USER api

# Set port
EXPOSE 5000

# Set run command
ENTRYPOINT ["./boot.sh"]