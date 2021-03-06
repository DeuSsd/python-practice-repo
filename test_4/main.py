"""
Создать классы студент, аспирант.
Студент содержит свойства: номер группы, средний балл.
 Аспирант отличается от студента наличием научной работы
 (название работы в виде строки).

Реализовать в классах следующие методы:
вывести информацию (фио, возраст)
вывести размер стипендии. Если средняя оценка равна 5, то стипендия 8000р для аспиранта и 6000р для студента,
если меньше 5, то стипендия для аспиранта 6000р, для студента 4000р, в других случаях стипендия 0р

Сравнение размера стипендии с другим студентом/аспирантом (больше или меньше)
"""


class Person:
    def __init__(self, fio: str, age: int):
        self._fio: str = fio
        self._age: int = age

    def get_info(self):
        return self._fio, self._age


class Student(Person):
    MARK_EXCELLENT = 5.
    MARK_GOOD = 4.
    MARK_BAD = 2.
    STUDENT_STIPEND_EXCELLENT = 6000
    STUDENT_STIPEND_GOOD = 4000
    STUDENT_STIPEND = 0

    def __init__(self, fio: str, age: int):
        super().__init__(fio, age)
        self._group_number: str = ""
        self._average_mark: float = 0
        self._stipend: float = 0

    def set_average_mark(self, average_mark: float):
        assert self.MARK_BAD <= average_mark <= self.MARK_EXCELLENT, f"Values expect be in range [{int(self.MARK_BAD)}..{int(self.MARK_EXCELLENT)}]"
        self._average_mark = average_mark

    def _count_stipend(self):
        if self._average_mark == self.MARK_EXCELLENT:
            self._stipend = self.STUDENT_STIPEND_EXCELLENT
        elif self._average_mark >= self.MARK_GOOD:
            self._stipend = self.STUDENT_STIPEND_GOOD
        else:
            self._stipend = self.STUDENT_STIPEND

    def get_stipend(self):
        self._count_stipend()
        return self._stipend

    def stipend_lt(self, other):
        return self.get_stipend() < other.get_stipend()

    def stipend_gt(self, other):
        self._count_stipend()
        return self.get_stipend() > other.get_stipend()

    def stipend_eq(self, other):
        self._count_stipend()
        return self.get_stipend() == other.get_stipend()


class Postgraduate(Student):
    STUDENT_STIPEND_EXCELLENT = 8000
    STUDENT_STIPEND_GOOD = 6000
    STUDENT_STIPEND = 0

    def __init__(self, fio: str, age: int):
        super().__init__(fio, age)
        self._research_work: str
