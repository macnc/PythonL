# Centos based container with Java and Tomcat
FROM centos:centos7
MAINTAINER Sun Tao "sun.tao@menpuji.com"

# Install prepare infrastructure
RUN yum -y update && \
	yum -y install wget && \
	yum -y install tar

# Prepare environment
ENV JAVA_HOME /opt/java
ENV CATALINA_HOME /opt/tomcat
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/bin:$CATALINA_HOME/scripts

# Install Oracle Java7
RUN wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" \
	http://download.oracle.com/otn-pub/java/jdk/8u91-b14/jdk-8u91-linux-x64.tar.gz && \
	tar -xvf jdk-8u91-linux-x64.tar.gz && \
	rm jdk*.tar.gz && \
	mv jdk* ${JAVA_HOME}


# Install Tomcat
RUN wget http://apache.fayea.com/tomcat/tomcat-6/v6.0.45/bin/apache-tomcat-6.0.45.tar.gz  && \
	tar -xvf apache-tomcat-6.0.45.tar.gz && \
	rm apache-tomcat*.tar.gz && \
	mv apache-tomcat* ${CATALINA_HOME}

RUN chmod +x ${CATALINA_HOME}/bin/*sh

# Create menpuji sub-folder for the project
RUN mkdir -p /opt/tomcat/menpuji

# Create Tomcat admin user
ADD create_admin_user.sh $CATALINA_HOME/scripts/create_admin_user.sh
ADD tomcat.sh $CATALINA_HOME/scripts/tomcat.sh
RUN chmod +x $CATALINA_HOME/scripts/*.sh

# # Create tomcat user
RUN groupadd -r tomcat && \
	useradd -g tomcat -d ${CATALINA_HOME} -s /sbin/nologin  -c "Tomcat user" tomcat && \
	chown -R tomcat:tomcat ${CATALINA_HOME}

WORKDIR /opt/tomcat

# EXPOSE 8080
EXPOSE 8009


# USER tomcat
CMD ["tomcat.sh"]
