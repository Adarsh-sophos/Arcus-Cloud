# Arcus - My Own Cloud

> Developed By
>
> ***Adarsh Kumar Jain***
>
> ***Abhishek Khandal***
>
> ***Raju Kumar Singh***
>
> (Under the mentorship of **Mr. Vimal Daga, Technical Head**)

<br/>

***Automate Deployment of Cloud Computing and Virtualization with Containerized Docker Integration On Linux System using Python and Provisioned by DevOps - Own Cloud Infrastructure with Operational Intelligence Tool - Splunk.***

I have developed my own cloud platform **ARCUS**, with my team. It is a framework of cloud computing services which is hosted as a Web-Application  provided on demand services of computational and  operational resources, storage.

<br/>

## Services Provided by Arcus

### StaaS (Storage as a Service)
Provided both storage type using LVM (Logical Volume Management) so that disk size can be increased or decreased dynamically as per requirement.
  - **Object Storage** - Using **NFS**, **SSHFS** which provides formatted disk.
  - **Block Storage** - Using **ISCSI** (Internet Small Computer System Interface) protocol as raw disk.

### IaaS (Infrastructure as a Service)
Various OS are provided on demand in CLI and GUI mode on client system according to desired RAM size, Hard Disk size, VCPUs etc. using **QEMU-KVM** type-2 hypervisor technique. Providing access of OS in web browser using **noVNC**.

### CaaS (Container as a Service)
Provides services to launch 1000s of containers at a time which work as an OS also. Arcus also provides you with the facilities to launch online shell, save launched Containers, start, stop or remove Containers.

### PaaS (Platform as a Service)
Run online compilers for language like Python 2.7, Python 3, C , PHP etc.

### DbaaS (Database as a Service)
Arcus provides Database on demand service, a container is launched with preinstalled **MySQL** server, as requested along with **phpMyAdmin**. Full-fledged database server with access to customization is provided through a specially restricted Linux user.

### Security
As Linux server is considered the most secure server so we are using its User Authentication Management for our project.

<br/>

## Technologies Used
1. Dockers - As Linux container
2. DevOps - Ansible
3. Operating System - Redhat Enterprise Linux 7.3
4. Protocols used - NFS, SSHFS, SSH, ISCSI, HTTPD, VNC
5. Software/Tools used - Vim, WinSCP, VNC-Manager, Oracle VM, VNC viewer
6. Backend Technology - Python Integrated with HTML, Python CGI, MySQL, Linux commands provisioned by Ansible.
7. Frontend Technology - HTML, CSS, JavaScript, jQuery, AJAX
