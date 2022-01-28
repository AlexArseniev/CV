from dao.cv_repository import CvRepo
from entity.cv import CV

if __name__ == '__main__':
    first_cv = CV('Alex', 'Petrov', '33', '06.12', '08765431', 'M', 'BG', 'Treta gluha', 'High', '5 years',
                  f"{'Python', 'C', 'C++'}")

    second_cv = CV('Misho', 'Kunchev', '43', '03.22', '045765431', 'M', 'BG', 'Iabulkova gradina', 'High school',
                   '1 year', f"{'JS', 'CSS'}")

    third_cv = CV('Karabas', 'Barabas', '100', '01.30', '66666666', 'M', 'ITL', 'Tri ushi', 'None',
                  '40 years', f"{'HTML', 'SQL'}")

    cvs = (first_cv, second_cv, third_cv)
    cvs_repo = CvRepo()

    for cv in cvs:
        cvs_repo.create(cv)

    for current_cv in cvs_repo.find_all():
        print(current_cv)
