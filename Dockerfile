FROM python:3.8-alpine
# TODO: Install python3 and python3-pip, hint "apt-get install python3 python3-pip"
#RUN apt-get install python3 python3-pip
#RUN apt-get update && apt-get install -y \
#    python3 \
#    python3-pip
# TODO: Copy application files into container
COPY . /app
# TODO: Install required python libraries
RUN pip install -r /app/requirements.txt
# TODO: Have the container expose port 8080
EXPOSE 8080
CMD python3 /app/app.py
