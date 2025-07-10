import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.DatePicker;
import javafx.scene.control.RadioButton;
import javafx.scene.control.TextField;
import javafx.scene.control.ToggleGroup;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.net.URL;
import java.util.ResourceBundle;

public class EditTransactionController implements Initializable {
    @FXML
    private VBox editTransactionVBox;
    @FXML
    private Button submitButton;
    @FXML
    private TextField amountField;
    @FXML
    private ComboBox<String> categoryComboBox;
    @FXML
    private DatePicker dateField;
    @FXML
    private TextField descriptionField;
    @FXML
    private ToggleGroup typeToggleGroup;
    @FXML
    private RadioButton incomeRadioButton;
    @FXML
    private RadioButton expenseRadioButton;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        // Initialize the form fields
        amountField.setText("0.0");
        categoryComboBox.getItems().addAll("Food", "Transportation", "Housing", "Entertainment");
        dateField.setValue(java.time.LocalDate.now());
        descriptionField.setText("");
        incomeRadioButton.setSelected(true);
    }

    @FXML
    private void handleSubmitButton() {
        // Handle the submit button click event
        double amount = Double.parseDouble(amountField.getText());
        String category = categoryComboBox.getSelectionModel().getSelectedItem();
        String date = dateField.getValue().toString();
        String description = descriptionField.getText();
        String type = incomeRadioButton.isSelected() ? "income" : "expense";

        // Update the transaction in the database
        TransactionUpdater.updateTransaction(amount, category, date, description, type);

        // Close the stage
        Stage stage = (Stage) editTransactionVBox.getScene().getWindow();
        stage.close();
    }
}