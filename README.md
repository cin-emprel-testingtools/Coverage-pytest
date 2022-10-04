# Coverage-pytest

## install

- pip install pytest
- pip install pytest-cov

Run Report in html with branch cov active
```bash
pytest --cov-report html:cov_html --cov-branch  --cov=codigo

```
Ou

```bash

pytest --cov=codigo --cov-report=html --cov-branch

```

onde:

--cov=codigo = diretorio onde o test ira cobrir
--cov-report=html = formato do relatorio que será gerado
--cov-branch = ativa test de branch
