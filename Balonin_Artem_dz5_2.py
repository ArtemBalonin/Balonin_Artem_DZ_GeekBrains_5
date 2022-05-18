import sys
tutors = [
    "Иван", "Анастасия", "Петр", "Сергей",
    "Дмитрий", "Борис", "Елена"
]
klasses = [
    '9А', '7В', '9Б', '8Б',
    # '9В', '10А', '10Б', '9А'
]

def my_zip_gen():
    len_klasses = len(klasses)
    return ((tutors, klasses[i]) if i < len_klasses else (tutors, None)
            for i, tutors in enumerate(tutors))
gen = my_zip_gen()
print(type(gen), sys.getsizeof(gen), *gen)