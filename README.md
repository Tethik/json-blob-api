# Readme

Install dependencies

```sh
pipenv install # or
pip install -r requirments.txt
```

Start the project

```sh
pipenv shell # if using pipenv
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
