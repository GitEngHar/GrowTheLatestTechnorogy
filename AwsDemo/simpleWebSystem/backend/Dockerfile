from python:3.8
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD ["uvicorn","backend:app","--reload","--host","0.0.0.0"]