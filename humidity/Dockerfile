# Set base image
FROM python:3.6-alpine

# Create new user and set working directory
RUN adduser -D humidity
WORKDIR /home/humidity

# Install requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy source code
COPY data_loader.py cache.py ./

# Make boot executable
RUN chmod +x data_loader.py

# Set files owner
RUN chown -R humidity:humidity ./
USER humidity

# Set run command
CMD "python3" "data_loader.py"