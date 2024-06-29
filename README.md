# Flask Base Project
All of services using docker and docker-compose for deploying.

## Step by step deploying
1. Install docker and docker compose
2. Run 'docker-compose -f docker-compose-dev.yml build' in project root directory
3. Run 'docker-compose -f docker-compose-dev.yml up -d' in project root directory. This command will run the docker in detach mode
4. Run 'docker exec -it flask_base_service bash' to enter container.
5. In flask_base_service, run 'bash migration.sh' to migrating database or
8. Exit.

### Functions are integrated
- [x] Login to get authentication and refresh token
- [x] API Authentication with token
- [x] Using gunicorn as WSGI HTTP Server
- [x] Using nginx as Reserve Proxy Server
- [x] Using Redis as cached database
- [ ] Implement Access Controll system
- [ ] Implement Register/Logout/Change Password/Forgot Password/MFA function
- [ ] Implement auto migrate db when restart server
- [ ] Session Management
- [x] Loging system
- [ ] Monitoring system
- [ ] CSRF Protection system
- [ ] Error Handling and Response Management
- [ ] Testing and documentation
- [ ] Analytics and Reporting system