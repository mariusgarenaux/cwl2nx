What to do for building the package and the app

The cli app does not need specific treatment. Just publish the package as usual.

> ⚠️ There might be a small delay on pipx before update is made with pypi (< 1 min)

## documentation for cli app :

https://packaging.python.org/en/latest/guides/creating-command-line-tools/

## documentation for building python packages :

```bash
python -m build
```

```bash
python -m twine upload --verbose --repository pypi dist/<package_name>-<last_version>.tar.gz
```
