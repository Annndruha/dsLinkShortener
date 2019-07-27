#Base image
FROM python:3-alpine

#Add the main dirictory
ADD ./ /home/LinkShortener

#Set that dirictory
WORKDIR /home/LinkShortener

# Addictional libraries for bot
RUN apk add --no-cache --virtual .build-deps \
    openssl-dev \
    libffi-dev \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del --no-cache .build-deps

#Specify the port number the container should expose 
EXPOSE 80

#Run the file
CMD ["python", "__main__.py"]
