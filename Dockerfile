FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /alumnusb_code
COPY requirements.txt /alumnusb_code/
RUN pip install -r requirements.txt
COPY . /alumnusb_code/
