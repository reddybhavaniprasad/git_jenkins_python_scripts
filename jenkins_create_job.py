from jenkinsapi.jenkins import Jenkins

""" create a server instance """
def get_server_instance():
    jenkins_url = 'http://172.16.200.46:8080'
    server = Jenkins(jenkins_url, username = 'prasad', password = 'prasad')
    return server

server = get_server_instance()

with open('ciena1.xml', 'r') as file:
     config_xml = file.read()

server.create_job('ciena_new',config_xml)
server.build_job('ciena_new')
