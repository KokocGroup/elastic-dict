from fabric.api import local, task, quiet


@task
def release():
    with quiet():
        version = local("cat version", capture=True).strip().split('.')
        version[-1] = str(int(version[-1]) + 1)
        new_version = '.'.join(version)
        local("echo {} > version".format(new_version))
        local('git commit -am "new version {}"'.format(new_version))
        local('git tag -a v{0} -m \'Release version {0}\''.format(new_version))
        local('git push origin master --tags')
    local("python setup.py register -r pypi")
    local("python setup.py sdist upload -r pypi")