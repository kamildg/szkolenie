from collections import defaultdict


class World_cup:
    def __init__(self):
        self._team = {}

    def add_team(self, name):
        self._team[name] = defaultdict(list)

    def report_grade(self, name, group, scored,lost, matches):
        by_subject = self._team[name]
        grade_list = by_subject[group]
        grade_list.append((scored,lost, matches))


    def average_grade(self, name):
        by_subject = self._team[name]

        score_sum, score_count = 0, 0
        for group, total in by_subject.items():
            scored_avg, lost_avg = 0, 0
            for scored,lost, matches in total:
                scored_avg += scored / matches
                lost_avg += lost / matches

        score_sum += scored_avg
        score_count += lost_avg
        return name, group, f'ilosc strzelonych goli {scored}',f'ilość straconych goli {lost}', f'ilość rozegranych meczy {matches}', f'Średnia strzelonych {score_sum}' , f'rednia straconych {score_count}'


book = World_cup()
book.add_team('Argentyna')
book.report_grade('Argentyna','grupa 1', 15, 13, 3)
print(book.average_grade('Argentyna'))
book.add_team('Polska')
book.report_grade('Polska','grupa 1', 15, 13, 3)
print(book.average_grade('Polska'))
book.add_team('Meksyk')
book.report_grade('Meksyk','grupa 1', 5, 7, 3)
print(book.average_grade('Meksyk'))
