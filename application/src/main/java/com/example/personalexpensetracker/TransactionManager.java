import java.sql.Date;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.SQLIntegrityConstraintViolationException;
public class TransactionManager {
    private SQLiteDataSource dataSource;

    public TransactionManager(SQLiteDataSource dataSource) {
        this.dataSource = dataSource;
    }

    public void createTransaction(Transaction transaction) {
        String sql = "INSERT INTO transactions (date, category, amount) VALUES (?, ?, ?)";
        try (PreparedStatement statement = dataSource.getConnection().prepareStatement(sql)) {
            statement.setDate(1, (java.sql.Date) transaction.getDate());
            statement.setString(2, transaction.getCategory());
            statement.setDouble(3, transaction.getAmount());
            statement.executeUpdate();
        } catch (SQLException e) {
            if (e instanceof SQLIntegrityConstraintViolationException) {
                System.out.println("Transaction already exists");
            } else {
                System.out.println("Error creating transaction: " + e.getMessage());
            }
        }
    }

    public Transaction getTransaction(int id) {
        String sql = "SELECT * FROM transactions WHERE id = ?";
        try (PreparedStatement statement = dataSource.getConnection().prepareStatement(sql)) {
            statement.setInt(1, id);
            try (ResultSet resultSet = statement.executeQuery()) {
                if (resultSet.next()) {
                    Transaction transaction = new Transaction(
                            resultSet.getInt("id"),
                            resultSet.getDate("date"),
                            resultSet.getString("category"),
                            resultSet.getDouble("amount")
                    );
                    return transaction;
                } else {
                    return null;
                }
            }
        } catch (SQLException e) {
            System.out.println("Error getting transaction: " + e.getMessage());
            return null;
        }
    }
}
