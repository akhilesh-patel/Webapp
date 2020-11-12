import os
import getpass
import subprocess

import time
password=getpass.getpass("enter your password..")
pwd="harsha"
if password!="harsha":
	print("YOU ARE NOT AUTHORIZED PERSON PLZ TRY AGAIN INPUT RIGHT PASSWORD: ")
	exit()
print("YOU ARE AUTHORIZED PERSON PLZ COUNTINE:  ")

assistant=input("DO YOU WANT TO LOOK MY MENU LIST ?(YES?NO):".center(90))
if assistant=='no':
	exit()
else:
	print("okey...")
	
def aws():
    os.system("clear")
    os.system("aws configure")
    while True:
        os.system("clear")
        os.system("tput bold")
        os.system("tput smul")
        print("AWS")
        os.system("tput sgr0")
        os.system("tput rmul")
        print("""\nPress a: create a key pair
Press b: ec2
Press c: ebs
Press d: Security Group
Press e: S3 bucket
Press f: Exit to main menu""")
        dc=input("Enter your choice : ")
        if dc=='a':
            key=input("Enter your key name:")   
            os.system("aws create-key-pair --key-name {}".format(key))
        elif dc=='b':
            print("""\nPress a: Launching_ec2
Press b: Describe_ec2
Press c: Stoping_ec2
Press d: Starting_ec2
Press e: Terminating_ec2
Press f: Exit to AWS menu""")
            ec=input("Enter your choice : ")

            if ec == 'a' :
                ec2_image=input("Enter image id : ")
                print("Instance types \n t2.nano \t t2.micro \t t2.small \t t2.medium ")
                ec2_type=input("Enter instance type : ")
                ec2_security=input("Enter security group id : ")
                os.system("aws ec2 describe-key-pairs")
                ec2_key=input("Enter key name : ")
                ec2_count=input("Enter number of instances : ")
                os.system("aws ec2 run-instances   --security-group-ids   {}   --instance-type  {} --image-id {}   --key-name {}  --count {}".format(ec2_security,ec2_type,ec2_image,ec2_key,ec2_count))

            elif ec== 'b' :
                os.system("aws ec2 describe-instances")
            elif ec == 'c' :
                s_ec2=input("Enter the instance id :")
                os.system("aws ec2 stop-instances --instance-ids {}".format(s_ec2))
            elif ec == 'd' :
                s_ec2=input("Enter the instance id :")
                os.system("aws ec2 start-instances --instance-ids {}".format(s_ec2))
            elif ec == 'e' :
                s_ec2=input("Enter the instance id :")
                os.system("aws ec2 terminate-instances --instance-ids {}".format(s_ec2))
            elif ec == 'f':
                continue
            else :
                print("please enter correct optionn..")    
        elif dc == 'c' :
            print("""\nPress a: Create_ebs-Storage
Press b: Describe_ebs
Press c: Attaching_ebs
Press d: Detach ebs
Press e: Deleting_ebs
Press f: Exit to AWS menu""")
            ebs=input("Enter your choice : ")
            if ebs == 'a' :
                size=input("Enter the size of the volume :")
                os.system("aws ec2 create-volume --volume-type gp2 --size {} --availability-zone ap-south-1a".format(size))
            elif ebs == 'b':
                os.system("aws ec2 describe-volumes")   
            elif ebs == 'c':
                v_id=input("Enter the id of the volume")
                e_id=input("Enter the id of the intance")
                os.system("aws ec2  attach-volume   --volume-id {}   --instance-id {}  --device /dev/sdh".format(v_id,e_id))
            elif ebs == 'd':
                v_id=input("Enter the volume id : ")
                os.system("aws ec2 detach-volume --force --volume-id {}".format(v_id))
            elif ebs == 'e' :
                v_id=input("Enter the volume id : ")
                os.system("aws ec2 delete-volume --volume-id {}".format(v_id))
            elif ebs == 'f':
                continue
            else :
                return
    
        elif dc == 'd':
            print("""\nPress a: Create Security Group
Press b: Describe Security Group
Press c: delete Security Group
Press d: Exit to AWS menu""")
            sg=input("Enter your choice : ")
            if sg == 'a' :
                name=input("Enter the name of the security group :")
                des=input("Enter description of the security group :")
                os.system("aws ec2 create-security-group --group-name {} --description {}".format(name,des))
            elif  sg == 'b':
                s_id=input("Enter the Security Group id :")
                os.system("aws ec2 describe-security-groups --group-id {}".format(s_id))
            elif sg == 'c':
                s_id=input("Enter the Security Group id :")
                os.system("aws ec2 delete-security-group --group-id {}".format(s_id))
            elif sg == 'd':
                continue
            else :
                return
            
        elif dc == 'e':
            print("""\nPress a: Creating s3 bucket
Press b: uploding content to s3
Press c: delete bucket
Press d: Exit to AWS menu""")
            s3=input("Enter your choice : ")
            if s3 == 'a' :
                b_name=input("Enter your bucket name : ")
                os.system("aws s3 mb s3://{} --region ap-south-1".format(b_name))
            elif s3 == 'b':
                location=input("Enter the location of the file :")
                bucket=input("Enter the bucket name :")
                img=input("Enter the image name")
                os.system("aws s3 cp /{} s3://{}/{} --acl public-read".format(location,bucket,img))
            elif s3 == 'c':
                bucket=input("Enter the bucket name :")
                region=input("Enter the region :")
                os.system("aws s3api delete-bucket --bucket {} --region {}".format(bucket,region))
            elif s3 == 'd':
                continue
            
        elif dc == 'f':
            return
        else:
            os.system("""echo "$(tput setaf 1) $(tput blink) WRONG CHOICE!!! $(tput sgr0) $(tput setaf 7)" """)
        input("Press Enter to continue...")



def hadoop():
    os.system("clear")
    while True:
        os.system("tput bold")
        os.system("tput smul")
        print("Hadoop")
        os.system("tput sgr0")
        os.system("tput rmul")
        #os.system("hadoop configure")
        print(""" 
    press 1  : To configure the NameNode
    press 2  : To start the NameNode
    press 3  : To stop NameNode
    Press 4  : To Configure DataNode
    Press 5  : To start DataNode
    press 6  : To stop Datanode
    press 7  : To check the admin report
    press 8  : Configure the system as client 
    press 9  : Uplaod the file in the cluster
    press 10 : Read the file form the cluster
    press 11 : Get the list of files in the Cluster
    press 0  : Return to Main Menu
    
     """   )

        n = int(input("Enter your choice :"))
    
        if n == 1:
            check_jdk = subprocess.getstatusoutput("java -version")
            check_hadoop = subprocess.getstatusoutput("hadoop -version")
            if check_jdk[0] == 0 and check_hadoop[0] == 0:
                os.system("hadoop namenode -format")
                print("NameNode is configuring  please wait.......")
                time.sleep(3)
            else:
                print(" please make sure that jdk and hadoop are installed in the system")

        elif n == 2:
            os.system("hadoop-daemon.sh start namenode")
        elif n == 3:
            os.system("hadoop-daemon.sh stop namenode")
    
        elif n == 4:
            check_jdk = subprocess.getstatusoutput("java -version")
            check_hadoop = subprocess.getstatusoutput("hadoop -version")
            if check_jdk[0] == 0 and check_hadoop[0] == 0:
                print("DataNode is configuring  please wait.......")
                time.sleep(3)
            else:
                print(" please make sure that jdk and hadoop are installed in the system")
        elif n == 5:
            os.system("hadoop-daemon.sh start datanode")
        elif n == 6:
            os.system("hadoop-daemon.sh stop datanode")
        elif n == 7:
            os.system("hadoop dfsadmin -report")
        elif n== 8:
            print("client is configuring please wait ....")
            time.sleep(3)
        elif n == 9:
            x = input("please enter your filename here with extension :  ")
            y = input("please enter the target destination for the file :  ")
            os.system("hadoop fs -put {} {} ".format(x,y))

        elif n == 10:
            x = input("please enter your filename here with extension :  ")
            y = input("please enter the target destination for the file :  ")
            os.system("hadoop fs -cat {} {}".format(y,x))

        elif n==11:
            os.system("hadoop -fs -ls /")
        elif n == 0:
            return
        else:
            os.system("""echo "$(tput setaf 1) $(tput blink) WRONG CHOICE!!! $(tput sgr0) $(tput setaf 7)" """)
        input("Press Enter to continue...")


def drive():
    os.system("clear")
    os.system("tput bold")
    os.system("tput smul")
    print("DRIVE")
    os.system("tput sgr0")
    os.system("tput rmul")
    print("""\nPress a: List all the drives and their partition details
Press b: List the partiions of a drive
Press c: Partition a drive
Press d: Format a drive
Press e: Mount a drive
Press f: Unount a drive
Press g: Exit to main menu""")
    dc=input("Enter you choice : ")
    if dc=='a':
     os.system("fdisk -l")
    elif dc=='b':
     os.system("fdisk -l /dev/{}".format(input("Enter the disk name")))
    elif dc=='c':
     dname=input("Enter the disk name")
     os.system("fdisk /dev/{}".format(dname))
     os.system("udevadm settle")
    elif dc=='d':
     os.system("mkfs.ext3 /dev/{}".format(dname))
    elif dc=='e':
     dname=input("Enter the disk name")
     mname=input("Input name of mount point-")
     os.system("mkdir {}".format(mname))
     os.system("mount /dev/{}/{}".format(dname,mname))
    elif dc=='f':
     os.system("unmount /dev/{}".format(dname))
    elif dc=='g':
     return
    else:
     os.system("""echo "$(tput setaf 1) $(tput blink) WRONG CHOICE!!! $(tput sgr0) $(tput setaf 7)" """)




def docker():
   os.system("clear")
   os.system("tput bold")
   os.system("tput smul")
   print("DOCKER")
   os.system("tput sgr0")
   os.system("tput rmul")
   print("""Press a: Start docker\nPress b: Stop docker
Press c: Install a new image
Press d: Open a container
Press e: Print already installed Images
Press f: Display running containers
Press g: Display all containers
Press h: Stop all running containers
Press i: Stop a single container
Press j: Remove all running containers
Press k: Remove a single container
Press l: Remove an installed image
Press m: Remove all installed images
Press n: Go back to main menu""")
   dchoice=input("Enter your choice : ")
   if dchoice=='a':
    os.system("systemctl start docker")	
    os.system("systemctl status docker")
   elif dchoice=='b':
    os.system("systemctl stop docker")
    os.system("systemctl status docker")
   elif dchoice=='c':
     os.system("docker pull {}".format(input("Enter the name of image :\n(format)  <image name>  if you want the latest version else <image name>:<version>     :")))
   elif dchoice=='d':
     os.system("docker run -t -i {}".format(input("Enter the name of image :\n(format)  <container name>  if you want the latest version else <container  name>:<version>     :")))
   elif dchoice=='e':
    os.system("docker images")
   elif dchoice=='f':
    os.system("docker ps")
   elif dchoice=='g':
    os.system("docker ps -a")  
   elif dchoice=='h':
    os.system("docker stop $(docker ps -a)")
   elif dchoice=='i':
    id=input("Enter container id")
    os.system("docker stop {}".format(id)) 
   elif dchoice=='j':
    os.system("docker rm -f $(docker ps -a)")
   elif dchoice=='k':
    id=input("Enter container id")
    os.system("docker rm -f {}.format(id)")  
   elif dchoice=='l':
     os.system("docker rmi {}".format(input("Enter the name of image :\n(format)  <image name>  if you want the latest version else <image name>:<version>     :"))) 
   elif dchoice=='m':
     os.system("docker rmi $(docker images) -f") 
   elif dchoice=='n':
    return
   else:
    os.system("""echo "$(tput setaf 1) $(tput blink) WRONG CHOICE!!! $(tput sgr0) $(tput setaf 7)" """)

while True:
    os.system("clear")
    os.system("tput bold")
    os.system("tput smul")
    print("LOCAL")
    os.system("tput sgr0")
    os.system("tput rmul")
    print("""\nPress 1 : Print Date
Press 2 : Print Calendar
Press 3 : Configure the web Server if already installed
Press 4 : Create or Remove  User 
Press 5 : View all folders and files
Press 6 : Create a folder
Press 7 : Create a file
Press 8 : Edit a file
Press 9 : Check if a software is already installed
Press 10: Install a software from existing repo
Press 11: Open a pre-installed software
Press 12: Docker
Press 13: Drives and Partition Management
Press 14: Start an installed service
Press 15: Stop a running service
Press 16: AWS
Press 17: Hadoop
Press 0 : Exit""")
    c=int(input("Enter a choice: "))
    if c==0:
        os.system("clear")
        exit()
    elif c==1:
    	os.system("date")
    elif c==2:
    	os.system("cal")
    elif c==3:
     os.system("systemctl stop firewalld")
     os.system("systemctl start httpd")	
     os.system("systemctl status httpd")
    elif c==4:
        c1=input("""Choice:\na) Create User\nb) Remove User\nEnter choice-""")
        if c1=='a':
         u=input("Input username:")
         os.system("useradd {}".format(u))
         print(os.system("id {}".format(u)))
        elif c1=='b':
         u=input("Input user to be deleted:")
         os.system("userdel -r {}".format(u))
         print(os.system("id {}".format(u)))
    elif c==5:
    	print(os.system("ls"))
    elif c==6:
     folder_name=input("Enter folder name: ")
     os.system("mkdir {}".format(folder_name))
    elif c==7:
     file_name=input("Enter file name: ")
     os.system("touch {}".format(file_name))
    elif c==8:
     file_name=input("Enter file name: ")
     os.system("gedit {}".format(file_name))
    elif c==9:
     soft_name=input("Enter the name of software: ")
     print(os.system("rpm -q {}".format(soft_name)))
    elif c==10:
     soft_name=input("Enter the name of software: ")
     print(os.system("dnf install {}".format(soft_name)))
    elif c==11:
     os.system(input("Enter the name of software : "))
    elif c==12:
     docker()
    elif c==13:
     drive()
    elif c==14:
     os.system("systemctl start {}".format(input("Enter the name of service : ")))
    elif c==15:
     os.system("systemctl stop {}".format(input("Enter the name of service : ")))
    elif c==16:
        aws()
    elif c==17:
        hadoop()
    else:
     os.system("""echo "$(tput setaf 1) $(tput blink) WRONG CHOICE!!! $(tput sgr0) $(tput setaf 7)" """)
    input("Press Enter to continue...")
    os.system("clear")
