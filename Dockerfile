FROM python:3.9.16-alpine3.17

WORKDIR /app

COPY ./recommender_ui ./recommender_ui

# Dependencies
# can't install matplotlib on alpine with poetry due to PEP517 error, hence using pip
# https://stackoverflow.com/questions/65569248/how-to-install-matplotlib-on-alpine
RUN pip install --upgrade pip setuptools wheel && \
    apk add --no-cache --virtual .build-deps musl-dev linux-headers g++ gcc zlib-dev make python3-dev jpeg-dev && \
    pip install gradio && \
    apk del .build-deps

EXPOSE 7860

ENTRYPOINT ["python", "./recommender_ui/app.py"]