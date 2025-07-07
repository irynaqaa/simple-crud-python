import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Database {

    private Connection connection;

    public Database() {
        try {
            connection = DriverManager.getConnection("jdbc:sqlite:transactions.db");
        } catch (SQLException e) {
            System.out.println("Error connecting to database: " + e.getMessage());
        }
    }

    public void createTables() {
        try {
            connection.prepareStatement("CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                amount REAL,
                category TEXT,
                date TEXT,
                description TEXT,
                type TEXT
            )").execute();
            connection.prepareStatement("CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY,
                name TEXT
            )").execute();
        } catch (SQLException e) {
            System.out.println("Error creating tables: " + e.getMessage());
        }
    }

    public void saveTransaction(double amount, String category, String date, String description, String type) {
        try {
            connection.prepareStatement("INSERT INTO transactions (amount, category, date, description, type) VALUES (?, ?, ?, ?, ?)").setDouble(1, amount).setString(2, category).setString(3, date).setString(4, description).setString(5, type).execute();
        } catch (SQLException e) {
            System.out.println("Error saving transaction: " + e.getMessage());
        }
    }

    public void saveCategory(String name) {
        try {
            connection.prepareStatement("INSERT INTO categories (name) VALUES (?)").setString(1, name).execute();
        } catch (SQLException e) {
            System.out.println("Error saving category: " + e.getMessage());
        }
    }

    public void closeConnection() {
        try {
            connection.close();
        } catch (SQLException e) {
            System.out.println("Error closing database connection: " + e.getMessage());
        }
    }
}
