# Use AWS ECR public image to avoid Docker Hub rate limits
FROM public.ecr.aws/docker/library/python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "application.py"]
