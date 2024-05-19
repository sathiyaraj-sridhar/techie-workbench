# Techie Workbench, Tailor-Made for Exploring AWS

This application is designed to demonstrate how to deploy an application on the AWS cloud and integrate AWS services using the AWS SDK.


## App Setup


### Install

- Download the source code.

```bash
git clone https://github.com/sathiyaraj-sridhar/techie-workbench.git
cd techie-workbench
```

- Create a virtual environment. If you don't have `venv` module instale it by running `python3 -m pip install virtualenv`.

```bash
python3 -m venv venv
source venv/bin/activate
```

- Install required Python packages.

```bash
python -m pip install -r source/requirements.txt
```


### Configure

- Export the AWS profile to ensure the AWS SDK uses those credentials.

```
export AWS_PROFILE='bob'
export AWS_DEFAULT_REGION=us-west-2
```


### Start

- Run the application. Ensure you are in the `source` directory.
```bash
python source/app.py
```


### Stop
- The app is running in the foreground. Press CTRL+C (SIGINT) to gracefully terminate the foreground process.


## Redis Setup


### Install

- Ensure that the necessary dependency packages are available on your system to build Redis from source.

```
sudo dnf install make,gcc
```

- Download the Redis source archive and install it.

```
cd /tmp
curl -O https://download.redis.io/redis-stable.tar.gz
tar -xzvf redis-stable.tar.gz
cd redis-stable
make
sudo make install
```


### Start

- Run the Redis in-memory database.

```
redis-server --protected-mode no
```

- Verify client connections.

```
redis-cli CLIENT LIST
```


### Stop
- The Redis is running in the foreground. Press CTRL+C (SIGINT) to gracefully terminate the foreground process.
