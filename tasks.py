from invoke import task

# Doesn't use index.py yet. This will be fixed.
@task
def start(ctx):
    ctx.run("python3 -m src.ui.ui", pty=True)

@task
def test(ctx):
    ctx.run("PYTHONPATH=. pytest -s -v src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)