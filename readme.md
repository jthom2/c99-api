<p align="center">
<br><br><br>
<a https://api.c99.nl/"><img src="https://api.c99.nl/assets/images/logo.png" width="100px"></a>
<br><br><br>
</p>

<p align="center">
<b>Seamlessly integrate the c99.nl API into your Python projects</b>
</p>

<p align=center>
<a href="https://pypi.org/project/c99-api/"><img src="https://img.shields.io/pypi/v/c99-api.svg"></a>
<!-- <a href="https://pypistats.org/packages/c99-api"><img src="https://pepy.tech/badge/c99-api"></a> -->
<a href="https://discord.gg/rR6xkP6rJu"><img src="https://img.shields.io/badge/Discord-700-blueviolet?logo=discord&amp;logoColor=white&style=round">

# Installation

```
pip install c99-api
```

# Usage

```python
# Import the package
import c99-api

# Define your API key
c99_api.key = 'your_key'
```

```python 
# Access list of different methods available
response = c99.list_methods()
print(response)
```

```python
# Example Methods

# Phone lookup
response = c99.phonelookup(number='1234567890', json=True)
print(response)

# Email validation
response = c99.emailvalidator(email='example@example.com', json=True)
print(response)

# Port scanner
response = c99.portscanner(host='example.com', json=True)
print(response)
```

## Other Docs

[API Overview](https://api.c99.nl/dashboard/api_overview)