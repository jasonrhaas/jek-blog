from fabric.api import local

host = 'jasonrhaas.com'

def prep():
	print "Make sure to commit changes and push!"

def deploy():
	local("jekyll build")
	local("scp -r _site jasonrhaas.com:~")