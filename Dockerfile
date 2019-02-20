FROM osrf/ros:kinetic-desktop-full
USER root
RUN apt-get update && apt-get install -y \
    apt-utils\
    locales \
    tmux \
    bash \
    curl \
    wget \
    vim \
    emacs24 \
    sudo \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    mesa-utils \
    unzip \
    && rm -rf /var/likb/apt/lists/*

RUN apt-get install -y \
    ros-kinetic-rosbridge-server \
    ros-kinetic-rosbridge-suite

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

RUN mkdir /home/ros_ws
ADD . /home/ros_ws
ADD ./entrypoint.bash /

RUN ["/bin/bash", "-c", "/home/ros_ws/build.bash"]

