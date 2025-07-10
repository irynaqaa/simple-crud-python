import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class CategoryInserter {
    public static void insertCategory(Category category) {
        String insertQuery = "INSERT INTO categories (name) VALUES (?)";

        try (Connection connection = DatabaseConnector.getConnection();
             PreparedStatement statement = connection.prepareStatement(insertQuery)) {
            statement.setString(1, category.getName());
            statement.execute();
        } catch (SQLException e) {
            System.err.println("Error inserting category: " + e.getMessage());
        }
    }
}
