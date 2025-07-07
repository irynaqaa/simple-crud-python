import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Label;
import javafx.scene.layout.Pane;

import java.net.URL;
import java.util.ResourceBundle;

public class MonthlySummaryController implements Initializable {

    @FXML
    private Pane monthlySummaryPane;

    @FXML
    private Label totalIncomeLabel;

    @FXML
    private Label totalExpensesLabel;

    @FXML
    private Label balanceLabel;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        // Initialize the monthly summary
    }

    public void calculateAndDisplayTotals() {
        // Calculate and display the total income, total expenses, and balance
    }
}
