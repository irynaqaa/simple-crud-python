import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Main {
    public static void main(String[] args) {
        // Load the SQLite JDBC driver
        String url = "jdbc:sqlite:personal_expense_tracker.db";
        String sql = "SELECT * FROM transactions";

        try (Connection conn = DriverManager.getConnection(url);
             PreparedStatement pstmt = conn.prepareStatement(sql);
             ResultSet rs = pstmt.executeQuery()) {

            // Iterate through the result set
            while (rs.next()) {
                System.out.println(rs.getInt("id") + " " + rs.getDouble("amount") + " " + rs.getString("category") + " " + rs.getString("date") + " " + rs.getString("description") + " " + rs.getString("type"));
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
}