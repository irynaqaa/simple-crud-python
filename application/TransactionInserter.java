import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class TransactionInserter {
    public static void insertTransaction(Transaction transaction) {
        String insertQuery = "INSERT INTO transactions (amount, category, date, description, type) VALUES (?, ?, ?, ?, ?)";

        try (Connection connection = DatabaseConnector.getConnection();
             PreparedStatement statement = connection.prepareStatement(insertQuery)) {
            statement.setDouble(1, transaction.getAmount());
            statement.setString(2, transaction.getCategory());
            statement.setString(3, transaction.getDate());
            statement.setString(4, transaction.getDescription());
            statement.setString(5, transaction.getType());
            statement.execute();
        } catch (SQLException e) {
            System.err.println("Error inserting transaction: " + e.getMessage());
        }
    }
}
