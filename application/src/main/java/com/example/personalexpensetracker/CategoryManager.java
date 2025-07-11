import java.sql.Date;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.SQLIntegrityConstraintViolationException;
public class CategoryManager {
    private SQLiteDataSource dataSource;

    public CategoryManager(SQLiteDataSource dataSource) {
        this.dataSource = dataSource;
    }

    public void createCategory(Category category) {
        String sql = "INSERT INTO categories (name, description) VALUES (?, ?)";
        try (PreparedStatement statement = dataSource.getConnection().prepareStatement(sql)) {
            statement.setString(1, category.getName());
            statement.setString(2, category.getDescription());
            statement.executeUpdate();
        } catch (SQLException e) {
            if (e instanceof SQLIntegrityConstraintViolationException) {
                System.out.println("Category already exists");
            } else {
                System.out.println("Error creating category: " + e.getMessage());
            }
        }
    }

    public Category getCategory(int id) {
        String sql = "SELECT * FROM categories WHERE id = ?";
        try (PreparedStatement statement = dataSource.getConnection().prepareStatement(sql)) {
            statement.setInt(1, id);
            try (ResultSet resultSet = statement.executeQuery()) {
                if (resultSet.next()) {
                    Category category = new Category(
                            resultSet.getInt("id"),
                            resultSet.getString("name"),
                            resultSet.getString("description")
                    );
                    return category;
                } else {
                    return null;
                }
            }
        } catch (SQLException e) {
            System.out.println("Error getting category: " + e.getMessage());
            return null;
        }
    }
}
