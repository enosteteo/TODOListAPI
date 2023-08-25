# Development environment setup

To clone the project run the following comand:
```sh
git clone git@github.com:enosteteo/TODOListAPI.git
```

For the next commands on this page, you must be at the **root** of the project:

## Local case
It's recommended to use a virtual enviroment in development:

```sh
python3 -m venv venv
```

After setup the development is activated through the command:

```sh
source venv/bin/activate
```

To install the required libs, run the following command:

```sh
pip install `cat requirements.txt`
```

## Docker case
Can be possible use the dev container on vscode, or docker-compose for tests:

```sh
docker-compose up 
```

For rebuild and recreate container:

```sh
docker-compose up --build --force-recreate
```