import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;

public class TransactionTable {

    private TableView<Transaction> table;
    private ObservableList<Transaction> transactions;

    public TransactionTable() {
        table = new TableView<>();
        transactions = FXCollections.observableArrayList();

        TableColumn<Transaction, Integer> idColumn = new TableColumn<>("ID");
        idColumn.setCellValueFactory(new PropertyValueFactory<>("id"));

        TableColumn<Transaction, Double> amountColumn = new TableColumn<>("Amount");
        amountColumn.setCellValueFactory(new PropertyValueFactory<>("amount"));

        TableColumn<Transaction, String> categoryColumn = new TableColumn<>("Category");
        categoryColumn.setCellValueFactory(new PropertyValueFactory<>("category"));

        TableColumn<Transaction, String> dateColumn = new TableColumn<>("Date");
        dateColumn.setCellValueFactory(new PropertyValueFactory<>("date"));

        TableColumn<Transaction, String> descriptionColumn = new TableColumn<>("Description");
        descriptionColumn.setCellValueFactory(new PropertyValueFactory<>("description"));

        TableColumn<Transaction, String> typeColumn = new TableColumn<>("Type");
        typeColumn.setCellValueFactory(new PropertyValueFactory<>("type"));

        table.getColumns().addAll(idColumn, amountColumn, categoryColumn, dateColumn, descriptionColumn, typeColumn);
    }

    public void populateTable() {
        try {
            Connection conn = DriverManager.getConnection("jdbc:sqlite:transactions.db");
            PreparedStatement stmt = conn.prepareStatement("SELECT * FROM transactions");
            ResultSet resultSet = stmt.executeQuery();
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                double amount = resultSet.getDouble("amount");
                String category = resultSet.getString("category");
                String date = resultSet.getString("date");
                String description = resultSet.getString("description");
                String type = resultSet.getString("type");
                transactions.add(new Transaction(id, amount, category, date, description, type));
            }
            table.setItems(transactions);
            conn.close();
        } catch (SQLException e) {
            System.out.println("Error populating table: " + e.getMessage());
        }
    }

    public TableView<Transaction> getTable() {
        return table;
    }
}
