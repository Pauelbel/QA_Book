""" 
Принцип единственной отвественности (Single Responsibility Principle)

Подразуемевает:
- Что класс должен иметь свою основную ответственность и не должен брать другие ответственности

"""
# Класс журнала
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0
    # Добавление записей в журнал
    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1
    # Удаление записей 
    def remove_entry(self, pos):
        del self.entries[pos]
    # Удобобчитаемое представление записей, для печати или другой обработки
    def __str__(self):
        return "\n".join(self.entries)

# Если необходимо сохранить журнал, луше делать это в одельном классе а не в Journal
# т.к. при сохранении могут быть добавлены дополнительные операции (например проверка прав на сохранение)
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("Первая запись в журнале")
j.add_entry("Последняя запись в журнале")
print(f"Записи в журнале:\n{j}\n")

p = PersistenceManager()
file = r'Design_patterns/SOLID/journal.txt'
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
