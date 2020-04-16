import pygit2

repo = pygit2.Repository(".")

repo.index.add_all()
repo.merge(repo.lookup_reference("FETCH_HEAD").target)
for thing in repo.index.conflicts:
	print(thing)