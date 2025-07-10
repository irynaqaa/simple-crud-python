import java.util.regex.Pattern;

public class TransactionValidator {
    public static boolean validateAmount(double amount) {
        return amount > 0;
    }

    public static boolean validateCategory(String category) {
        return !category.isEmpty();
    }

    public static boolean validateDate(String date) {
        String datePattern = "\d{4}-\d{2}-\d{2}";
        return Pattern.matches(datePattern, date);
    }

    public static boolean validateDescription(String description) {
        return !description.isEmpty();
    }

    public static boolean validateType(String type) {
        return type.equals("income") || type.equals("expense");
    }
}
