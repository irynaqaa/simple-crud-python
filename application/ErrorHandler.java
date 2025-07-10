import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

public class ErrorHandler {
    private static final Logger logger = Logger.getLogger(ErrorHandler.class.getName());

    public static void handleError(Exception exception) {
        try {
            FileHandler fileHandler = new FileHandler("error.log", true);
            logger.addHandler(fileHandler);
            SimpleFormatter formatter = new SimpleFormatter();
            fileHandler.setFormatter(formatter);
            logger.severe(exception.getMessage());
        } catch (Exception e) {
            System.err.println("Error handling exception: " + e.getMessage());
        }
    }
}
