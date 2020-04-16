import pygit2

repo = pygit2.Repository(".")
try:
	repo.index.add_all()
	repo.merge(repo.lookup_reference("FETCH_HEAD").target)
	for thing in repo.index.conflicts:
		print(thing[0].path)
		repo.index.add(thing[2])
finally:
	repo.state_cleanup()