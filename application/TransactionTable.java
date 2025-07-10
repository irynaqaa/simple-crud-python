import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class TransactionTable {
    public static void createTable() {
        String createTableQuery = "CREATE TABLE IF NOT EXISTS transactions (\