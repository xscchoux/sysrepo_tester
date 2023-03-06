FROM debian:buster

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -qy build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev


# Install Python 3.10 on Debian 11 / Debian 10
# https://computingforgeeks.com/how-to-install-python-on-debian-linux/
RUN wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz && \
    tar -xf Python-3.10.*.tgz && \
    cd Python-3.10.*/ && \
    ./configure --enable-optimizations && \
    make -j 4 && \
    make altinstall

RUN DEBIAN_FRONTEND=noninteractive apt install -qy python3-pip vim git

# Install libyang
RUN DEBIAN_FRONTEND=noninteractive apt install -qy cmake libpcre2-dev doxygen libcmocka-dev valgrind && \
    git clone https://github.com/CESNET/libyang.git && \
    cd libyang && \
    mkdir build && cd build && \
    cmake .. && \
    make && \
    make install
    
RUN pip3 install libyang

# Install sysrepo
RUN DEBIAN_FRONTEND=noninteractive apt install -qy tar pkg-config libsystemd-dev && \
    git clone https://github.com/sysrepo/sysrepo.git && \
    cd sysrepo && \
    mkdir build && cd build && \
    cmake .. && \
    make && \
    make install
    
RUN pip3 install sysrepo

RUN ldconfig

COPY install_yang.py delete_yang.py /home/
COPY OpenROADM_MSA_Public /home/OpenROADM_MSA_Public
