shevrole_owner = {'sam', 'edit', 'semen', 'petr'}
work_near = {'konstantin', 'vladislav', 'sam', 'petr', 'edit'}
live_near = {'john', 'vladislav', 'olga', 'mike', 'grant', 'covid', 'bilbo' }
live_and_work = work_near.union(live_near)
print(live_and_work)
owner_and_live_and_work = shevrole_owner.intersection(live_and_work)
print(owner_and_live_and_work)