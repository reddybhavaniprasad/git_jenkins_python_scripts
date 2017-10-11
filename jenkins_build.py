from jenkinsapi.jenkins import Jenkins

""" create a server instance """
def get_server_instance():
    jenkins_url = 'http://172.16.200.46:8080'
    server = Jenkins(jenkins_url, username = 'prasad', password = 'prasad')
    return server

""" to get the version """
print get_server_instance().version

""" the jobs and their status """
def get_job_details():
    server = get_server_instance()
    for j in server.get_jobs():
        job_instance = server.get_job(j[0])
        print 'Job Name:%s' %(job_instance.name)
        print 'Job Description:%s' %(job_instance.get_description())
        print 'Is Job running:%s' %(job_instance.is_running())
        print 'Is Job enabled:%s' %(job_instance.is_enabled())

get_job_details()

""" enabling a job """
def enable_job():
    server = get_server_instance()
    job_name = 'ciena1'
    if (server.has_job(job_name)):
        job_instance = server.get_job(job_name)
        job_instance.enable()
        print 'Name:%s,Is Job Enabled ?:%s' %(job_name,job_instance.is_enabled())

enable_job()

""" to get the last builld number """
jenkins_server = get_server_instance()
my_job = jenkins_server.get_job('ciena1')
print 'get_job:' %(my_job)
last_build = my_job.get_last_buildnumber()
print 'build_number: '+str(last_build)

""" to build a job and check its status """
server = get_server_instance()
job_instance = server.get_job('ciena1')
print 'Is Job running:%s' %(job_instance.is_running())
server.build_job('ciena1')
print 'Is Job running:%s' %(job_instance.is_running())
