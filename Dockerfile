FROM alpine:3.12
ENV PYTHONUNBUFFERED=1

RUN echo "**** install Python ****" && \
    apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

# Creating working folder for docker
WORKDIR /app

#Copying application files from source to docker folder
COPY /src/ /app

#Copying test folder
COPY /test/ /app/test


#Installing dependencies 
RUN pip3 --no-cache-dir install -r requirements.txt

#Opening port to enable api interaction 
EXPOSE 80

# Running application
ENTRYPOINT ["python3"]
CMD ["server.py"]  
 
