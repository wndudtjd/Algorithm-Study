SELECT name, count(name)
from animal_ins
group by name
having count(name) > 1 # group by 절의 조건절은 having절이다.
order by name