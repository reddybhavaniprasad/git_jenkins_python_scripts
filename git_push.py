import os
import sys
import re

""" Committing and Pushing the changes """
def commit_process():
        commit = ['y','Y','yes','Yes','YES']
        leave = ['n','N','no','No','NO']
        option = raw_input("Do you want to commit the changes(y/n):")
        if option in commit:
                os.system('git commit -m "updated the feauture"')
                os.system('git push origin master')
                print("committing and pushing are done")
        elif option in leave:
                print("Changes are made but not committed")
        else:
                print("Invalid option- Try again")
                commit_process()

""" To make list of lists into a single list """
def list_of_lists_to_single_list(list1):
	list2 = []
        for x in list1:
                if type(x) == type([]):
                        for l in x:
                                list2.append(l)
                else:
                        list2.append(x)

        list2 = set(list2)
        list2 = list(list2)
	return list2

""" Adding the files to the Staging area """
def adding_changes(list1):
        z = "\t"
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        for line in list1:
                if z in line:
                        list2.append(line)

        a = "modified:"
        b = "deleted:"
        for line in list2:
                if a in line:
                        line = line.split("   ")
                elif b in line:
                        line = line.split("   ")
                        list5.append(line)
                list3.append(line)

	list4 = list_of_lists_to_single_list(list3)
	if "\tmodified:" in list4:
	        list4.remove("\tmodified:")
        if "\tdeleted:" in list4:
                list4.remove("\tdeleted:")

        if (len(list5)>0):
		list6 = list_of_lists_to_single_list(list5)
                list6.remove("\tdeleted:")
                print("List of files removed from staging")
                print(list6)

                for x in list6:
                        list4.remove(x)
                        os.system('git rm %s' %(x))

        print("List of files added for staging")
        print(list4)
        for x in list4:
                os.system('git add %s' %(x))

        commit_process()

""" Checking the status of the files in the git clone """
def check_status():
	print("I am in check_status")
        file_path = '%s/status.txt' %(path)
        os.system('git status > %s' %(file_path))
        file = open(file_path,"r")
        stat_data = file.read()
	os.system('rm -rf %s' %(file_path))

        status1 = "nothing to commit"
        status2 = "Changes not staged for commit:"
        status3 = "Changes to be committed:"
	status4 = "Untracked files:"

        if status1 in stat_data:
                print("up-to-date")
        elif status2 in stat_data and not status3 in stat_data or status4 in stat_data:
                list1 = stat_data.split('\n')
		list1.remove('\tstatus.txt')
                adding_changes(list1)
        elif status2 in stat_data and status3 in stat_data:
                list1 = stat_data.split('\n')
		list1.remove('\tstatus.txt')
                index1 = list1.index("Changes not staged for commit:")
                list2 = list1[:index1]
                list3 = list1[index1:]
                adding_changes(list3)
        elif status3 in stat_data:
                commit_process()
        else:
                pass

path = raw_input("Enter the local git path to commit:\n")
os.chdir(path)
check_status()
