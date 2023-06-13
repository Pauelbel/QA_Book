#### Консольные команды

|                        |                          |
| ---------------------- | ------------------------ |
| `--log-cli-level=INFO` | Запустить журналирование |


|            |                            |
| ------------------ | -------------------------------------------- |
| `--lf`             | Запустить последние упавшие тесты            |
| `--collect-only`   | Собрать информацию о тестах                  |
| `-x / --maxfail=n` | Остановить тесты после 1-го или n-го падения |

#### Параметризация

|                          |                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------- |
| @pytest.mark.skip        | всегда пропускать тест                                                           |
| @pytest.mark.skipif      | Пропускать тест при выполнении условия                                           |
| @pytest.mark.xfail       | Тест не должен проходить и pytest будет воспринимать это как ожидаемое поведение |
| @pytest.mark.parametrize | многократный запуск теста с параметрами                                          |
| @pytest.mark.usefixtures | использовать указанный список фикстур                                            |
| @pytest.mark.parametrize | позволяет использовать параметризацию на уровне тестовой функции                 |
| @pytest.mark.fixture     | позволяет использовать парамтризацию на уровне фикстур                           |
| @pytest_generaate_tests  | позволяет релизовать custom-схему динамической парамтризации                     |