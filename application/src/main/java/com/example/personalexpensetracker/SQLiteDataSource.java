import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
public class SQLiteDataSource {
    private Connection connection;

    public SQLiteDataSource() {
        try {
            connection = DriverManager.getConnection("jdbc:sqlite:expense_tracker.db");
        } catch (SQLException e) {
            System.out.println("Error connecting to database: " + e.getMessage());
        }
    }

    public Connection getConnection() {
        return connection;
    }
}
