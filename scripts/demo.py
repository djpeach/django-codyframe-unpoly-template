# python manage.py runscript demo --script-args dryrun
def run(*args):
    dryrun = "dryrun" in args
    print(f"Hello World! (dryrun: {dryrun}")
