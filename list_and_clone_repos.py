import pygithub3
import re
import os
import sys

gh = None

def gather_clone_urls(organization, no_forks=True):
    all_repos = gh.repos.list(user=organization).all()
    for repo in all_repos:
        # Don't print the urls for repos that are forks.
        if no_forks and repo.fork:
            continue
        yield repo.clone_url


class Clone():
    def repo_selection(self):
        self.repo = raw_input("Enter the repo you wish to clone:")
        if self.repo in list2:
            self.repo_link1 = 'https://github.com/%s/%s.git' %(user,self.repo)
            self.repo_link2 = 'git@github.com:%s/%s.git' %(user,self.repo)
            self.path = raw_input("Enter the path you wish to clone the repo:")
            os.chdir(self.path)
        else:
            print("This repo is not present in your git:")
            self.repo_selection()

    def choice_of_cloning(self):
        self.ch = int(raw_input("Enter the choice you wish to clone the repo\n 1. HTTP \n 2. SSH \n"))
        if self.ch == 1:
            os.system("git clone %s" %(self.repo_link1))
        elif self.ch == 2:
            os.system("git clone %s" %(self.repo_link2))
        else:
            print("Wrong choice, Please Try Again:")
            self.choice_of_cloning()

gh = pygithub3.Github()
user = raw_input("Enter the user_name:")
clone_urls = gather_clone_urls(user)
file = open("git_links.txt","w")
print("The following are the list of repo url's present in your git:")
for url in clone_urls:
    file.write(url)
    print url


with open('git_links.txt', 'r') as file:
     links = file.read()

list1 = []
obj = re.findall(r'([a-zA-Z_]*)(\.git)',links)
for x in obj:
    y = list(x)
    for z in y:
        list1.append(z)

set1 = set(list1)
list2 = list(set1)
list2.remove('.git')

print("The following are the list of repos present in your git:")
for x in list2:
    print(x)

clone = Clone()
clone.repo_selection()
clone.choice_of_cloning()
