# PHPDoc Example

To generate phpDocumenter files for this code, run:

```bash
composer install
vendor/bin/phpdoc -d ./ --ignore "vendor/" -t ./docs
```

The generated files will be found in the `docs/` directory.

More info: [phpDocumentor](https://www.phpdoc.org/)
