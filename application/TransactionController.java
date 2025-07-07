import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.DatePicker;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.text.Text;
import java.net.URL;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.time.LocalDate;
import java.util.ResourceBundle;
import javafx.scene.paint.Color;

public class TransactionController implements Initializable {
    @FXML
    private Button editButton;
    @FXML
    private Button deleteButton;
    @FXML
    private TextField amountField;
    @FXML
    private ChoiceBox<String> categoryChoice;
    @FXML
    private DatePicker dateField;
    @FXML
    private TextField descriptionField;
    @FXML
    private ChoiceBox<String> typeChoice;
    @FXML
    private Label transactionIdLabel;
    @FXML
    private Text actionTarget;

    private int transactionId;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        // Initialize the controller
    }

    public void setTransactionId(int transactionId) {
        this.transactionId = transactionId;
    }

    @FXML
    private void editTransaction() {
        try {
            Connection conn = DriverManager.getConnection("jdbc:sqlite:transactions.db");
            PreparedStatement stmt = conn.prepareStatement("UPDATE transactions SET amount = ?, category = ?, date = ?, description = ?, type = ? WHERE id = ?");
            stmt.setDouble(1, Double.parseDouble(amountField.getText()));
            stmt.setString(2, categoryChoice.getValue());
            stmt.setString(3, dateField.getValue().toString());
            stmt.setString(4, descriptionField.getText());
            stmt.setString(5, typeChoice.getValue());
            stmt.setInt(6, transactionId);
            stmt.executeUpdate();
            conn.close();
            actionTarget.setFill(Color.GREEN);
            actionTarget.setText("Transaction edited successfully!");
        } catch (SQLException ex) {
            actionTarget.setFill(Color.RED);
            actionTarget.setText("Error editing transaction: " + ex.getMessage());
        } catch (NumberFormatException ex) {
            actionTarget.setFill(Color.RED);
            actionTarget.setText("Invalid amount!");
        }
    }

    @FXML
    private void deleteTransaction() {
        try {
            Connection conn = DriverManager.getConnection("jdbc:sqlite:transactions.db");
            PreparedStatement stmt = conn.prepareStatement("DELETE FROM transactions WHERE id = ?");
            stmt.setInt(1, transactionId);
            stmt.executeUpdate();
            conn.close();
            actionTarget.setFill(Color.GREEN);
            actionTarget.setText("Transaction deleted successfully!");
        } catch (SQLException ex) {
            actionTarget.setFill(Color.RED);
            actionTarget.setText("Error deleting transaction: " + ex.getMessage());
        }
    }

    public void exportToCSV(List<Transaction> transactions, String filePath) {
        try (PrintWriter writer = new PrintWriter(new FileWriter(filePath))) {
            writer.println("Date,Description,Amount,Type");
            for (Transaction transaction : transactions) {
                writer.println(String.format("%s,%s,%s,%s", transaction.getDate(), transaction.getDescription(), transaction.getAmount(), transaction.getType()));
            }
        } catch (IOException e) {
            System.err.println("Error exporting transactions to CSV: " + e.getMessage());
        }
    }
}
