# PyToque Class

Class with methods to make requests to the ElToque API (Cuba).

## How to use
Primero necesitaras solicitar un token personal desde el sitio de ElToque. 

### Explanation
https://eltoque.com/eltoque-abre-acceso-a-su-api-de-las-tasas-de-cambio

### Form to obtain token
https://tasas-token.eltoque.com/

Open your virtual environment and install dependencies

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

_Import the PyToque class and initialize it by sending the api_key obtained on the official ElToque site as a parameter._

**Warning** Remember to be careful with the privacy of your personal token.

```python
from pytoque.core import PyToque

toque = PyToque(api_key=API_KEY)
```

## Docs

### get_today() -> dict
Returns the exchange rates for the current date.

### get_date(date: str) -> dict
Date parameter in format (YYYY-MM-DD)

Returns the exchange rates of the given date.



