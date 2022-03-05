# Readme

Install dependencies

```sh
pipenv install
```

Start the project

```
pipenv shell
python app.py
```

## Usage

Save data via

```
PUT /put/<id>
{
    <json blob>
}
```

Read the same data via

```
GET /get/<id>
```
