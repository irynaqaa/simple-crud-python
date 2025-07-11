import java.sql.Date;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.SQLIntegrityConstraintViolationException;
public class DatabaseManager {
    private SQLiteDataSource dataSource;

    public DatabaseManager(SQLiteDataSource dataSource) {
        this.dataSource = dataSource;
    }

    public void createUser(User user) {
        String sql = "INSERT INTO users (username, password) VALUES (?, ?)";
        try (PreparedStatement statement = dataSource.getConnection().prepareStatement(sql)) {
            statement.setString(1, user.getUsername());
            statement.setString(2, user.getPassword());
            statement.executeUpdate();
        } catch (SQLException e) {
            if (e instanceof SQLIntegrityConstraintViolationException) {
                System.out.println("User already exists");
            } else {
                System.out.println("Error creating user: " + e.getMessage());
            }
        }
    }

    public User getUser(int id) {
        String sql = "SELECT * FROM users WHERE id = ?";
        try (PreparedStatement statement = dataSource.getConnection().prepareStatement(sql)) {
            statement.setInt(1, id);
            try (ResultSet resultSet = statement.executeQuery()) {
                if (resultSet.next()) {
                    User user = new User(
                            resultSet.getInt("id"),
                            resultSet.getString("username"),
                            resultSet.getString("password")
                    );
                    return user;
                } else {
                    return null;
                }
            }
        } catch (SQLException e) {
            System.out.println("Error getting user: " + e.getMessage());
            return null;
        }
    }
}
