from fabric.api import local

host = 'jasonrhaas.com'

def test():
	local("jekyll serve --watch")

def prep():
    local("git add -p && git commit")
    local("git push")

def deploy():
	local("jekyll build")
	local("scp -r _site jasonrhaas.com:~")