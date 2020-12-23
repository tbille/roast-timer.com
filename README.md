# ![roast-timer.com](https://roast-timer.com/assets/timer-logo.png "roast-timer.com") Coffee roast timer

This timer is made for home coffee roaster that want to log their roasts. I use this site when roasting on y [Gene Café CBR-101](https://www.genecafe.eu/gene-cafe-cbr-101.php).

This is the repository for the site [roast-timer.com](https://roast-timer.com).

## Run the project

- Install ruby. On Ubuntu:

```
$ sudo apt -y install make build-essential ruby ruby-dev
$ vim ~/.bashrc
# Add the lines
export GEM_HOME=$HOME/gems
export PATH=$HOME/gems/bin:$PATH

$ source ~/.bashrc
$ gem install jekyll bundler
```
- Run the project locally
```
$ bundle install
$ bundle exec jekyll serve
```
- Access http://localhost:4000