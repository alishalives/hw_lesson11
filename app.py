# Импорт flask и рендера
from flask import Flask, render_template

# Импорт функций
import utils

# Создаем экземпляр Flask
app = Flask(__name__)


# Создаем представление главной страницы со списком всех кандидатов
@app.route('/')
def first_page():
    candidates = utils.load_candidates()
    return render_template("list.html", candidates=candidates)


# Создаем представление страницы /candidate/<x> с выводом данных про кандидата <x>
@app.route('/candidate/<x>')
def candidate_page(x):
    candidate = utils.get_candidate(int(x))
    return render_template("card.html", candidate=candidate)


# Создаем представление страницы /search/<candidate_name> с выводом кандидатов с <candidate_name>
@app.route('/search/<candidate_name>')
def get_candidate(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    len_candidates = len(candidates)
    return render_template("search.html", candidates=candidates, len_candidates=len_candidates)


# Создаем представление страницы /skill/<skill_name> с выводом кандидатов с <skill_name>
@app.route('/skill/<skill_name>')
def get_candidate_by_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates)


app.run()
