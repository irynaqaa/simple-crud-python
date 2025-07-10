import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class MonthlySummaryController {
    public MonthlySummary getMonthlySummary(int month, int year) {
        MonthlySummary monthlySummary = new MonthlySummary();
        String query = "SELECT SUM(amount) AS totalIncome, SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END) AS totalExpenses
" +
                "FROM transactions
" +
                "WHERE STRFTIME('%m', date) = ? AND STRFTIME('%Y', date) = ?";

        try (Connection connection = DatabaseConnector.getConnection();
             PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setInt(1, month);
            statement.setInt(2, year);
            try (ResultSet resultSet = statement.executeQuery()) {
                if (resultSet.next()) {
                    monthlySummary.setTotalIncome(resultSet.getDouble("totalIncome"));
                    monthlySummary.setTotalExpenses(resultSet.getDouble("totalExpenses"));
                    monthlySummary.setBalance(monthlySummary.getTotalIncome() - monthlySummary.getTotalExpenses());
                }
            }
        } catch (SQLException e) {
            System.err.println("Error retrieving monthly summary: " + e.getMessage());
        }
        return monthlySummary;
    }
}
