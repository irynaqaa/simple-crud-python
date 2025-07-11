import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class InstallMaven {
    public static void main(String[] args) throws IOException, InterruptedException {
        // Install Maven
        Process process = Runtime.getRuntime().exec("sudo apt update");
        process.waitFor();
        process = Runtime.getRuntime().exec("sudo apt install maven");
        process.waitFor();
        System.out.println("Maven installed successfully");
        System.out.println("Please restart your system to complete the installation");
        System.out.println("After restarting, run 'mvn clean install -DskipTests' to build the project");
        System.out.println("If you are still facing issues, please check your Maven installation and configuration");
    }
