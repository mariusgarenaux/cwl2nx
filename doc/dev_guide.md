To upload project to pypi :

Update pyproject

```
python -m build
python -m twine upload --verbose --repository pypi dist/cwl2nx-<derniere_version>.tar.gz
```


