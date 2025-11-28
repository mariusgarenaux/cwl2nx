## Build and upload package

To upload project to pypi :

Update pyproject.toml file

Run :

```
python -m build
python -m twine upload --verbose --repository pypi dist/cwl2nx-<derniere_version>.tar.gz
```

> `pip install build` and `pip install twine`

## CLI app

The cli app does not need specific treatment. Just publish the package as usual.

> ⚠️ There might be a small delay on pipx before update is made with pypi (< 1 min)

### Documentation for cli app :

https://packaging.python.org/en/latest/guides/creating-command-line-tools/
