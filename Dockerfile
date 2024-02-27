FROM python:3.11
RUN mkdir /bot
COPY ./requirements.txt /bot
RUN pip install -r /bot/requirements.txt --no-cache-dir
COPY . /bot
WORKDIR /bot
CMD ["python3", "app.py"]