To upload project to pypi :

Update pyproject.toml file

Run :
```
python -m build
python -m twine upload --verbose --repository pypi dist/cwl2nx-<derniere_version>.tar.gz
```

> `pip install build` and `pip install twine`