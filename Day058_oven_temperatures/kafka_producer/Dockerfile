#FROM confluentinc/cp-kafka:latest
FROM confluentinc/cp-kafka:latest

# set user to root to allow for package installation
USER root

# install updates
RUN yum update -y
RUN yum install gcc openssl-devel bzip2-devel libffi-devel zlib-devel -y

# add requirements.txt file
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

# install pip and install librarires
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 

 # add main.py file
COPY ./main.py /code/

# run main.py using python
CMD ["python", "main.py"] 
