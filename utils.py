# Импорт JSON
import json


# Функция, загружающая данные из файла
def load_candidates():
    with open("candidates.json", "r", encoding="utf-8") as file:
        list_candidates = json.load(file)
    return list_candidates


# Функция, возвращающая список всех кандидатов
def load_candidates_from_json():
    all_candidates = []
    candidates = load_candidates()
    for candidate in candidates:
        all_candidates.append(candidate['name'])
    return all_candidates


# Функция, возвращающая кандидата по id
def get_candidate(candidate_id):
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate


# Функция, возвращающая кандидата по имени
def get_candidates_by_name(candidate_name):
    candidates = load_candidates()
    candidates_with_name = []
    for candidate in candidates:
        names = candidate['name'].split()
        for name in names:
            if str(candidate_name).lower() == name.lower():
                candidates_with_name.append(candidate)
    return candidates_with_name


# Функция, возвращающая кандидата по навыку
def get_candidates_by_skill(skill_name):
    candidates = load_candidates()
    candidates_with_skills = []
    for candidate in candidates:
        skills = candidate['skills'].split(", ")
        for skill in skills:
            if str(skill_name).lower() == skill.lower():
                candidates_with_skills.append(candidate)
    return candidates_with_skills
