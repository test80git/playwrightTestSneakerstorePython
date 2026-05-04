# Test

## Если тест в классе

```bash
pytest tests/test_login.py::TestLogin::test_discount -v --alluredir=allure-results
```

## По имени функции
```bash
pytest tests/test_login.py::test_discount -v --alluredir=allure-results
```


## По ключевому слову (части имени)
```bash
pytest tests/test_login.py -k "discount" -v --alluredir=allure-results
```


## По маркеру (если есть @pytest.mark.smoke)
```bash
pytest tests/test_login.py -m smoke -v --alluredir=allure-results
```

## 📝 Примеры:
```bash
# Простой тест
pytest tests/test_login.py::test_discount -v --alluredir=allure-results

# Тест в классе
pytest tests/test_login.py::TestLogin::test_discount -v --alluredir=allure-results

# С выводом print
pytest tests/test_login.py::test_discount -v -s --alluredir=allure-results
```


