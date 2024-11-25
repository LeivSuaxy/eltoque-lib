# ElToque Class

Class with methods to make requests to the ElToque API (Cuba).

## How to use
Open your virtual enviroment and install dependencies

_Create Virtual Environment_
```python
python -m venv .venv   
```
If you use Linux remember to use python3

<br/>

_Activate Virtual Environment_
### Linux
```bash
source .venv/bin/activate
```

### Windows
```bash
.venv\Scripts\activate
```

_Install Dependencies_
```python
pip install -r requirements.txt
```

## Docs

### get_today()
Returns the exchange rates for the current date.

### get_date(date: str)
Date parameter in format (YYYY-MM-DD)

Returns the exchange rates of the given date.



