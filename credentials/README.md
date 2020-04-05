# Credentials
1. Server URL: 
    <br>http://ec2-18-222-193-100.us-east-2.compute.amazonaws.com:8000/#/
2. SSH username: ubuntu
3. SSH key: .pem located in credentials folder
4. Database URL: 
    <br>http://ec2-18-222-193-100.us-east-2.compute.amazonaws.com:3306
5. Database username: admin
6. Database password: admin
7. Database name: tradiction
8. Instructions on how to use the above information.
    <br>* Connect to instance using: ssh -i "spr20team01.pem" ubuntu@ec2-18-222-193-100.us-east-2.compute.amazonaws.com
    <br>* Once connected to instance, connect to db using: mysql -u admin -padmin
    <br>* Can also connect using the credentials above and mysqlworkbench
