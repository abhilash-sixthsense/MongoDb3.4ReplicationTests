Setup
-------
1)Install docker compose
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose

2)Build the testclient
    cd to testclient directory
    sudo docker build -t python-test-client .

3)cd back to the parent directory and run the docker compose and all the services will be started
    sudo docker-compose up


4)cd to testclient and run run.sh. This will give you a terminal access to python container. from there run the following.
    python test.py
