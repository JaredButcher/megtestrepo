import pygit2

repo = pygit2.Repository(".")
try:
	repo.index.add_all()
	repo.merge(repo.lookup_reference("FETCH_HEAD").target)
	for thing in repo.index.conflicts:
		for thing2 in thing:
			if not thing2 is None:
				print(thing2.path)
			else:
				print("NONE")
		repo.index.add(thing[2])
	repo.index.write()
	repo.create_commit('HEAD', repo.default_signature, repo.default_signature, "AHH43", repo.index.write_tree(), [repo.head.target])
finally:
	repo.state_cleanup()