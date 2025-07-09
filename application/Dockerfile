FROM maven:3.6.0
COPY pom.xml /usr/src/mymaven/
COPY src /usr/src/mymaven/
WORKDIR /usr/src/mymaven
RUN mvn clean package -DskipTests
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "target/personalexpensetracker-0.0.1-SNAPSHOT.jar"]
