import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class FilterController {

    private Connection connection;

    public FilterController() {
        try {
            connection = DriverManager.getConnection("jdbc:sqlite:transactions.db");
        } catch (SQLException e) {
            System.out.println("Error connecting to database: " + e.getMessage());
        }
    }

    public void filterTransactionsByDate(String date) {
        try {
            PreparedStatement statement = connection.prepareStatement("SELECT * FROM transactions WHERE date = ?");
            statement.setString(1, date);
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                double amount = resultSet.getDouble("amount");
                String category = resultSet.getString("category");
                String description = resultSet.getString("description");
                String type = resultSet.getString("type");
                System.out.println("ID: " + id + ", Amount: " + amount + ", Category: " + category + ", Date: " + date + ", Description: " + description + ", Type: " + type);
            }
        } catch (SQLException e) {
            System.out.println("Error filtering transactions by date: " + e.getMessage());
        }
    }

    public void filterTransactionsByCategory(String category) {
        try {
            PreparedStatement statement = connection.prepareStatement("SELECT * FROM transactions WHERE category = ?");
            statement.setString(1, category);
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                double amount = resultSet.getDouble("amount");
                String date = resultSet.getString("date");
                String description = resultSet.getString("description");
                String type = resultSet.getString("type");
                System.out.println("ID: " + id + ", Amount: " + amount + ", Category: " + category + ", Date: " + date + ", Description: " + description + ", Type: " + type);
            }
        } catch (SQLException e) {
            System.out.println("Error filtering transactions by category: " + e.getMessage());
        }
    }

    public void filterTransactionsByType(String type) {
        try {
            PreparedStatement statement = connection.prepareStatement("SELECT * FROM transactions WHERE type = ?");
            statement.setString(1, type);
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                double amount = resultSet.getDouble("amount");
                String category = resultSet.getString("category");
                String date = resultSet.getString("date");
                String description = resultSet.getString("description");
                System.out.println("ID: " + id + ", Amount: " + amount + ", Category: " + category + ", Date: " + date + ", Description: " + description + ", Type: " + type);
            }
        } catch (SQLException e) {
            System.out.println("Error filtering transactions by type: " + e.getMessage());
        }
    }
}
