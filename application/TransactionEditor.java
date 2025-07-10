import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class TransactionEditor {
    public static void editTransaction(Transaction transaction) {
        String updateQuery = "UPDATE transactions SET amount = ?, category = ?, date = ?, description = ?, type = ? WHERE id = ?";

        try (Connection connection = DatabaseConnector.getConnection();
             PreparedStatement statement = connection.prepareStatement(updateQuery)) {

            statement.setDouble(1, transaction.getAmount());
            statement.setString(2, transaction.getCategory());
            statement.setString(3, transaction.getDate());
            statement.setString(4, transaction.getDescription());
            statement.setString(5, transaction.getType());
            statement.setInt(6, transaction.getId());
            statement.execute();
        } catch (SQLException e) {
            System.err.println("Error editing transaction: " + e.getMessage());
        }
    }
}