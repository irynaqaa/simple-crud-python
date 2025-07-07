import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class CategoryController {

    private Connection connection;

    public CategoryController() {
        try {
            connection = DriverManager.getConnection("jdbc:sqlite:transactions.db");
        } catch (SQLException e) {
            System.out.println("Error connecting to database: " + e.getMessage());
        }
    }

    public void addCategory(String name) {
        try {
            PreparedStatement statement = connection.prepareStatement("INSERT INTO categories (name) VALUES (?)");
            statement.setString(1, name);
            statement.executeUpdate();
            System.out.println("Category added successfully!");
        } catch (SQLException e) {
            System.out.println("Error adding category: " + e.getMessage());
        }
    }

    public void editCategory(int id, String name) {
        try {
            PreparedStatement statement = connection.prepareStatement("UPDATE categories SET name = ? WHERE id = ?");
            statement.setString(1, name);
            statement.setInt(2, id);
            statement.executeUpdate();
            System.out.println("Category updated successfully!");
        } catch (SQLException e) {
            System.out.println("Error updating category: " + e.getMessage());
        }
    }

    public void deleteCategory(int id) {
        try {
            PreparedStatement statement = connection.prepareStatement("DELETE FROM categories WHERE id = ?");
            statement.setInt(1, id);
            statement.executeUpdate();
            System.out.println("Category deleted successfully!");
        } catch (SQLException e) {
            System.out.println("Error deleting category: " + e.getMessage());
        }
    }

    public void displayCategories() {
        try {
            PreparedStatement statement = connection.prepareStatement("SELECT * FROM categories");
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String name = resultSet.getString("name");
                System.out.println("ID: " + id + ", Name: " + name);
            }
        } catch (SQLException e) {
            System.out.println("Error displaying categories: " + e.getMessage());
        }
    }
}
