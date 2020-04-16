import pygit2

repo = pygit2.Repository(".")
try:
	repo.index.add_all()
	repo.merge(repo.lookup_reference("FETCH_HEAD").target)
	print(repo.index.conflicts.keys)
	for thing in repo.index.conflicts:
		print(thing)
finally:
	repo.state_cleanup()