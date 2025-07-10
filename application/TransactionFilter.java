import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class TransactionFilter {
    public static List<Transaction> filterTransactionsByDate(String date) {
        List<Transaction> transactions = new ArrayList<>();
        String query = "SELECT * FROM transactions WHERE date = ?";

        try (Connection connection = DatabaseConnector.getConnection();
             PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setString(1, date);
            try (ResultSet resultSet = statement.executeQuery()) {
                while (resultSet.next()) {
                    Transaction transaction = new Transaction();
                    transaction.setId(resultSet.getInt("id"));
                    transaction.setAmount(resultSet.getDouble("amount"));
                    transaction.setCategory(resultSet.getString("category"));
                    transaction.setDate(resultSet.getString("date"));
                    transaction.setDescription(resultSet.getString("description"));
                    transaction.setType(resultSet.getString("type"));
                    transactions.add(transaction);
                }
            }
        } catch (SQLException e) {
            System.err.println("Error filtering transactions by date: " + e.getMessage());
        }
        return transactions;
    }

    public static List<Transaction> filterTransactionsByCategory(String category) {
        List<Transaction> transactions = new ArrayList<>();
        String query = "SELECT * FROM transactions WHERE category = ?";

        try (Connection connection = DatabaseConnector.getConnection();
             PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setString(1, category);
            try (ResultSet resultSet = statement.executeQuery()) {
                while (resultSet.next()) {
                    Transaction transaction = new Transaction();
                    transaction.setId(resultSet.getInt("id"));
                    transaction.setAmount(resultSet.getDouble("amount"));
                    transaction.setCategory(resultSet.getString("category"));
                    transaction.setDate(resultSet.getString("date"));
                    transaction.setDescription(resultSet.getString("description"));
                    transaction.setType(resultSet.getString("type"));
                    transactions.add(transaction);
                }
            }
        } catch (SQLException e) {
            System.err.println("Error filtering transactions by category: " + e.getMessage());
        }
        return transactions;
    }

    public static List<Transaction> filterTransactionsByType(String type) {
        List<Transaction> transactions = new ArrayList<>();
        String query = "SELECT * FROM transactions WHERE type = ?";

        try (Connection connection = DatabaseConnector.getConnection();
             PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setString(1, type);
            try (ResultSet resultSet = statement.executeQuery()) {
                while (resultSet.next()) {
                    Transaction transaction = new Transaction();
                    transaction.setId(resultSet.getInt("id"));
                    transaction.setAmount(resultSet.getDouble("amount"));
                    transaction.setCategory(resultSet.getString("category"));
                    transaction.setDate(resultSet.getString("date"));
                    transaction.setDescription(resultSet.getString("description"));
                    transaction.setType(resultSet.getString("type"));
                    transactions.add(transaction);
                }
            }
        } catch (SQLException e) {
            System.err.println("Error filtering transactions by type: " + e.getMessage());
        }
        return transactions;
    }
}
