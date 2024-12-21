FROM python:3.12

WORKDIR /app

# copy the requirements folder one level up
COPY requirements/ requirements/
RUN pip install -r requirements/main.txt

COPY ./monolith .

CMD [ "fastapi", "run", "app/main.py", "--proxy-headers", "--port", "8000" ]
